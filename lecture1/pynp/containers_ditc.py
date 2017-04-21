#!python27
d = { 'cat':'cute', 'dog':'furry'}
print d['cat']
print 'cat' in d # ture or false
print 'cute' in d
d['fish'] = 'wet'
print d
print d.get('pig','fat') # get an element with a default

print "-----------------------------"

d = {'person':2 , "cat":4,"sipder":8}
for animal in d:# key list
    legs = d[animal]
    print "A %s has %d legs" % (animal, legs)
print "-------------------"
nums = [0, 1, 2 ,3 ,4]
even_num_to_squre = {x:x ** 2 for x in nums}
print even_num_to_squre
