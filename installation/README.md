= Notes on nbgrader formgrade =

Currently, the following seems to work:

* Start nbgrader formgrade --course-dir=notebokks/gp1 from home dir of
  jupyterhub
* Tunnel into the machine to port 5000
* This does *not* require authentication

Not working: authentication via jupyterhub. Maybe skip?

Todos:

* Better list of students?

== Print accounts ==

split -l 20 groupsaccounts.yaml
 a2ps  -f 24   x* -o pw.ps ; open pw.ps
 
 
