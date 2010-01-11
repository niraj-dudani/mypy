import subprocess

print "Starting process.."
process = subprocess.Popen( [ "python", "dummy-program.py" ] )
process.communicate()
print "Process done."
