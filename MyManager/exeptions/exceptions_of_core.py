from .base import BaseAppError


class ValidationInputDataError(BaseAppError):
    pass


class InvalidInputIdError(ValidationInputDataError):

    def __init__(self, provided_str: str, reason: str):

        message = f"Некорректный ID '{provided_str}': {reason}"

        super().__init__(message)

class InvalidInputDateError(ValidationInputDataError):

    def __init__(self, provided_str: str, reason: str):

        message = f"Некорректная дата '{provided_str}': {reason}"

        super().__init__(message)

class InvalidInputAmountError(ValidationInputDataError):

    def __init__(self, provided_str: str, reason: str):

        message = f"Некорректная сумма '{provided_str}': {reason}"

        super().__init__(message)

class InvalidInputTypeOfOperationError(ValidationInputDataError):

    def __init__(self, provided_str: str, reason: str):

        message = f"Некорректный тип операции '{provided_str}': {reason}"

        super().__init__(message)