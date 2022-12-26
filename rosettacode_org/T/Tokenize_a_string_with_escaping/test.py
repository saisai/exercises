
def hello(s):

    def test(s):
        print(s)
        def tt(b):
            print(s, b)
            def cc(d):
                print(d)

            return cc
        return tt

    return test(s)


hello("h")("b")("c")

