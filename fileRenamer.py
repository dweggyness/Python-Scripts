# A script I made to rename some music files that I download. The files are prefixed with their track number and I wanted to
# remove them. ex : "01 Space Song.mp3" to "Space Song.mp3"
# This script renames every MP3 that fits the criteria in the directory it is in.


import os


def main():
	count = 0
	directory = os.path.dirname(os.path.realpath(__file__)) # get directory that this script is in
	print(directory)

	for filename in os.listdir(directory):
		if filename.lower().endswith('.mp3'): # check if its an mp3
			if len(filename) > 3: # check if its longer than 3 characters ( which we are testing )
				prefix = filename[0:3] # pull first 3 characters 

				if prefix[0:2].isdigit() and prefix[2] == " ": # check if first 3 characters follow the format we want to remove
					src = filename
					dst = filename[3:]
					os.rename(src,dst)
					count += 1

	print("%s files have been renamed." % (count))

if __name__ == '__main__':

	main()
