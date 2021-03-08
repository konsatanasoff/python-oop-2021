class PhotoAlbum:
    def __init__(self, pages):
        pass

    def from_photo_count(self, photos_count):
        pass

    def add_photo(self, label):
        pass

    def display(self):
        pass



album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
