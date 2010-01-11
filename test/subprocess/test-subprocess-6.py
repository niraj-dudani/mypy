import sys
import subprocess

class tee:
	def __init__( self, stream, filename, mode = 'w' ):
		self.stream = stream
		self.file = open( filename, mode )
	def fileno( self ):
		return self.stream2.fileno()
	def write( self, x ):
		self.stream1.write( x )
		self.stream2.write( x )

#~ class tee:
	#~ def __init__( self, stream1, stream2 ):
		#~ self.stream1 = stream1
		#~ self.stream2 = stream2
	#~ def fileno( self ):
		#~ return self.stream2.fileno()
	#~ def write( self, x ):
		#~ self.stream1.write( x )
		#~ self.stream2.write( x )

#~ w = sys.stdout.write
#~ def nw( x ):
	#~ with open( 'file.out', 'w' ) as file:
		#~ file.write( x )
	#~ w( x )
#~ sys.stdout.write = nw

outfile = open( 'file.out', 'w' )
errfile = open( 'file.err', 'w' )
myout = tee( sys.stdout, outfile )
myerr = tee( sys.stderr, errfile )

print "Starting process.."
process = subprocess.Popen(
	[ "python", "dummy-program.py" ],
	stdout = myout, stderr = myerr )
process.communicate()
status = process.returncode
print "Process done."

print
print "[ Err ]"
print status
