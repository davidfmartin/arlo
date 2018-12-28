from Arlo import Arlo
from configparser import ConfigParser, ParsingError

from datetime import timedelta, date
import datetime
import sys
from os import path

CONFIG_FILE = '/resources/arlo.ini'
ARLO_USER = ''
ARLO_PASS = ''
ARLO_VIDEOS = ''

# load config file
try:
	cwd = path.abspath(path.dirname(__file__))
	properties_file = cwd + CONFIG_FILE
	properties = ConfigParser()
	properties.read(properties_file)

	ARLO_USER = properties.get('ARLO', 'arlo.username')
	ARLO_PASS = properties.get('ARLO', 'arlo.password')
	ARLO_VIDEOS = properties.get('ARLO', 'arlo.videospath')
except ParsingError as err:
    raise RuntimeError(f"Could not parse: {err}")

try:
	# Instantiating the Arlo object automatically calls Login(), which returns an oAuth token that gets cached.
	# Subsequent successful calls to login will update the oAuth token.
	arlo = Arlo(ARLO_USER, ARLO_PASS)
	# At this point you're logged into Arlo.

	today = (date.today()-timedelta(days=0)).strftime("%Y%m%d")
	seven_days_ago = (date.today()-timedelta(days=7)).strftime("%Y%m%d")

	# Get all of the recordings for a date range.
	library = arlo.GetLibrary(seven_days_ago, today)

	# Iterate through the recordings in the library.
	matched_library = []
	for recording in library:

		videotime = datetime.datetime.fromtimestamp(int(recording['name'])//1000).strftime('%H-%M')
		#print("videotime: " + videotime)
		if videotime == '08-00' or videotime == '15-00':
			matched_library.append(recording)
			videofilename = datetime.datetime.fromtimestamp(int(recording['name'])//1000).strftime('%Y-%m-%d %H-%M-%S') + ' ' + recording['uniqueId'] + '.mp4'
			##
			# The videos produced by Arlo are pretty small, even in their longest, best quality settings,
			# but you should probably prefer the chunked stream (see below). 
			###    
			#    # Download the whole video into memory as a single chunk.
			#    video = arlo.GetRecording(recording['presignedContentUrl'])
			#	 with open('videos/'+videofilename, 'wb') as f:
			#        f.write(video)
			#        f.close()
			# Or:
			#
			# Get video as a chunked stream; this function returns a generator.
			stream = arlo.StreamRecording(recording['presignedContentUrl'])
			with open(ARLO_VIDEOS+videofilename, 'wb') as f:
			 	for chunk in stream:
			 		f.write(chunk)
			 	f.close()

			print('Downloaded video '+videofilename+' from '+recording['createdDate']+'.')

	# Delete all of the videos you just downloaded from the Arlo library.
	#result = arlo.BatchDeleteRecordings(matched_library)
	#print('Batch deletion of videos completed successfully.')

except Exception as e:
    print(e)
