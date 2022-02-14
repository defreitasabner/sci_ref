import re
from typing import List, Dict
import docx

from constants import MONTH_LIST


class TextReader:

    def __init__(self):
        self.file_path: str = './mocks/neotropical_caliscelids_review.docx'
        self.raw_text: str = None
        self.reference_list: List[Dict[str, str]] = []

    def open_main_file(self, file) -> str:
        with open(file, mode="r", encoding="utf-8-sig") as main_file:
            pass

    def extractRawText(self) -> None:
        document = docx.Document(self.file_path)
        raw_text_temp = []

        for paragraph in document.paragraphs:
            raw_text_temp.append(paragraph.text)

        self.raw_text = '\n'.join(raw_text_temp)

    def search_references_on_raw_text(self) -> str:
        first_pattern = '[A-Z]+[a-z]{1,20}[,]?[ ][0-9]{4}'
        raw_references = re.findall(first_pattern, self.raw_text)
        references_without_duplication = list(set(raw_references))
        second_pattern = '([A-Z]+[a-z]{1,20})[,]?[ ]([0-9]{4})'
        for reference in references_without_duplication:
            treatment = re.search(second_pattern, reference)
            treated_reference = {
                'author': treatment.group(1),
                'year': treatment.group(2)
            }
            self.reference_list.append(treated_reference)

    def removing_dates(self):
        for item in self.reference_list:
            if item['author'] in MONTH_LIST:
                self.reference_list.remove(item)
                print(item)


test = TextReader()
test.extractRawText()
test.search_references_on_raw_text()
test.removing_dates()

print(test.reference_list)
print(len(test.reference_list))
