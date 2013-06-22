# Originally written by andy.maach@students.fhu.edu

input_directory=$1
output_directory=$2
results_file=$3

#Divide the content!

divider="python ParagraphDivider.py"

echo $divider
echo $input_directory
echo $output_directory

mkdir "$output_directory"

for writer in `ls $input_directory`
do
  echo "Writer: $writer"
  mkdir "$output_directory/$writer"
  for doc in `ls $input_directory/$writer`
  do
    echo "$doc"
    $divider "$input_directory/$writer/$doc" "$output_directory/$writer/$doc_#.txt"
  done
done


#Parse the content!


scanner="python BasicParser.py"
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