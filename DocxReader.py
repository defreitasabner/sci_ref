import docx


class DocxReader:

    def __init__(self, file_path: str) -> None:
        self.file_path: str = file_path
        self.raw_text: str = None

    def extract_raw_text(self) -> None:
        document = docx.Document(self.file_path)
        raw_text_temp = []
        for paragraph in document.paragraphs:
            raw_text_temp.append(paragraph.text)
        self.raw_text = '\n'.join(raw_text_temp)

    def export_raw_text(self) -> str:
        return self.raw_text
