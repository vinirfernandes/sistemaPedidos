class EmailAlreadyExist(Exception):
    def __init__(self, message="Email already exist"):
        super().__init__(message)