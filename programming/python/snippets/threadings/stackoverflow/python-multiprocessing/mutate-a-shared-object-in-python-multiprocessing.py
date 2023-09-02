import multiprocessing

def init_processes(d, the_lock):
    global conns, lock
    conns, lock = d, the_lock

class Line():
    def __init__(self, text, group) -> None:
        self.text = text
        self.group = int(group)

    def get_link(self):
        return self.text.split('_from')[0]

    def __repr__(self):
        return f"<{self.group},{self.text}>"

class Groups():

    def __init__(self, name ) -> None:
        self.name = name
        self.groups = {k:set() for k in [10,20,30]}

    def add_to_dict(self,line : Line):

        #connection = line.get_link()
        connection = line.group
        if connection not in self.groups.keys():
            self.groups[connection] = set()

        self.groups[connection].add(line.text)


def thread_f(item : Line):

    # Update the dictionary of every Group object accordingly
    global conns # Not strictly necessary

    key = item.get_link()

    # We need to let the managed dict know there is an updated value for the key:
    """
    conns[key].add_to_dict(item)
    """
    with lock:
        the_set = conns[key]
        the_set.add_to_dict(item)
        conns[key] = the_set # reset the reference

def main():

    # Parse the file and store the information in an iterable
    with open('dummy.txt') as f:

        info = [ Line(*line.strip().split()) for line in f]

    # Update the global (shared) object and initialize a dictionary
    # this has the following initialization:
    # { a_to_b : set(), c_to_f : set() }
    conns = multiprocessing.Manager().dict(
        { k : Groups(k) for k in {x.get_link() for x in info} }
    )

    # Update the shared object according to the iterable information
    lock = multiprocessing.Lock()
    with multiprocessing.Pool(5, initializer=init_processes, initargs=(conns, lock)) as pool:

        res = pool.map(thread_f,     # add to the appropriate key the items
                        info,        # the lines
                        chunksize=1) # respect the order

    # Display the Results
    for group_name, group_obj in conns.items():

        print(f"Grp Name {group_name} has the following:")

        for cost, connections in group_obj.groups.items():

            print(cost,connections)


if __name__ == "__main__":
    main()

    # https://stackoverflow.com/questions/71119918/mutate-a-shared-object-in-python-multiprocessing