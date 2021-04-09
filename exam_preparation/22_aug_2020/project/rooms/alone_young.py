from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    room_member_count = 1
    room_cost = 10
    appliance_type = (TV,)

    def __init__(self, family_name: str, pension: float):
        super().__init__(family_name, pension, self.room_member_count)
        self.calculate_expenses(self.appliances)