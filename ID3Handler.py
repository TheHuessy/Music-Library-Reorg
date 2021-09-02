## ID3 Tag handling

import eyed3 as id3
import re
#from mutagen.mp4 import MP4


album_regex = '\(|\)|".*"'
title_regex = "\(|\)|[P|p]rod\..*|[F|f]eat\..*|"

#Pull info from song file
def get_mp3_info(path):
    global album_regex
    global title_regex
    tag_info = id3.load(path).tag
    artist = tag_info.artist if tag_info.artist else None
    album = tag_info.album if tag_info.album else None
    cleaned_album = re.sub(pattern=album_regex, repl="", string=tag_info.album).strip()
    song_title = tag_info.title if tag_info.title else None
    cleaned_song_title = re.sub(pattern=title_regex, repl="", string=tag_info.title).strip()

    data = {"artist": artist, 
    "album": album, 
    "title": song_title, 
    "cleaned_album": cleaned_album, 
    "cleaned_title": cleaned_song_title
    }

    return(data)

# That ^ but for mp4/m4u



