import csv

from exceptions import UserNotFoundException
from user_validator import UserValidator


class UserRepository:
    def __init__(self, file_name):
        self.file_name = file_name
        self.validator = UserValidator()

    def add_user(self, user):
        self.validator.validate_user(user)
        with open(self.file_name, "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(user.values())

    def find_by_name(self, name):
        with open(self.file_name, 'r') as f:
            reader = csv.DictReader(f)
            for user in reader:
                if user["name"] == name:
                    return user
        raise UserNotFoundException(f"User {name} not found")

    def delete_by_name(self, name):
        found_users = []
        is_found = False
        with open(self.file_name, 'r') as f:
            reader = csv.DictReader(f)
            for user in reader:
                if user["name"] == name:
                    is_found = True
                    continue
                found_users.append(user.values())
        if not is_found:
            raise UserNotFoundException(f"User {name} not found")
        self.write_all(found_users)

    def write_all(self, users):
        with open(self.file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["name", "age"])
            if users:
                writer.writerows(users)

    def update_age(self, name, change):
        found_users = []
        with open(self.file_name, 'r') as f:
            reader = csv.DictReader(f)
            for user in reader:
                if user["name"] == name:
                    user["age"] = change['age']
                    found_users.append(user.values())
                else:
                    found_users.append(user.values())
        with open(self.file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["name", "age"])
            if found_users:
                writer.writerows(found_users)
