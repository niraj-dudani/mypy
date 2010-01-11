import subprocess

# This works well. However, according to the documentation, 
# if the program generates a lot of text, then process.wait() can
# deadlock. Replace wait() with communicate().

print "Starting process.."
process = subprocess.Popen( [ "python", "dummy-program.py" ] )
process.wait()
print "Process done."
