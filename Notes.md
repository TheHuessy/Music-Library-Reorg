## New Notes (2021 Edition)
Going to overhaul this so it's over engineered and forces me to focus on structure and tuning


### Process Map
* Read files one by one (looping through each folder within the music directory) to create master df of origin->destination with correct id3 info
	__For each file read:__
	* Get current path (√)
	* If Song (MP3/M4A)
		* Extract Existing ID3 Tag (√)
			* Map Artist, Album, Title
			* If missing, add full path to deds object
	* If image
		* Pull containing folder name and image path to df for checking
			Want to see if the image pulled should be the album art for that album
				This will require manual checks so we'll need to output these data in a seperate df

* Post processes
	* Evaluating ded/untagged songs
		This is where you may want to try to use the lastfm API if it's still up
		[NEEDS MORE RESEARCH]

	* Evaluating album art
		Go through each file, decide yes or no
			If yes:
				Copy image file to newly created, clean music library location
			If not:
				Ignore/add to list of album art to search for


### Rough list of functions/classes/modules
#### File Wrangling
* File handling
	* Read in
		Read in all recursive files from a base directory[?]
			Generate a [the existing] dict?
			Executes the file processing functions, all wrapped up in a single function
				Something like `gather_music_library()` 
	* Write out
* ID3 tag handling
	* Pull tags from existing files
		Begin with a single file path
			Read it's id3 tag
				Evaluate if it has all the needed info
				--What about songs with incomplete song title file names?
					That shouldn't affect the id3 tag tho. Will want to look at a sample of files to make sure this assumption is accurate.

	* Write new tags to destination files
* Image handling
	* For the time being it may just be wisest to skip them/just copy them over as is to the finalized new folder location
		* Might have to put them in the output table with "album" and "artist" attributes so the new dest path can be created.

#### Path Evaluation
* Querying music lib db generated in the wrangling step, running analyses
	* Removing unexpected characters/elements ("feat. blah", etc.)
	* Checking each album to generate expected album artist
		* What to do about albums with listed feature artists vs various artists albums
			* Probs just flag/dive into anything that has a large standard deviation and anything with the word "Various" in the artist field
		* Music info API handling for missing info
			* Will also need to flag/dive into missing info lines
* Updating SQL table(s) and generating finialized set of origin/destination file paths
	


### Future Additions
* Convert/modify to utilize Spark/pyspark and see if this sort of operation would be faster on an ARM Spark cluster (2 data nodes) vs a gaming PC
	* This will probably just be a part of an after-project since getting the Spark Cluster to talk to Windows may be more trouble than I want it to be
		* Save to hadoop on cluster as backup?
	