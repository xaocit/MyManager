from .base import BaseAppError

class LoadSaveDataBaseError(BaseAppError):
    pass


class DecoderDataBaseError(LoadSaveDataBaseError):

    def __init__(self, reason):

        message = f"Данные не в формате json: {reason}"

        super().__init__(message)

class FileWithDataBaseFoundError(LoadSaveDataBaseError):

    def __init__(self, file_path: str):

        message = f"Файл с базой данных по пути {file_path} не найден !"

        super().__init__(message)


class SaveDataBaseError(LoadSaveDataBaseError):

    def __init__(self, reason: str):

        message = f"Ошибка сохранения базы данных: {reason}"

        super().__init__(message)