word = list ( "abcccdefghijklllle" )
if not word:
    quit ( )

output = [ ]
i = 0
j = 1
while i < len ( word ) and j < len ( word ):

    if word [ i ] == word [ j ]:
        j = j + 1
    else:
        output.append ( word [ i ] )
        i = j
        j = j + 1

# last character
output.append ( word [ len ( word ) - 1 ] )

print( "len: ", len ( word ) )
print( "in: ", word )
print( "out:", output )
