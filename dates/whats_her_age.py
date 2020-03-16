import datetime

def get_age(birth_date, current_date=None):
    if current_date == None:
        current_date = datetime.date.today()
    return current_date.year - birth_date.year - (
                (current_date.month, current_date.day) < (birth_date.month, birth_date.day))


