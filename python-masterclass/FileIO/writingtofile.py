cities = ["Mumbai", "Banglore", "Chennai", "Delhi"]

with open("cities.txt","w") as city_file:
    for city in cities:
        print(city, file=city_file)
        # print(city, file=city_file, flush=True) # for fast writing without buffering

cities = []

with open("cities.txt",'r') as city_file:
    for city in city_file:
        cities.append(city.strip('\n'))

    print(cities)
    print('-' * 40)
    for city in cities:
        print(city)

songAlbum = "DilSe","A R Reheman", "1997", ((1,"Dilse Re"),(2,"Jiya Jale"))

with open("dilse.txt",'w') as song_album:
    print(songAlbum, file=song_album)

with open("dilse.txt",'r') as song_album:
    content = song_album.readline()

    song = eval(content)
    print(song)
    title, artist, year, tracks = song
    print(title)
    print(artist)
    print(year)
    for song in tracks:
        print(song)


