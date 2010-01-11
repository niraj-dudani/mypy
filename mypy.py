import csv
class ConversionError:
	pass

def load_csv( file, delimiter = ',', comment = '', skip_empty = False, type = "string" ):
	"""
	Args:
		file: Path to file that needs to be loaded.
		delimiter: Character separating fields.
		comment: Line starting with characters in this string will be skipped.
		skip_empty: Empty lines will be skipped if true.
		type: Convert data found in file to a specified type. Possible values:
			"float", "int", 
	
	Returns:
		List of lists of strings: All 'words' found in a line are clubbed
		together in a list. All such lists are then clubbed together and
		returned.
	"""
	reader = csv.reader( open( file ), delimiter = delimiter )
	data = []
	for row in reader:
		if len( row ) == 0:
			if not skip_empty:
				data.append( [] )
		elif len( row[ 0 ] ) == 0:	# If first field in a line is an empty string
			data.append( row[:] )
		elif row[ 0 ][ 0 ] not in comment:
			data.append( row[:] )
	
	#~ Not tested:
	#~ try:
		#~ if type == "float":
			#~ data = [ [ float( d ) for d in row ] for row in data ]
		#~ elif type == "int":
			#~ data = [ [ int( d ) for d in row ] for row in data ]
	#~ except ValueError as message:
		#~ print "Error loading csv file '" + file "'.",
		#~ print "Could not convert row:", len( data ) + ", col:", len( data[:-1] )
		#~ print message
		#~ raise ConversionError
	
	return data

def print_log( file, msg = "" ):
	file.write( msg + "\n" )
	print msg

import commands
def run_commands( command_list, logfile = 'run.log' ):
	with open( logfile, 'w' ) as file:
		for ( index, command ) in enumerate( command_list ):
			print_log( file,  "[Running command #" + str( index ) + "]" )
			print_log( file,  "Command: " + command )
			
			( status, output ) = commands.getstatusoutput( command )
			
			print_log( file,  "Exit status: " + str( status ) )
			print_log( file,  "Output: " + output )
			print_log( file )
			
			if status != 0:
				break
