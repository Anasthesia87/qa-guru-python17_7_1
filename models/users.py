from dataclasses import dataclass
from enum import Enum

USER_ADULT_AGE = 18


class UserStatus(Enum):
    student = 'student'
    worker = 'worker'

@dataclass()
class User:
    name: str
    age: int
    status: UserStatus
    items: list[str]

    def is_adult(self):
        return self.age >= USER_ADULT_AGE


class Worker(User):

    status = UserStatus.worker

    def __init__(self, name, age, items):
        self.name = name
        self.age = age
        self.items = items

    def do_work(self):
        pass

    # def __init__(self, name, age, status, items):  уже есть в dataclass
    #     self.name = name
    #     self.age = age
    #     self.status = status
    #     self.items = items


    # def __eq__(self, other):   уже есть в dataclass
    #     return (self.name == other.name,
    #             self.age == other.age,
    #             self.status == other.status,
    #             self.items == other.items)





if __name__ == '__main__':
    d = {'name': 'Oleg',
         'age': 20,
         'status': 'student',
         'items': ['book','pen','paper']}

    oleg = User(name='Oleg', age=16, status=UserStatus.student, items=['book','pen','paper'])
    oleg2 = User(name='Oleg', age=16, status=UserStatus.student, items=['book', 'pen', 'paper'])
    olga = User(name='Olga', age=18, status=UserStatus.worker, items=['book', 'paper'])

    olga_worker = Worker(name='Olga', age=18, items=['book', 'paper'])

    # assert oleg == oleg2
    # assert olga == olga_worker

    assert oleg.age == 16
    assert olga.age == 18

    olga.age += 1

    assert olga.age == 19
