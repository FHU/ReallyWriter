# Originally written by andy.maach@students.fhu.edu

output_directory=$1
results_file=$2


#Parse the content!
scanner="python BasicParser.py"


# Make sure the output file does not exist.
rm $results_file


touch $results_file

# The header
echo "% Title: Reallywritter" >> $results_file
echo "%" >> $results_file
echo "@RELATION text" >> $results_file
echo "" >> $results_file

# Have the scanners publish their headers here.
$scanner fields >> $results_file


# Save the different authors.
# Note: I'm being lazy and not removing that last ",". It'll have to be removed manually.
printf "@ATTRIBUTE   author		{" >> $results_file
for writer in `ls $output_directory`
do
printf "$writer, " >> $results_file
done
echo "}" >> $results_file


#Head of the data section.
echo "" >> $results_file
echo "@DATA" >> $results_file


for writer in `ls $output_directory`
do
echo "Writer: $writer"
for doc in `ls $output_directory/$writer`
do
echo $doc
$scanner "$output_directory/$writer/$doc" >> $results_file
#Other parsers can be placed here.
echo ",$writer" >> $results_file
done
done