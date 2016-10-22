.PHONY: distribute pueoutput puealloutput hueoutput huealloutput puerelease

# GP1SERVERDIR := jupyterhub@gp1test.cs.upb.de:output
GP1SERVERDIR := jupyterhub@gp1.cs.upb.de:uebungen

# use this to ssh in a root
ACCOUNTDIRBASE := root@gp1test.cs.upb.de:/home

# Webserverdir: this depends on where you mount the group directory 
WEBSERVERDIR := /Volumes/groups/fg-karl/public/http/lehre/ws1617/gp1


pueoutput:
	git pull
	# source ~/.venvs/jupyter/bin/activate; cd pue/$(ch) ; jupyter nbconvert *.ipynb
	cd pue/$(ch) ; if [ -x ~/anaconda3/bin/jupyter ] ; then  ~/anaconda3/bin/jupyter nbconvert *.ipynb ; else  source ~/.venvs/jupyter/bin/activate; cd pue/$(ch) ; jupyter nbconvert *.ipynb --to pdf ; fi 
	# cd pue/$(ch) ; ~/anaconda3/bin/jupyter nbconvert *.ipynb
	# source ~/.venvs/jupyter/bin/activate; 	cd pue/$(ch) ; jupyter nbconvert *.ipynb --to pdf
	# cd pue/$(ch) ; ~/anaconda3/bin/jupyter nbconvert *.ipynb --to pdf

# puealloutput:
# 	for d in pue/p* ; do make pueoutput ch=`basename $$d` ; done 

hueoutput:
	echo "this needs to be called make hueoutput ch=bla"
	git pull
	source ~/.venvs/jupyter/bin/activate; cd hue/$(ch) ; jupyter nbconvert *.ipynb
	source ~/.venvs/jupyter/bin/activate; cd hue/$(ch) ; jupyter nbconvert *.ipynb --to pdf

# huealloutput:
# 	for d in hue/h* ; do make hueoutput ch=`basename $$d` ; done 

# alloutput: huealloutput puealloutput

distribute:
	rsync -vah --exclude "notes" --exclude Makefile ../uebungen/ ${WEBSERVERDIR}
	rsync -vazh --exclude "notes" --exclude Makefile ../uebungen/ ${GP1SERVERDIR}

puerelease: 
	make pueoutput ch=$(ch)
	sed -i"" -e "s/<\\!-- $(ch)/<\\!-- $(ch) -->/" pue/index.html
	sed -i"" -e "s/^ *$(ch) -->/  <\\!-- $(ch) -->/" pue/index.html
	make distribute
	ssh root@gp1.cs.upb.de "python3.4 /home/jupyterhub/bin/copy-file-to-user.py -a  -s /home/jupyterhub/uebungen/pue/ -t pue -c $(ch) -x .ipynb -x .html -x .pdf -d figures"

huerelease:
	make hueoutput ch=$(ch)
	sed -i"" -e "s/<\\!-- $(ch)/<\\!-- $(ch) -->/" pue/index.html
	sed -i"" -e "s/^ *$(ch) -->/  <\\!-- $(ch) -->/" pue/index.html
	make distribute
	echo "Remember to trigger nbgrader!" 

