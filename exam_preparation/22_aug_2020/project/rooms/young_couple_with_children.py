from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    room_member_count = 2
    room_cost = 30
    appliance_type = (TV, Laptop, Fridge)

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        members_count = self.room_member_count + len(children)
        super().__init__(family_name, salary_one + salary_two, members_count)
        self.children = list(children)
        self.calculate_expenses(self.appliances, self.children)
