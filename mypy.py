import csv

class ConversionError( Exception ):
	pass

def load_csv(
	file, delimiter = '\t', comment = '', cast = str,
	skip_empty_lines = False, skip_empty_entries = "none" ):
	"""
	Args:
		file: Path to file that needs to be loaded.
		delimiter: Character separating fields.
		comment: Line starting with characters in this string will be skipped.
		skip_empty_lines: Empty lines will be skipped if true.
		skip_empty_entries: Possible values:
			"none": Empty entries (tokens between 2 'commas') will not be skipped
			"all": All empty entries will be skipped
			"ends": Only empty entries at the beginning and end of rows will be skipped
		cast: Convert data found in file to a specified type. Tested
			with str, float, int. For float and int, any empty entries
			will be returned as None. Raises ConversionError if any
			entry could not be cast successfully.
	
	Notes:
		If after skipping empty entries, a line is empty then it will be
		skipped if skip_empty_lines is True. On the other hand, if the
		first entry in a line starts with a comment character only after
		skipping empty entries, then this line will not be considered as
		a comment, and will be included in the returned table.
	
	Returns:
		List of lists of strings: All 'words' found in a line are clubbed
		together in a list. All such lists are then clubbed together and
		returned.
	"""
	reader = csv.reader( open( file ), delimiter = delimiter )
	
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
		elif skip_empty_entries != "none":
			print "Warning: load_csv: 'skip_empty_entries' should be",
			print "one of 'none', 'ends' and 'all'. Assuming 'none'."
		
		append = True
		if len( row ) == 0:
			if skip_empty_lines:
				append = False
		#~ elif len( row[ 0 ] ) > 0 and row[ 0 ][ 0 ] in comment:
			#~ append = False
		
		if append:
			if cast != str:
				try:
					row = [ cast( d ) if d != '' else None for d in row ]
				except ValueError as message:
					print \
						"Error loading csv file '" + file + "', line " + str( line ) + ":"
					print message
					raise ConversionError
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
