#!python27
x = 1
print  type(x)
x = (x + 1) ** 2
print type(x)
print x
x = x ** 0.3
print x
x = 1.0
print type(x)
x += 1
print x
print "-----------------------------"
f = False
t = True
print f and t
print f or t
print not f
print "-----------------------------"
s1 = 'sdsdsd1'
print s1
print type(s1)
s2 = "sdsdsd2"
print s2
print type(s2)
print s1 + s2
print s1 + " " +s2
print "%s %s %d" % (s1,s2,14)

print "------------------------------"
s = "hello"
print s.capitalize()
reps =  s.replace("l",'my love')
print reps
print type(reps.strip())
