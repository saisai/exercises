import multiprocessing


class ProcessedLine():
    def __init__(self, text : str) -> None:
        self.text, group = text.strip().split()
        self.group = int(group)
        self.link = text.split('_from')[0]
        self.dict = {self.link: {self.group: set([self.text])}}

def process_line(text : str):
    processed_line = ProcessedLine(text)
    return processed_line

def compute_chunksize(iterable_size, pool_size):
    chunksize, remainder = divmod(iterable_size, 4 * pool_size)
    if remainder:
        chunksize += 1
    return chunksize

def main():

    def generate_lines():
        with open('dummy.txt') as f:
            for line in f:
                yield line

    ESTIMATED_NUMBER_OF_LINES_IN_FILE = 7
    POOL_SIZE = min(ESTIMATED_NUMBER_OF_LINES_IN_FILE, multiprocessing.cpu_count())
    # chunksize to be used with imap_unordered:
    chunksize = compute_chunksize(ESTIMATED_NUMBER_OF_LINES_IN_FILE, POOL_SIZE)
    pool = multiprocessing.Pool(POOL_SIZE)
    # Specify a chunksize value if the size of the iterable is large
    results = {}
    for processed_line in pool.imap_unordered(process_line, generate_lines(), chunksize=chunksize):
        link = processed_line.link
        if link not in results:
            # Just update with the entire dictionary
            results.update(processed_line.dict)
        else:
            # Update the set dictionary:
            set_dict = results[link]
            set_key = processed_line.group
            if set_key in set_dict:
                set_dict[set_key].add(processed_line.text)
            else:
                #set_dict[set_key] = set(processed_line.text)
                set_dict[set_key] = processed_line.dict[link][set_key]
    pool.close()
    pool.join()

    for group_name, groups in results.items():
        print(f'Group Name {group_name} has the following:')
        for k, v in groups.items():
            print('   ', k, '->', v)
        print()

if __name__ == "__main__":
    main()

    # https://stackoverflow.com/questions/71119918/mutate-a-shared-object-in-python-multiprocessing