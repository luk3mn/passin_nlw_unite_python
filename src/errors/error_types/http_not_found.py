class HttpNotFoundError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.messge = message
        self.name = "Not Found"
        self.status_code = 404