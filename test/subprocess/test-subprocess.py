import subProcess

print "Starting process.."
process = subProcess.subProcess( "python dummy-program.py" )
process.read()
print "Process done."

print
print "[ Out ]"
print process.outdata

print
print "[ Err ]"
print process.errdata
