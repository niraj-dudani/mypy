import subProcess

# Need to flush the programs streams to receive data while the program
# is running.

print "Starting process.."
process = subProcess.subProcess( "python dummy-program.py" )
while( process.read( 0.1 ) ):
	print "tick!"
	print process.outchunk
print "Process done."

print
print "[ Out ]"
print process.outdata

print
print "[ Err ]"
print process.errdata
