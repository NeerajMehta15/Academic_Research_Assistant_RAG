class Paper:
    def __init__(self, title:str, abstract:str, authors:list[str], year:int, venue:str, content:str, file_path:str, paper_id:str, citations:list[str]):
        self.title = title
        self.abstract = abstract
        self.authors = authors
        self.year = year
        self.venue = venue
        self.content = content      
        self.file_path = file_path  
        self.paper_id = paper_id  
        self.citations = citations  