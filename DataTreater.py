from typing import List, Dict
from datetime import date

from constants import MONTH_LIST


class DataTreater:

    def __init__(self, reference_list: List[Dict[str, str]]) -> None:
        self.reference_list = reference_list

    def remove_month(self) -> None:
        print(
            "Removing data which key 'author' are months because they usually are dates, but check it."
        )
        for item in self.reference_list:
            if item['author'] in MONTH_LIST:
                self.reference_list.remove(item)
                print(item)

    def remove_future_date(self) -> None:
        print(
            f"Removing data which key 'year' are future dates (after {date.today().year})"
        )
        for item in self.reference_list:
            if int(item['year']) > date.today().year:
                self.reference_list.remove(item)
                print(item)

    def export_reference_list_treated(self) -> List[Dict[str, str]]:
        return self.reference_list
