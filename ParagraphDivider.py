'''
Created on Jun 17, 2013

@author: andy.maach@students.fhu.edu
'''

import sys

if len(sys.argv) < 3:
    print "Usage:"
    print "ParagraphDivider.py input output"
    print "When exporting paragraphs, use # to represent where the paragraph index should go."
    print "For example: 'paragraph#.txt' will become 'paragraph100.txt' for the 100th paragraph. "


# Get the input and output locations.
source = sys.argv[1]
output =  sys.argv[2]

#Open the input
f = open(source, 'r')

# This keeps track of what the paragraph number is.
paragraph_number = 0

# Book content starts with several *s. This variable
# keeps track whether or not the beginning of the content
# has been found.
is_content = False

# Variables used to decide whether or not each line is content or a chapter header,
# or something else.
prior_length = 0
is_writing = False
prior = "ERROR"

# The buffer for the 
data = ""

# This function simply writes the buffer to a new file.
def flush_to_file(d, pn):
    if len(d) < 100: return
    m = output.replace('#', str(pn))
    out = open(m, 'w')
    out.write(d)

for line in f:
    text = line.strip()
    
    # First, consider enabling or disabling the parser
    # if the stars are found.
    if "***" in text:
        if not is_content: is_content = True
        else: break
        
    # Paragraphs are divided by empty lines.
    #This first condition finds the first line, and enables writing.
    if is_content and len(text) > 0 and prior_length == 0:
        paragraph_number += 1
        is_writing = True
        
    #if an initial empty line has been found add the content from this line
    # to the buffer.
    elif is_content and prior_length > 0 and is_writing:
        data += prior + " "

    
    # 
    if is_writing and len(text) == 0:
        flush_to_file(data, paragraph_number)
        data = ""
        is_writing = False
        
    prior = text
    prior_length = len(text)

f.close()
