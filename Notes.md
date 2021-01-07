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
* File handling
	* Read in
	* Write out
* ID3 tag handling
	* Pull tags from existing files
	* Write new tags to destination files
* Image handling
* Music info API handling


	