import csv
from typing import Dict

from FileManager import FileManager


class CsvFileManager(FileManager):

    def __init__(self, input_path: str) -> None:
        self.__input_path: str = input_path
        self.__output_path: str = None
        self.__reference_list: Dict[str, str] = None

    def __create_file(self) -> None:
        with open(file=self.__input_path, mode='x', encoding='utf-8-sig') as file:
            pass

    def __read_file(self) -> None:
        with open(file=self.__input_path, mode='r', encoding='utf-8-sig') as file:
            reference_list = csv.DictReader(file)
            self.__reference_list = reference_list

    def __write_file(self) -> None:
        with open(file=self.__output_path, mode='w', encoding='utf-8-sig') as file:
            pass

    def __update_file(self) -> None:
        with open(file=self.__input_path, mode='a', encoding='utf-8-sig') as file:
            pass

    def __export_data(self) -> Dict[str, str]:
        return self.__data
