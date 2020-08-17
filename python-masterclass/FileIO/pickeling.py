import pickle

song_album = ('Dil Se',
              'A.R.Reheman',
              '1997',
              ((1, 'Dil se'),
               (2, 'Chayya Chayya')))

with open('songsalbum.pickle', 'wb') as pickle_file:
    pickle.dump(song_album, pickle_file)

with open('songsalbum.pickle', 'rb') as album_file:
    album = pickle.load(album_file)


album_name, artist, year, song_list = album
print(album_name)
print(artist)
print(year)
#print(song_list)

for track_num,song in song_list:
    print('{}. {}'.format(track_num,song))
