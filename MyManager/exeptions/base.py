# Базовый класс для всех моих кастомных исключений

class BaseAppError(Exception):

    def __init__(self, *args):
        super().__init__(*args)


class ExitApp(BaseAppError):
    """Сигнал завершения приложения"""