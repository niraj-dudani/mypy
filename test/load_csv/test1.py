import mypy
import pprint

pp = pprint.PrettyPrinter()

print "=== Default args. (delimiter = '\\t') ==="
pp.pprint( mypy.load_csv( 'sample1.dat' ) )

print
print "=== Delimiter = ' ' ==="
pp.pprint( mypy.load_csv( 'sample1.dat', delimiter = ' ' ) )

print
print "=== Delimiter = ' ', comment = '#' ==="
pp.pprint( mypy.load_csv( 'sample1.dat', delimiter = ' ', comment = '#' ) )

print
print "=== Delimiter = ' ', comment = '#;' ==="
pp.pprint( mypy.load_csv( 'sample1.dat', delimiter = ' ', comment = '#;' ) )

print
print "=== Delimiter = ' ', comment = '#', skip_empty_lines = True ==="
pp.pprint( mypy.load_csv( 'sample1.dat', delimiter = ' ', comment = '#', skip_empty_lines = True ) )

print
print "=== Delimiter = ' ', comment = '#', skip_empty_entries = 'ends' ==="
pp.pprint( mypy.load_csv( 'sample1.dat', delimiter = ' ', comment = '#', skip_empty_entries = 'ends' ) )

print
print "=== Delimiter = ' ', comment = '#;', skip_empty_entries = 'ends' ==="
pp.pprint( mypy.load_csv( 'sample1.dat', delimiter = ' ', comment = '#;', skip_empty_entries = 'ends' ) )

print
print "=== Delimiter = ' ', comment = '#', skip_empty_entries = 'ends', skip_empty_lines = True ==="
pp.pprint( mypy.load_csv( 'sample1.dat', delimiter = ' ', comment = '#', skip_empty_entries = 'ends', skip_empty_lines = True ) )

print
print "=== Delimiter = ' ', comment = '#', skip_empty_entries = 'all' ==="
pp.pprint( mypy.load_csv( 'sample1.dat', delimiter = ' ', comment = '#', skip_empty_entries = 'all' ) )

print
print "=== Delimiter = ' ', comment = '#', skip_empty_entries = 'all', skip_empty_lines = True ==="
pp.pprint( mypy.load_csv( 'sample1.dat', delimiter = ' ', comment = '#', skip_empty_entries = 'all', skip_empty_lines = True  ) )
