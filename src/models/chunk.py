class Chunk:
    def __init__(self, paper_id:str, chunk_id:str, content:str, start_idx:int, end_idx:int, metadata:dict, search_vector:list[float]):
        self.paper_id = paper_id
        self.chunk_id = chunk_id
        self.content = content
        self.start_idx = start_idx
        self.end_idx = end_idx
        self.metadata = metadata
