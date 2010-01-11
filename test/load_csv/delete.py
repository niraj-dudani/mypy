row = [ '', '', 'd', '', '' ]
for i in range( len( row ) - 1, -1, -1 ):
	if row[ i ] == '':
		del row[ i ]
print row
