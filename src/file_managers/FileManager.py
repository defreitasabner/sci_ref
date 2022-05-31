from abc import ABCMeta, abstractmethod


class FileManager(metaclass=ABCMeta):

    @abstractmethod
    def __create_file(self) -> None:
        ...

    @abstractmethod
    def __read_file(self) -> None:
        ...

    @abstractmethod
    def __write_file(self) -> None:
        ...

    @abstractmethod
    def __update_file(self) -> None:
        ...

    @abstractmethod
    def __export_data(self) -> str:
        ...
