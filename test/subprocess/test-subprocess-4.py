import subprocess

# From docs:
# to get anything other than None in the result tuple, you need to give
# stdout=PIPE and/or stderr=PIPE

print "Starting process.."
process = subprocess.Popen(
	[ "python", "dummy-program.py" ],
	stdout = subprocess.PIPE, stderr = subprocess.PIPE )
( outdata, errdata ) = process.communicate()
status = process.returncode
print "Process done."

print
print "[ Out ]"
print outdata

print
print "[ Err ]"
print errdata

print
print "[ Err ]"
print status
