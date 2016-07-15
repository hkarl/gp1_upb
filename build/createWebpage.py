"""Create the webpage for all the released lectures

Takes three arguments:

- Path to where to find the chapter directories 
- Path to the file containing the released chapters
- Path to file in the output/vorlesung directory, in which the output should be created

TODO: switch to jinja templates 

"""

import argparse
import os
import yaml
import codecs
import time
import locale

def get_released_chapters(releasedFile):
    with open(releasedFile, 'r') as f:
        released = yaml.load(f)

    return released['released']

def get_content(orgpath, released, output):
    res = []
    for c in released:
        entry = {}
        # get the title 
        with open(os.path.join(orgpath,
                               c,
                               c + ".org"), 'r') as f:
            for line in f:
                    if line.startswith('#+TITLE:'):
                            entry['title']=line[9:]
                            break

        entry['notebook'] = os.path.join(c, c+".ipynb")
        entry['date'] = time.strftime(
            "%A, %Y-%m-%d, %H:%M", 
            time.localtime(os.path.getctime(os.path.join(c, c+".ipynb"))))
        entry['pdf'] = os.path.join(c, c+".pdf")
        entry['tgz'] = os.path.join(c, c+".tgz")

        # is there an audio file already in output?
        # TODO: adapt this depending on the recording tool we will use... 
        if os.path.isfile(os.path.join(c, c+".audio")):
            entry['audio'] = os.path.join(c, c+".audio")
        else:
            entry['audio'] = ""
        
        res.append(entry)
    return res


def format_entry(entry):
    return """
<li> <b> {} </b>
<br>
Version: {}
<ul>
<li><a href="{}">Notebook</a></li>
<li><a href="{}">PDF</a></li>
<li><a href="{}">TGZ</a></li>
<li><a href="{}">Audio-Mitschnitt</a></li>
</ul>
</li>

""".format(entry['title'], entry['date'],
           entry['notebook'], entry['pdf'], entry['tgz'], entry['audio'])

def format_page(entries):
    body = ""
    for e in entries:
        body += format_entry(e)

    # TODO: add uebungen! 

    html = ("<html><body><title>GP1 </title> <h1>GP1 </h1>\n<h2> Vorlesung </h2>\n<ul>"
        + body + "</ul></body></html>")
    return html

#################

locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')


parser = argparse.ArgumentParser(description="Create a web page to point to all released chapters")
parser.add_argument('--org', required=True, help="Path where to find the chapter directories")
parser.add_argument('--released', required=True, help="Which chapters are released?")
parser.add_argument('--html', '-o', required=True, help="Where to put output?")

args = parser.parse_args()

released = get_released_chapters(args.released)

entries = get_content(args.org, released, args.html)
html = format_page(entries)

with codecs.open(args.html, 'w', 'utf-8') as f:
    f.write(html)

