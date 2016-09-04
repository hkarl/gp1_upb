import sys
import os
import re
import itertools

indir = sys.argv[1]
print(indir)

with open(os.path.join("..", indir, indir+".tex"), 'r') as f:
    with open(os.path.join("..", indir, "chapter.tex"), 'w') as out:
        lines = f.readlines()

        # get the title
        titleline = [x for x in lines if "title{Kapitel" in x][0]
        title = re.search("Kapitel [0-9]*: (.*?)\\\\", titleline)
        # print(title.groups()[0])
        out.write("\\chapter{{{}}}\n".format(title.groups()[0]))
        
        # and now write all the stuff after newpage
        body = itertools.dropwhile(lambda x: "newpage" not in x,
                                       lines)
        # skip over the newpage itself and the end document at the end 
        outlines = itertools.filterfalse(
            lambda x: "end{document}" in x,
            itertools.islice(body, 1, None))

        for l in outlines:
            out.write(l)


 
