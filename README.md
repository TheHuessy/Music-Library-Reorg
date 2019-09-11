# Music-Library-Reorg
Apple has no idea how to make an intuitive file structure. I need to reorganize about 128GB of music into a more logical file structure and I'm choosing to do this with Python on a Linux Machine


## The Problem (Backstory)
A long long time ago, I was burgled and the thief took off with my laptop which had all of my music on it. These were files stored in a music folder, organized by artist as the primary filed and then album and then all songs in that album. I was able to retrieve my whole library by copying my iPod classic to another PC, but the resulting files (after they had been decoded to not read as `YFGW.mp3`), the file structure had changed to what I assume is iTunes' standard format.

It's a garbage format. I mean, it's just so dumb. 

Instead of organizing things from the artist down, iTunes organizes things from song up, so to speak. I'll use Ghostface Killah's album 'More Fish' as an example. The way I had the files stored, there would be a Ghostface Killah folder, then all of his albums I had of his, then the songs in them. For the track 'You Know I'm No Good', which features Amy Winehouse, would look like:

`~/Music/Ghostface Killah/More Fish/You Know I'm No Good feat. Amy Winehouse.mp3`

and the rest of the album would be in there and the directory paths would look something like:

`~/Music/Ghostface Killah/More Fish/Back Like That (Remix) feat Kanye West & Ne-Y.mp3`
`~/Music/Ghostface Killah/More Fish/Street Opera feat Sun-God.mp3`
`~/Music/Ghostface Killah/More Fish/Guns N' Razors (Feat. Trife Da God, Cappadonna & Killa Sin).mp3`
`etc.`
`etc.`

However, when iTunes got its little mits on these songs and went out to their libraray db to, I assume, verify id3 tags or verify legality (lol), it would reorganize everything so that I ended up the messiest file structure. The resulting directory paths of the same songs would now look like:


`/Music/Ghostface Killah & Amy Winehouse/More Fish/You Know I'm No Good feat. Amy Winehouse.mp3`
`~/Music/Ghostface Killah Feat. Kanye West & Ne-Y/More Fish/Back Like That (Remix) feat Kanye West & Ne-Y.mp3`
`~/Music/Ghostface Killah Feat. Sun God/More Fish/Street Opera feat Sun-God.mp3`
`~/Music/Ghostface Killah Feat. Trife Da God, Cappadonna & Killa Sin/More Fish/Guns N' Razors (Feat. Trife Da God, Cappadonna & Killa Sin).mp3`
`etc.`
`etc.`

This is not a problem if you're on iTunes on your computer or use an iPhone that forces you to use iTunes. There are some of us, however, that aren't so beholden to Apple's products and like to listen to music files on an SD card in their phone. I use VLC, which has its own limits, but when I try to pick out something to listen to, I can't just go to Ghostface Killah's folder and peruse albums because I will only get songs where Ghostface is the sole artist. 

If I want to listen to More Fish in its entirety, I'd have to hunt each song down by all artists involved in the song and create a playlist on the go. By the time I've finished this, I'm either 20 mins late to where ever I was going, or I just got hit by a bus because I was walking and creating a playlist and not paying attention. This is a problem!

## The Solution (A Solution)

I'm lazy, I don't want to go through manually and move folders around all night, especially with 128GB of music. What is the secret solution to any lazy person's tech problems? Write a script to do it for you!

## The Plan

Write a python script that executes the following steps:
* Read evey file in the targeted music directory recursively
* Use the `eyeD3` module to read the id3 tags of each song and extract:
    * Artist
    * Album
* Use this info to generate a new directory path based on that info
* Have a secondary directory (`Cleaned Files` for instance) where I check whether the new directory path exists, create it if it doesn't, and copy the file over
* Repeat in loop as needed until it's done

## Anticipated Problems

This isn't a perfect solution, but it is, as far as I can tell, the fastest. I'm essentially backing up my music library and shuffling it around to suit my (not stupidly engineered) needs. 

### Missing id3 Tags

By running a quick test on a few Ghostface folders, I've found that some files simply don't have id3 tags, though some of their neighbors do. My current approach is going to be to isolate the files that can't be parsed into a new directory path and either enter the data manually (let's hope not) or figure out why some do and don't have id3 tags.

### Time

I'm going through a ton of files. At first I tried to copy the files over to my Linux machine via USB (2.0) which would have taken 30 hours. I will attempt to move them to my home server with a USB 3.0 cable and see if that makes a difference. The other plan is to eject the SD card and try to check transfer speeds of built in SD card readers. 

Best Case scenario, I can find all the various music libraries on my home server and won't have to transfer anything until the files have been reorganized.
