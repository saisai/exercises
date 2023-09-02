

#class MixinA(object):
class MixinA:

    def __init__(self, test):
        self.test = test
    
    def hello(self):
        print(self.test)
        print(self.age)
        print(self.hair_color)
        
#class MixinB(object):
class MixinB:

    name = "MixinB"
    
    def b_hello(self):
        for i in self.get_generator():
            print(i, end=" ")
        
    
    
        
        
        
class Hello(MixinA, MixinB):
    
    hair_color = "white"
    
    def __init__(self, name, age):
        super(Hello, self).__init__(name)
        self.age = age

    def get_generator(self):
        for i in range(10):
            yield i

if __name__ == '__main__':
    t = Hello("Richard", 30)    
    t.hello()    
    t.b_hello()
    print(t.name)