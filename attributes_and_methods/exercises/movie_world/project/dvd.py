import calendar


class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {self.check_if_rented()}"

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        day, month, year = date.split(".")
        month = calendar.month_name[int(month)]
        year = int(year)
        return cls(name, id, year, month, age_restriction)

    def check_if_rented(self):
        if self.is_rented:
            return "rented"
        return "not rented"
