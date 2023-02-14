from exceptions import InvalidUserException


class UserValidator:
    def validate_user(self, user):
        if "name" not in user:
            raise InvalidUserException("No name provided")
        if "product" not in user:
            raise InvalidUserException("No product provided")
        if "car" not in user:
            raise InvalidUserException("No car provided")
