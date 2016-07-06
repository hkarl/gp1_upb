= Build process for content = 

== Lectures == 


=== INput === 

  * actual content in content/ 
  * released chapters in build/released
    * one line per directory name 

=== Output === 

   
   * directory output/
   * example chapter: bla 
      * output/bla/
	  * output/bla/bla.pdf 
	  * output/bla/sources 
	     * in there, one file per tangled output 
	  * output/bla/bla.ipynb 
	     * output/bla/figures/... with all the necessary figures 
      * output/bla/bla-notebook.tgz - comprising ipynb and figures 
	
	* Copy that to: 
	   * Group directory, for easy access and offline consumption 
	   * to all the user accounts 
	      * make sure to be very fault-tolerant here!  
		 
=== Process === 

  * Has to be done on linux machine, it seems :-( 
  * 
