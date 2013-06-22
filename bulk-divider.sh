# Originally written by andy.maach@students.fhu.edu

input_directory=$1
output_directory=$2

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

