import InvertedIndex

inverted_index_buffer = InvertedIndex.Index()


## This is test input ( removed once the file read function is written )
inverted_index_buffer.index('1', 'Dog, Cat')
inverted_index_buffer.index('2', 'Water, Lake, River')
inverted_index_buffer.index('3', 'Sand, Dessert, Human')
inverted_index_buffer.index('4', 'Celebration, New Years, Party')

##To do: Input function to read all files in a folder and store tags to send to search

inverted_index_buffer.print()
