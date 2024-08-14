class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}s"

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.amount

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return Currency(self.currency, self.amount + other.amount)
        elif isinstance(other, (int, float)):
            return Currency(self.currency, self.amount + other)
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        elif isinstance(other, (int, float)):
            self.amount += other
        else:
            return NotImplemented
        return self
    
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
print(c1) 

# print(c1 + c3)



# 2 ----------------------------------------------------

from func import sum_numbers

sum_numbers(5, 10)



#3 ------------------------------------------------------
import random
import string

def generate_random_string(length=5):
    return ''.join(random.choices(string.ascii_letters, k=length))

random_string = generate_random_string()

#4-----------------------------------------------------------

from datetime import datetime

def display_current_date():
    print(datetime.now().strftime("%Y-%m-%d"))

display_current_date()


#5 ------------------------------------------------------------ 

def time_until_january_first():
    now = datetime.now()
    next_january_first = datetime(now.year + 1, 1, 1)
    time_left = next_january_first - now
    print(f"The 1st of January is in {time_left}")

time_until_january_first()


#6 ------------------------------------------------------------ 

def minutes_lived(birthdate_str, date_format="%Y-%m-%d"):
    birthdate = datetime.strptime(birthdate_str, date_format)
    now = datetime.now()
    minutes = int((now - birthdate).total_seconds() // 60)
    print(f"You have lived for {minutes} minutes.")

result = minutes_lived("1990-01-01")
print(result)


#7------------------------------------------------------------

pip install faker
from faker import Faker

# NOTE TO CHECKER - I AM NOT SURE WHY THIS IMPORT FAILED?
