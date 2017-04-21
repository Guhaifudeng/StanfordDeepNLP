#!python27
class Greeter(object):
    #Constructor
    def  __init__(self, name):
        self.name = name #create an instance variable
    #instance method
    def  greet(self, loud = False):
        if loud:
            print 'HELLO, %s' % self.name.upper()
        else:
            print 'Hello, %s' % self.name

g = Greeter('Fred')
g.greet()
g.greet(loud = True)
