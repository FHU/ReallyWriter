ReallyWriter
============

A machine learning system for analyzing text

---------

This repository contains the scripts that convert folders of documents into properties in bulk quantities which can then be given to Weka to learn.

Paragraph Divider takes a Project Gutenberg book and converts it to many small files. Each of these files represents one paragraph. ASSUME THIS ONLY WORKS WITH PROJECT GUTENBERG E-BOOKS. Of course, you can modify it to work with anything. The first argument should be the source file. The second should be the desired destination file format. Use the # symbol to represent the number of the paragraph. Note that not every paragraph will be exported.

Basic Parser takes a simple text document (I assume UTF-8) and prints out the number of letters per word, vowels per letter, and words per sentence. Its only argument is simply the file to be processed.

bulk-divider.sh takes a directory of documents, organized in sub-directories by author, and divides them all up by paragraph using the Paragraph divider python script. It takes two arguments: the first is the directory from which to find the documents, the second is an empty directory to which to put the divided paragraphs.

bulk-parser.sh can produce a .arff file from the directory that bulk-divider creates. The first argument is the directory of divided paragraphs, the second is the arff file. Note that the trailing "," will have to be removed from the list of authors in the arff file in order to be valid. Maybe someday I'll fix this…but that day is not today.

------

Link to Weka:
http://www.cs.waikato.ac.nz/ml/weka/

Link to Project Gutenberg:
http://www.gutenberg.org/ebooks/search/