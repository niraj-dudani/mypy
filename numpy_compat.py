is_numpy = 1
try:
	import numpy
except ImportError:
	is_numpy = 0

def new_array():
	if not is_numpy:
		return []
	else:
		return numpy.array( [] )

def append( mat, row ):
	if not is_numpy:
		mat.append( row )
	else:
		mat.resize( mat.shape[ 0 ] + 1 )
		mat[ -1 ] = numpy.array( row )
