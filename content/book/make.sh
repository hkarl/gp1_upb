# get the list of chapters
export chapters=`grep -e "- " ../released.yaml  | cut -d " " -f 4`
echo $chapters

# build the graphicspath
echo -n "\graphicspath{" > graphicspath
for c in $chapters ; do echo -n "{../$c/}" >> graphicspath ; done 
echo "}" >> graphicspath 

# build the chapters include commands
echo "% chapter" > chapters
for c in $chapters ; do echo  "\input{../$c/chapter}" >> chapters ; done
echo "% done chapter" >> chapters

# and create the chapter tex files as such

for c in $chapters ; do python makechapters.py $c ; done



# run pdf
pdflatex -shell-escape book
pdflatex -shell-escape book
pdflatex -shell-escape book

cp book.pdf ../../output/vorlesung
