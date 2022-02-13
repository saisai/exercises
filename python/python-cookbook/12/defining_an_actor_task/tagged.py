from actor import Actor

class TaggedActor(Actor):
    def run(self):
        while True:
            tag, *payload = self.recv()
            getattr(self, "do_"+tag)(*payload)


    # Methods corresponding to different message tags
    def do_A(self, x):
        print("Running A", x)

    def do_B(self, x, y):
        print("Running B", x, y)

if __name__ == '__main__':
    a = TaggedActor()
    a.start()
    a.send(('A', 1)) # Invoke do_A(1)
    a.send(('B', 2, 3)) # Invokes do_B(2, 3)
    for i in range(0, 10):
        a.send(('B', i, i))

    a.close()
    a.join()

