from src import DocxReader
from src.ReferenceSearcher import ReferenceSearcher
from src.DataTreater import DataTreater

file_path = './mocks/neotropical_caliscelids_review.docx'

docx_reader = DocxReader(file_path)

docx_reader.extract_raw_text()
raw_text = docx_reader.export_raw_text()

reference_searcher = ReferenceSearcher(raw_text)
reference_searcher.search_references_on_data()
reference_list = reference_searcher.exporting_references_cited_on_text()

data_treater = DataTreater(reference_list)
data_treater.remove_month()
data_treater.remove_future_date()
reference_list_treated = data_treater.export_reference_list_treated()

print(reference_list_treated)
