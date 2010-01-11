import subprocess

print "Starting process.."
status = subprocess.call( [ "python", "dummy-program.py" ] )
print "Process done."

print
print "[ Err ]"
print status
