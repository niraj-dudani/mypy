import mypy
import pprint

pp = pprint.PrettyPrinter()

print "=== Delimiter = ' ', comment = '#' ==="
pp.pprint( mypy.load_csv( 'sample2.dat', delimiter = ' ', comment = '#' ) )

print
print "=== Delimiter = ' ', comment = '#', cast = str ==="
pp.pprint( mypy.load_csv( 'sample2.dat', delimiter = ' ', comment = '#', cast = str ) )

print
print "=== Delimiter = ' ', comment = '#', cast = float ==="
try:
	pp.pprint( mypy.load_csv( 'sample2.dat', delimiter = ' ', comment = '#', cast = float ) )
except Exception as message:
	print message,

print
print "=== Delimiter = ' ', comment = '#', cast = float, skip_empty_entries = 'ends' ==="
try:
	pp.pprint( mypy.load_csv( 'sample2.dat', delimiter = ' ', comment = '#', cast = float, skip_empty_entries = 'ends' ) )
except Exception as message:
	print message,

print
print "=== Delimiter = ' ', comment = '#', cast = float, skip_empty_entries = 'ends', skip_empty_lines = True ==="
try:
	pp.pprint( mypy.load_csv( 'sample2.dat', delimiter = ' ', comment = '#', cast = float, skip_empty_entries = 'ends', skip_empty_lines = True ) )
except Exception as message:
	print message,

print
print "=== Delimiter = ' ', comment = '#', cast = float, skip_empty_entries = 'all', skip_empty_lines = True ==="
try:
	pp.pprint( mypy.load_csv( 'sample2.dat', delimiter = ' ', comment = '#', cast = float, skip_empty_entries = 'all', skip_empty_lines = True ) )
except Exception as message:
	print message,

print
print "=== Delimiter = ' ', comment = '#', cast = int ==="
try:
	pp.pprint( mypy.load_csv( 'sample2.dat', delimiter = ' ', comment = '#', cast = int ) )
except Exception as message:
	print message,

print
print "=== Delimiter = ' ', comment = '#', cast = int, ignore_conversion_errors = True ==="
try:
	pp.pprint( mypy.load_csv( 'sample2.dat', delimiter = ' ', comment = '#', cast = int, ignore_conversion_errors = True ) )
except Exception as message:
	print message,

print
print "=== Delimiter = ' ', comment = '#', cast = int, ignore_conversion_errors = True, skip_empty_entries = 'all', skip_empty_lines = True ==="
try:
	pp.pprint( mypy.load_csv( 'sample2.dat', delimiter = ' ', comment = '#', cast = int, ignore_conversion_errors = True, skip_empty_entries = 'all', skip_empty_lines = True ) )
except Exception as message:
	print message,
