from abc import ABCMeta, abstractmethod


class FileReader(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.data = None

    @abstractmethod
    def open_file(self) -> None:
        with open(self.file_path, mode="r", encoding="utf-8-sig") as file:
            pass

    @abstractmethod
    def export_data(self) -> str:
        return self.data