class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        new_pages = photos_count // 4
        return cls(new_pages)

    def check_free_slots(self):
        return [p for p in self.photos if len(p) < 4]

    def add_photo(self, label):
        if not self.check_free_slots():
            return "No more free spots"

        for p_number, page in enumerate(self.photos, start=1):
            if len(page) < 4:
                page.append(label)
                n_slot = len(page)
                return f"{label} photo added successfully on page {p_number} slot {n_slot}"

    def display(self):
        photos_display = ""

        for page in self.photos:
            photos_display += f"-----------\n"
            photos = f"{'[] ' * len(page)}"
            photos_display += f"{photos[:-1]}\n"
        photos_display += f"-----------\n"
        return photos_display


# album = PhotoAlbum(2)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
#
# print(album.display())
