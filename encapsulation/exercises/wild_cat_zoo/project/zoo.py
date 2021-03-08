class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    @staticmethod
    def all_workers_salary(all_workers):
        total_salary = 0
        for worker in all_workers:
            total_salary += worker.salary
        return total_salary

    def check_if_enough_budget(self, price):
        return self.__budget >= price

    @staticmethod
    def check_if_enough_space(capacity_limit, item_count):
        return capacity_limit > len(item_count)

    def add_animal(self, animal, price):
        if not self.check_if_enough_budget(price):
            return "Not enough budget"
        if not self.check_if_enough_space(self.__animal_capacity, self.animals):
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if not self.check_if_enough_space(self.__workers_capacity, self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        workers = [w for w in self.workers if w.name == worker_name]
        if not workers:
            return f"There is no {worker_name} in the zoo"
        worker = workers[0]
        self.workers.remove(worker)
        return f"{worker.name} fired successfully"

    def pay_workers(self):
        total_salary = self.all_workers_salary(self.workers)
        if not self.__budget >= total_salary:
            return "You have no budget to pay your workers. They are unhappy"
        left_budget = self.__budget - total_salary
        self.__budget -= total_salary
        return f"You payed your workers. They are happy. Budget left: {left_budget}"

    def get_animal_needs(self):
        return sum([a.get_needs() for a in self.animals])

    def tend_animals(self):
        total_needs = self.get_animal_needs()
        if not self.check_if_enough_budget(total_needs):
            return "You have no budget to tend the animals. They are unhappy."
        left_budget = self.__budget - total_needs
        self.__budget -= total_needs
        return f"You tended all the animals. They are happy. Budget left: {left_budget}"

    def profit(self, amount):
        self.__budget += amount

    def get_type(self, location, type_name: str):
        return [str(el) for el in location if el.__class__.__name__ == type_name]

    def animals_status(self):
        lions = self.get_type(self.animals, "Lion")
        tigers = self.get_type(self.animals, "Tiger")
        cheetahs = self.get_type(self.animals, "Cheetah")
        new_line = "\n"

        return f"You have {len(self.animals)} animals\n" \
               f"----- {len(lions)} Lions:\n{''.join(lions)}\n" \
               f"----- {len(tigers)} Tigers:\n{new_line.join(tigers)}\n" \
               f"----- {len(cheetahs)} Cheetahs:\n{new_line.join(cheetahs)}"

    def workers_status(self):
        keepers = self.get_type(self.workers, "Keeper")
        caretakers = self.get_type(self.workers, "Caretaker")
        vets = self.get_type(self.workers, "Vet")
        new_line = "\n"

        return f"You have {len(self.workers)} workers\n" \
               f"----- {len(keepers)} Keepers:\n{new_line.join(keepers)}\n" \
               f"----- {len(caretakers)} Caretakers:\n{new_line.join(caretakers)}\n" \
               f"----- {len(vets)} Vets:\n{new_line.join(vets)}"


# zoo = Zoo("Zootopia", 3000, 5, 8)
#
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
#
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]
#
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
#
# # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))
#
# # Tending animals
# print(zoo.tend_animals())
#
# # Paying keepers
# print(zoo.pay_workers())
#
# # Fireing worker
# print(zoo.fire_worker("Adam"))
#
# # Printing statuses
# print(zoo.animals_status())
# print(zoo.workers_status())
