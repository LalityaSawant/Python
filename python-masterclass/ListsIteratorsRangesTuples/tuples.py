# t = 'a','b','c'
# print(t)
#
# print('a','b','c')
# print(('a','b','c'))
#
# my_list = ['a',23,'what']
#
# print(my_list)

song1 = "Koi Mil gaya","Udit Narayan",1999
print(song1)

#unpacking tuple
song, artist, year = song1
print(song)
print(artist)
print(year)

songlist =["Yaroon","KK",1998]
print(songlist)
songlist.append("Rock")
print(songlist)

#erorr when used list withdifferent length
# song, artist, year = songlist
# print(song)
# print(artist)
# print(year)

imelda = "More Mayhem", "Imlda May", 2011, (
    (1,'Song1'),(2,'Song2'),(3,'song3'))

album,artist,year,tracks = imelda
print(album)
print(artist)
print(year)
for num,track in tracks:
    print(track)


