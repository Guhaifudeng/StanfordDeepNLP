#!python27
animals = {'cat', 'dog'}
print 'cat' in animals
animals.add('fish')
print animals
print len(animals)
animals.remove('cat')
print len(animals)
animals.add('pig')
print animals

for idx , animal in enumerate(animals):
    print '# %d: %s' % (idx, animal)
print '---------------'

from math import sqrt
nums = { int(sqrt(x)) for x in range(30)}
print nums
