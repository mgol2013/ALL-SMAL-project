# You need to install tidalapi using pip install tidalapi (more can be found here https://github.com/tamland/python-tidal)
# Input is UTF-8 CSV file with format Artist - Album
# Fill in your username and password on line 13 -> session.login('username', 'password') 
# Fill in filename of your CSV file on line 16 -> with open('file.csv', encoding="utf8") as csvfile:

import csv
import sys
import pprint

import tidalapi

session = tidalapi.Session()
session.login('t.kostkan@volny.cz', '1Domek')
favorites = tidalapi.Favorites(session, session.user.id)

with open('file.csv', encoding="utf8") as csvfile:
	rows = csv.reader(csvfile)
	for artist, album in rows:
		print('Processing {} - {}\n'.format(artist, album))
		
		albums_data = session.search('album', '{} - {}'.format(artist, album)).albums

		if len(albums_data) == 0:
			print('WARNING: No albums found for {} - {}, continuing'.format(artist, album))
			continue

		selection = 0

		album_to_add = albums_data[selection]
		favorites.add_album(album_to_add.id)

		print('\n{}\n'.format('*' * 20))
