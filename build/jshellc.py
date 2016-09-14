"""Take a piece of Java code, 
turn it into a script to use in excpect to 
feed into jshell.

Skips over %%tutor calls,

If a public static void is detected, 
add a line to call this method with an empty input
""" 

import sys
import re

javaprog = sys.argv[1]
expectscript = javaprog + ".exp"
jshellpath = "/Library/Java/JavaVirtualMachines/jdk-9.jdk/Contents/Home/bin/jshell"

translator = str.maketrans({
    '"': r'\"',
    '{': r'\{',
    '}': r'\}',
    '[': r'\[',
    ']': r'\]',
    })

callIt = False

def construct_action(a):
    action = '\nsend "' + a + r'\r"'
    pattern1 = '\n"jshell> " ' + "{" + action + "\n}"
    pattern2 = '\n"   ...> " ' + "{" + action + "\n}"
    command = 'expect { ' + pattern1 + pattern2 + '\n}\n' 

    return command

with open(javaprog, "r") as jf:
    with open(expectscript, "w") as es:
        es.write("spawn " + jshellpath + "\n")
        for line in jf:

            if "%%tutor" in line:
                continue 

            # do we have to create a call?
            if "public static void main" in line:
                callIt = True 
            
            line = (line.rstrip()).translate(translator)
            print(line)
            
            es.write(construct_action(line))

        if callIt:
            classname = re.sub(".java", "", javaprog)
            action = (classname +
                          ".main(new String[0]);").translate(translator)
            es.write(construct_action(action))
            
        es.write(r'expect "jshell> " {send "/exit\r" }' + "\n")
        
        


