import re
from typing import List, Dict


class ReferenceSearcher:

    def __init__(self, data) -> None:
        self.data: str = data
        self.references_cited_on_text: List[Dict[str, str]] = []

    def search_references_on_data(self) -> str:
        first_pattern = '[A-Z]+[a-z]{1,20}[,]?[ ][0-9]{4}'
        raw_references = re.findall(first_pattern, self.data)
        references_without_duplication = list(set(raw_references))
        second_pattern = '([A-Z]+[a-z]{1,20})[,]?[ ]([0-9]{4})'
        for reference in references_without_duplication:
            treatment = re.search(second_pattern, reference)
            treated_reference = {
                'author': treatment.group(1),
                'year': treatment.group(2)
            }
            self.references_cited_on_text.append(treated_reference)

    def exporting_references_cited_on_text(self) -> List[Dict[str, str]]:
        return self.references_cited_on_text
