import csv
import pytest

from models.providers import UserProvider, CsvUserProvider, DatabaseUserProvider, ApiUserProvider
from models.users import User, USER_ADULT_AGE, UserStatus, Worker


# -------------------------------------------------------------------------------------
# Используем объектный подход работы с данными.
# -------------------------------------------------------------------------------------
@pytest.fixture(params=[CsvUserProvider, DatabaseUserProvider, ApiUserProvider])
def user_provider(request) -> UserProvider:
    return request.param()


@pytest.fixture
def users(user_provider) -> list[User]:
    return user_provider.get_users()


    # with open("users.csv") as file_csv:
    #     users = list(csv.DictReader(file_csv, delimiter=';'))
    # return [User(name=user['name'],
    #              age=int(user['age']),
    #              status=UserStatus(user['status']),
    #              items=user['items'])
    #         for user in users
    #         ]
    # return [
    #     User(**user)
    #     for user in users
    # ]


@pytest.fixture
def workers(users) -> list[Worker]:
    """
    Берем только работников из списка пользователей
    """
    workers = [Worker(name=user.name, age=user.age, items=user.items)
               for user in users if user.status == UserStatus.worker]
    return workers


def test_workers_are_adults_v3(workers):
    """
    Тестируем, что все работники старше 18 лет
    """
    for worker in workers:
        # worker.do_work()
        assert worker.is_adult(), f"Worker {worker.name} младше {USER_ADULT_AGE} лет"



