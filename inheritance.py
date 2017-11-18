#Understanding inheritance using classes in python programming language.

#Parent Class
class A(object):
    def go(self):
        print("go A go!")
    def stop(self):
        print("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")
        
#Child of A
class B(A):
    def go(self):
        super(B, self).go()
        print("go B go!")
        
#Child of A
class C(A):
    def go(self):
        super(C, self).go()
        print("go C go!")
    def stop(self):
        super(C, self).stop()
        print("stop C stop!")
        
#Child of B and C
class D(B,C):
    def go(self):
        super(D, self).go()
        print("go D go!")
    def stop(self):
        super(D, self).stop()
        print("stop D stop!")
    def pause(self):
        print("wait D wait!")
        
#Child of B and C
class E(B,C): pass

#creating objects of each class
a = A()
b = B()
c = C()
d = D()
e = E()

# specify output from here onwards, run each command below one by one and try to understand.

a.go()
b.go()
c.go()
d.go()
e.go()

a.stop()
b.stop()
c.stop()
d.stop()
e.stop()

a.pause()
b.pause()
c.pause()
d.pause()
e.pause()
