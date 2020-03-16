from datetime import date


class Person:

    def __init__(self, first, last, birth):
        self.first_name = first
        self.last_name = last
        self.birth_date = birth

    def full_name(self):
        """
        Returns full name with blank space.
        :return:
        """
        return "{} {}".format(self.first_name, self.last_name)

    def age(self):
        """
        Returns persons age.
        :return:
        """
        today = date.today()
        return today.year - self.birth_date.year - (
                    (today.month, today.day) < (self.birth_date.month, self.birth_date.day))


class Female(Person):

    def __init__(self, first, last, birth):
        super().__init__(self, first, last, birth)

    def full_name(self):
        super().full_name(self)

    def age(self):
        """
        Returns persons age but when person is over 20 then return 20.
        :return:
        """
        today = date.today()
        age = today.year - self.birth_date.year - (
                    (today.month, today.day) < (self.birth_date.month, self.birth_date.day))

        if age > 20:
            return 20
        else:
            return age
