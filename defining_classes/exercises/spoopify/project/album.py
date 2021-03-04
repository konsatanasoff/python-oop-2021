from exercises.spoopify.project.song import Song


class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = list(songs)
        self.published: bool = False

    def add_song(self, song: Song):
        is_single = song.single

        if is_single and song not in self.songs:
            return f"Cannot add {song.name}. It's a single"

        if self.published and song not in self.songs:
            return f"Cannot add songs. Album is published."

        if song in self.songs:
            return f"Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if song_name not in [song.name for song in self.songs]:
            return "Song is not in the album."
        if self.published:
            return "Cannot remove songs. Album is published."

        song = [song for song in self.songs if song.name == song_name][0]
        self.songs.remove(song)
        return f"Removed song {song.name} from album {self.name}."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        return f"Album {self.name} is already published."

    def details(self):
        result = f"Album {self.name}\n"
        for s in self.songs:
            result += f"== {s.get_info()}\n"
        return result
