import csv

from test_users_functions import workers


# -------------------------------------------------------------------------------------
# Прямолинейный вариант теста
# -------------------------------------------------------------------------------------


def test_workers_are_adults():
    """
    Тестируем, что все работники старше 18 лет
    """
    with open("users.csv") as file_csv:
        users = list(csv.DictReader(file_csv, delimiter=';'))
        workers = [user for user in users if user['status'] == 'worker']

    for worker in workers:
        assert int(worker["age"]) >= 18, f"Пользователь {worker['name']} младше 18 лет"

        # workers = []
        # for user in users:
        #     if user["status"] == "worker":
        #         workers.append(user)



