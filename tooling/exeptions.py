class CustomExeption(Exception):
    def __init__(self, message):
        super().__init__(message)

raise CustomExeption("Bad Request")