#========
# Curve characteristics
#========
import numpy
from scipy import integrate
# Doesn't work for some reason:
# from . import numpy_array
# from mypy import numpy_array
import mypy

def clip( y, x = None, x_min = None, x_max = None ):
	if x == None:
		return ( y, x )
	
	if len( y ) == 0:
		raise ValueError( "'y' is empty." )
	
	if x != None and len( y ) != len( x ):
		raise ValueError( "'y' and 'x' are not of the same length." )
	
	y = mypy.numpy_array( y )
	x = mypy.numpy_array( x )
	
	if x_min != None:
		y = y[ x >= x_min ]
		x = x[ x >= x_min ]
	
	if x_max != None and len( y ) > 0:
		y = y[ x <= x_max ]
		x = x[ x <= x_max ]
	
	return ( y, x )

def amp( y, x = None, x_min = None, x_max = None, subtractBaseline = False, peak_index = False ):
	y = mypy.numpy_array( y )
	x = mypy.numpy_array( x )
	
	( yl, xl ) = clip( y, x, x_min = x_min )
	if peak_index:
		index_shift = len( y ) - len( yl )
	( y, x ) = clip( yl, xl, x_max = x_max )
	
	amp = max( y )
	
	if subtractBaseline:
		amp = amp - y[ 0 ]
	
	if peak_index:
		peak_i = numpy.argmax( y ) + index_shift
		return ( amp, peak_i )
	else:
		return amp

def area( y, x = None, x_min = None, x_max = None, subtractBaseline = False, rule = 'trapezoid' ):
	y = mypy.numpy_array( y )
	x = mypy.numpy_array( x )
	
	if rule == 'trapezoid':
		f = integrate.trapz
	elif rule == 'simpsons':
		f = integrate.simps
	elif rule == 'rectangle':
		raise Exception( 'Rectangle method not yet implemented' )
	
	( y, x ) = clip( y, x, x_min, x_max )
	
	if subtractBaseline:
		y = y - y[ 0 ]
	
	if x == None:
		return f( y )
	else:
		return f( y, x )

def _test():
	print \
	'''
	6 |                          o      
	5 |                                 
	4 |      o                          
	3 |                                 
	2 |                o                
	1 | o                               
	0 |           o         o         o 
	  L__________________________________
	   0.1  0.2  0.3  0.4  0.5  0.6  0.7
	'''
	
	x = numpy.linspace( 0.1, 0.7, 7 )
	y = ( 1, 4, 0, 2, 0, 6, 0 )
	
	print '------------------------------------------------------------'
	print '( peak, peak_index ) = amp( y, peak_index = True )'
	print 'ar = area( y )'
	print '------------------------------------------------------------'
	( peak, peak_index ) = amp( y, peak_index = True )
	ar = area( y )
	print "peak:", peak
	print "peak index:", peak_index
	print "area:", ar
	print
	
	print '------------------------------------------------------------'
	print '( peak, peak_index ) = amp( y, x, peak_index = True )'
	print 'ar = area( y, x )'
	print '------------------------------------------------------------'
	( peak, peak_index ) = amp( y, x, peak_index = True )
	ar = area( y, x )
	print "peak:", peak
	print "peak index:", peak_index
	print "x at peak:", x[ peak_index ]
	print "area:", ar
	print
	
	print '------------------------------------------------------------'
	print '( peak, peak_index ) = amp( y, x, x_max = 0.3, peak_index = True )'
	print 'ar = area( y, x, x_max = 0.3 )'
	print '------------------------------------------------------------'
	( peak, peak_index ) = amp( y, x, x_max = 0.3, peak_index = True )
	ar = area( y, x, x_max = 0.3 )
	print "peak:", peak
	print "peak index:", peak_index
	print "x at peak:", x[ peak_index ]
	print "area:", ar
	print
	
	print '------------------------------------------------------------'
	print '( peak, peak_index ) = amp( y, x, x_min = 0.3, peak_index = True )'
	print 'ar = area( y, x, x_min = 0.3 )'
	print '------------------------------------------------------------'
	( peak, peak_index ) = amp( y, x, x_min = 0.3, peak_index = True )
	ar = area( y, x, x_min = 0.3 )
	print "peak:", peak
	print "peak index:", peak_index
	print "x at peak:", x[ peak_index ]
	print "area:", ar
	print
	
	print '------------------------------------------------------------'
	print '( peak, peak_index ) = amp( y, x, x_min = 0.2, x_max = 0.6, peak_index = True )'
	print 'ar = area( y, x, x_min = 0.2, x_max = 0.6 )'
	print '------------------------------------------------------------'
	( peak, peak_index ) = amp( y, x, x_min = 0.2, x_max = 0.6, peak_index = True )
	ar = area( y, x, x_min = 0.2, x_max = 0.6 )
	print "peak:", peak
	print "peak index:", peak_index
	print "x at peak:", x[ peak_index ]
	print "area:", ar
	print
	
	print '------------------------------------------------------------'
	print '( peak, peak_index ) = amp( y, x, x_min = 0.2, x_max = 0.6, subtractBaseline = True, peak_index = True )'
	print 'ar = area( y, x, x_min = 0.2, x_max = 0.6, subtractBaseline = True )'
	print '------------------------------------------------------------'
	( peak, peak_index ) = amp( y, x, x_min = 0.2, x_max = 0.6, subtractBaseline = True, peak_index = True )
	ar = area( y, x, x_min = 0.2, x_max = 0.6, subtractBaseline = True )
	print "peak:", peak
	print "peak index:", peak_index
	print "x at peak:", x[ peak_index ]
	print "area:", ar
	print
	
	print '------------------------------------------------------------'
	print '( peak, peak_index ) = amp( y, x_min = 0.2, x_max = 0.6, subtractBaseline = True, peak_index = True )'
	print 'ar = area( y, x_min = 0.2, x_max = 0.6, subtractBaseline = True )'
	print '------------------------------------------------------------'
	( peak, peak_index ) = amp( y, x_min = 0.2, x_max = 0.6, subtractBaseline = True, peak_index = True )
	ar = area( y, x_min = 0.2, x_max = 0.6, subtractBaseline = True )
	print "peak:", peak
	print "peak index:", peak_index
	print "x at peak:", x[ peak_index ]
	print "area:", ar
	print

if __name__ == '__main__':
	_test()
