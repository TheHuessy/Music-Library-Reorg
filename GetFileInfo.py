#File loading (Origin dir -> pull and clean -> data out to pg)
import ID3Handler
from SQLEngine import SQLEngine
#import SQLUtils # May not need this since we're really just writing to sql at this point
import os
import pandas as pd


## Read target dir
	## How is target supplied?
output_dict = pd.DataFrame(columns=[
	'dir_path',
	'file_name',
	'full_path',
	'tag_artist',
	'tag_album',
	'tag_album_clean',
	'tag_title',
	'tag_title_clean'
	])

def read_library(library_target):
	#Just loop through each file, passing each song file into `ID3Handler::get_mp3_info`
	# If file type is not MP3, then print what it is so we can build id3 handlers for it (I think  it's just mp4)

	global output_dict

	for (dirpath, dirnames, filenames) in os.walk(library_target):
		if filenames:
			for file in filenames:
				origin_filepath = os.path.join(dirpath, file)

				## MP3 HANDLING
				if file.endswith(".mp3") or file.endswith(".MP3"):
					print(file)
					try:
						song_data = ID3Handler.get_mp3_info(origin_filepath)
					except Exception as err:
						print("Failed to get ID3 info from {}".format(file))
						continue
					else:
						new_row = pd.DataFrame({
							"dir_path": [dirpath],
							"file_name": [file],
							"full_path": [origin_filepath],
							"tag_artist": [song_data['artist']],
							"tag_album": [song_data['album']],
							"tag_album_clean": [song_data['cleaned_album']],
							"tag_title": [song_data['title']],
							"tag_title_clean": [song_data['cleaned_title']]
							})

						output_dict = output_dict.append(new_row)
				else:
					print("Not an MP3: {}".format(file))
					## add handler logic here for non-mp3 files we can get data from

## Write everything out to postgres
def write_to_sql():
	global output_dict

	try:
		with SQLEngine() as sql_engine:
			output_dict.to_sql(
				name="music_lib_origin",
				con=sql_engine,
				if_exists='replace',
				index=False
				)
	except Exception as err:
		print("Was not able to write output to sql!\n{}".format(err))

def pull_info(library_target):
	print("Starting Library Pull...")
	read_library(library_target)
	print("Writing to Postgres...")
	write_to_sql()
	print("Finished!")




