import csv

from models.users import User, UserStatus


class UserProvider:

    def get_users(self) -> list[User]:
        raise NotImplementedError

class CsvUserProvider(UserProvider):


   def get_users(self) -> list[User]:
       with open("users.csv") as file_csv:
          users = list(csv.DictReader(file_csv, delimiter=';'))
       return [User(name=user['name'],
                 age=int(user['age']),
                 status=UserStatus(user['status']),
                 items=user['items'])
            for user in users
            ]

class DatabaseUserProvider(UserProvider):

    def get_users(self) -> list[User]:
        raise NotImplementedError

class ApiUserProvider(UserProvider):

    def get_users(self) -> list[User]:
        raise NotImplementedError