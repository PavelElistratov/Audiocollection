class Track:
    def __init__(self, name='Unnamed', time=0):
        self.name = name
        self.time = int(time)

    def show(self): # метод, выводящий информацию по треку в виде <Название-Длительность>
        print(f'{self.name}-{self.time}')


class Album:
    def __init__(self, album_name='Unnamed album', band='No band'):
        self.album_name = album_name
        self.band = band
        self.tracks = [] # Пустой список треков при создании объекта

    def add_track(self, track):  # добавление нового трека в список треков
        self.tracks.append(track) # добавление (стандартный метод .append) объекта track в список self.tracks

    def get_tracks(self):   # выводит информацию по всем трекам (используется метод show)
        for track in self.tracks:
            track.show()

    def get_duration(self):  # выводит длительность всего альбома
        total = 0
        for track in self.tracks:
            total += track.time
        print(f'Общая длительность альбома {self.album_name} {total} мин')


track_1 = Track('Калинка', 5)
# track_1.show()

track_2 = Track('Малинка', 7)
track_3 = Track('Березка', 3)

folk_album = Album('Народные песни', 'Хор Турецкого')
# print(folk_album.album_name, folk_album.band)

folk_album.add_track(track_1)
folk_album.add_track(track_2)
folk_album.add_track(track_3)
# print(folk_album.tracks)
folk_album.get_tracks()


ram_1 = Track('Mein Herz brennt', 5)
ram_2 = Track('Sonne', 4)
ram_3 = Track('Ich will', 3)
ram_4 = Track('Mutter', 4)

mutter = Album('Mutter', 'Rammstein')

mutter.add_track(ram_1)
mutter.add_track(ram_2)
mutter.add_track(ram_3)
mutter.add_track(ram_4)

mutter.get_tracks()
mutter.get_duration()
