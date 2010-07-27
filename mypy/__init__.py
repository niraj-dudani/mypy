#~ Not required since we are explicitly importing the modules below.
#~ __all__ = [ 'analysis', 'pack' ]

import curve

import csv
import os
import os.path as path
import subprocess
import numpy

def numpy_array( a ):
	t = type( numpy.array( [ 1 ] ) )
	if a == None:
		return None
	elif type( a ) == t:
		return a
	else:
		return numpy.array( a )

#~ _iptc = None
#~ try:
	#~ from IPython.kernel import client
#~ except ImportError:
	#~ pass # _iptc = None
#~ else:
	#~ import twisted
	#~ try:
		#~ _iptc = client.TaskClient()
	#~ except twisted.internet.error.ConnectionRefusedError:
		#~ pass # _iptc = None
#~ 
#~ def pmap( f, lst ):
	#~ if _iptc:
		#~ return _iptc.map( f, lst )
	#~ else:
		#~ return map( f, lst )
#~ 
#~ def pmap( f, lst, info = False ):
	#~ if info:
		#~ def g( x ):
			#~ import time
			#~ import os
			#~ import socket
			#~ 
			#~ # host = socket.getfqdn() # Fully qualified domain name.
			#~ host = socket.gethostname()
			#~ pid = os.getpid()
			#~ cwd = os.getcwd()
			#~ 
			#~ t1 = time.strftime( "%H:%M:%S", time.localtime() )
			#~ y = f( x )
			#~ t2 = time.strftime( "%H:%M:%S", time.localtime() )
			#~ 
			#~ return ( y, ( host, pid, cwd, t1, t2 ) )
	#~ else:
		#~ g = f
	#~ 
	#~ y = _pmap( g, lst )
	#~ 
	#~ if info:
		#~ return zip( *y )
	#~ else:
		#~ return y

def movie(
	frames,
	movie_file,
	blank_frame = None,
	frame_delay = 25,
	last_frame_delay = 100,
	blank_delay = 100,
	blank_position = 0 ):
	"""
	Takes images and puts them together into a movie.
	
	Args:
		frames: Paths to image files.
		movie_file: Path to output movie file.
		blank_frame: Path to a special image file that can be inserted at any
			point of the movie. Useful for giving a title frame, or an ending
			frame.
		frame_delay: Delay between movie frames, in milliseconds.
		last_frame_delay: Delay for last frame in the movie, in milliseconds.
		blank_delay: Delay for the special frame that is put at the end or
			beginning of the movie.
		blank_position: Position of the blank frame. 0 indicates beginning of
			the movie. -1 indicates end. Other integers greater than 0 and less
			than the number of frames can be used to indicate intermediate
			positions.
	
	Notes:
		Depends on the ImageMagick "convert" tool.
	"""
	import subprocess
	tool = 'convert'
	
	try:
		subprocess.call( tool, stdout = subprocess.PIPE )
	except:
		raise OSError( "Unable to execute tool 'convert'." )
	
	if len( frames ) == 0:
		return
	
	command = frames[ : ]
	
	command.insert( 0, `frame_delay` )
	command.insert( 0, '-delay' )
	
	command.insert( -1, '-delay' )
	command.insert( -1, `last_frame_delay` )
	
	if blank_frame:
		blank_args = ( '-delay', `blank_delay`, blank_frame )
		if blank_position == -1:
			command.extend( blank_args )
		else:
			command.insert( blank_position, blank_args[ 2 ] )
			command.insert( blank_position, blank_args[ 1 ] )
			command.insert( blank_position, blank_args[ 0 ] )
	
	command.insert( 0, tool )
	command.append( movie_file )
	
	subprocess.call( command )

def require_dir( directory ):
	if path.isfile( directory ):
		raise ValueError( "'" + directory + "' is a file. Should be a directory." )
	elif not path.isdir( directory ):
		os.makedirs( directory )

class ConversionError( Exception ):
	pass

def load_csv(
	file_path, delimiter = '\t', comment = '', cast = str,
	skip_empty_lines = False, skip_empty_entries = "none",
	ignore_conversion_errors = False ):
	"""
	Args:
		file_path: Path to file that needs to be loaded.
		delimiter: Character separating fields.
		comment: Line starting with characters in this string will be skipped.
		skip_empty_lines: Empty lines will be skipped if true.
		skip_empty_entries: Possible values:
			"none": Empty entries (tokens between 2 'commas') will not be skipped
			"all": All empty entries will be skipped
			"ends": Only empty entries at the beginning and end of rows will be skipped
		cast: Convert data found in file to a specified type. Tested
			with str, float, int. For float and int, any empty entries will be
			returned as None. Raises ConversionError if any entry could not be
			cast successfully.
		ignore_conversion_errors: If True, any fields which could not be
			successfully casted will be returned as None.
	
	Notes:
		If after skipping empty entries, a line is empty then it will be
		skipped if skip_empty_lines is True. On the other hand, if the
		first entry in a line starts with a comment character only after
		skipping empty entries, then this line will not be considered as
		a comment, and will be included in the returned table.
	
	Returns:
		A 2-dimensional "array" containing a table read from the given file.
		The array is implemented as a list of lists.
	"""
	if skip_empty_entries not in ( 'none', 'ends', 'all' ):
		print "Warning: load_csv: 'skip_empty_entries' should be one of",
		print "'none', 'ends' and 'all'. Assuming 'none'."
		skip_empty_entries = 'none'
	
	with open( file_path ) as f:
		reader = csv.reader( f, delimiter = delimiter )
		
		line = 0
		data = []
		for row in reader:
			line = line + 1
			
			if len( row ) > 0 and len( row[ 0 ] ) > 0 and row[ 0 ][ 0 ] in comment:
				continue
			
			if skip_empty_entries == "ends":
				while len( row ) > 0 and row[ 0 ] == '':
					del row[ 0 ]
				while len( row ) > 0 and row[ -1 ] == '':
					del row[ -1 ]
			elif skip_empty_entries == "all":
				for i in range( len( row ) - 1, -1, -1 ):
					if row[ i ] == '':
						del row[ i ]
			
			append = True
			if len( row ) == 0:
				if skip_empty_lines:
					append = False
			#~ elif len( row[ 0 ] ) > 0 and row[ 0 ][ 0 ] in comment:
				#~ append = False
			
			if append:
				if cast != str:
					cast_row = []
					for d in row:
						try:
							cast_row.append( cast( d ) if d != '' else None )
						except ValueError as message:
							if ignore_conversion_errors:
								cast_row.append( None )
							else:
								print \
									"Error loading csv file '" + file_path + "', line " + str( line ) + ":"
								print message
								raise ConversionError
					row = cast_row
				data.append( row[ : ] )
	
	return data

def col( matrix, cols ):
	if isinstance( cols, int ):
		cols = ( cols, )
	
	return [
		[
			matrix[ i ][ j ]
			for j in cols
		]
		for i in range( len( matrix ) )
	]

def print_log( file, msg = "" ):
	file.write( msg + "\n" )
	print msg

import commands
def run_commands( command_list, log_file = 'run.log', file_mode = 'w' ):
	"""Takes and executes a list of shell commands. Prints output and
	exit status. Stores all output in a log file. Useful if using a
	python script as a shell script.
	
	For single commands, just use the subrpocess module."""
	with open( log_file, file_mode ) as file:
		for ( index, command ) in enumerate( command_list ):
			print_log( file,  "[Running command #" + str( index ) + "]" )
			print_log( file,  "Command: " + command )
			
			( status, output ) = commands.getstatusoutput( command )
			
			print_log( file,  "Exit status: " + str( status ) )
			print_log( file,  "Output: " + output )
			print_log( file )
			
			if status != 0:
				break

#~ if __name__ == "__main__":
	#~ job_size = 10 ** 7
	#~ n_jobs = 5
	#~ 
	#~ def big( size ):
		#~ import math
		#~ for i in xrange( size ):
			#~ math.sin( 1.0 )
		#~ return 1.0
	#~ 
	#~ d = pmap( big, ( job_size, ) * n_jobs, info = True )
	#~ 
	#~ print "Result:"
	#~ print d[ 0 ]
	#~ 
	#~ print
	#~ print "Info:"
	#~ for ( n, i ) in enumerate( d[ 1 ] ):
		#~ print '[', n, ']', 
		#~ for j in i:
			#~ print j,
		#~ print