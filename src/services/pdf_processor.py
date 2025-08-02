from langchain_community.document_loaders import PyPDFLoader
import os

def get_pdfs_from_folder(documents_path):
    '''This function identifies all pdf files in the documents path and returns a list of file paths'''
    pdf_files = []
    for file in os.listdir(documents_path):
        if file.endswith('.pdf'):
            full_path = os.path.join(documents_path, file)
            pdf_files.append(full_path)
    return pdf_files

def extract_text_from_pdf(pdf_files):
    '''This function processes individual pdf files and returns a dictionary of processed documents'''
    pdf_content = {}
    paper_id = 1
    for pdf_file in pdf_files:
        loader = PyPDFLoader(pdf_file)
        docs = loader.load()
        pdf_content[f'paper_{paper_id}'] = {'path': pdf_file, 'content': docs}
        paper_id += 1
    return pdf_content

