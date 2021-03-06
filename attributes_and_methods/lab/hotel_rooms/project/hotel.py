from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @staticmethod
    def find_room(rooms, room_number):
        return list(filter(lambda r: r.number == room_number, rooms))[0]

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room_number):
        self.rooms.append(room_number)

    def take_room(self, room_number, people):
        result = self.find_room(self.rooms, room_number).take_room(people)

        if result:
            return result
        self.guests += people

    def free_room(self, room_number):
        room = self.find_room(self.rooms, room_number)
        to_remove = room.guests
        result = room.free_room()

        if result:
            return result
        self.guests -= to_remove

    def print_status(self):
        n_free_rooms = [str(r) for r in self.rooms if not r.is_taken]
        n_taken_rooms = [str(r) for r in self.rooms if r.is_taken]
        print(f"Hotel {self.name} has {self.guests} total guests")
        print(f"Free rooms: {', '.join(n_free_rooms)}")
        print(f"Taken rooms: {', '.join(n_taken_rooms)}")


# hotel = Hotel.from_stars(5)
#
# first_room = Room(1, 3)
# second_room = Room(2, 2)
# third_room = Room(3, 1)
#
# hotel.add_room(first_room)
# hotel.add_room(second_room)
# hotel.add_room(third_room)
#
# hotel.take_room(1, 4)
# hotel.take_room(1, 2)
# hotel.take_room(3, 1)
# hotel.take_room(3, 1)
#
# hotel.print_status()