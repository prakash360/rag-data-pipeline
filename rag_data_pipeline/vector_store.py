from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.docstore.document import Document
import os, shutil
from typing import List, Tuple


class VectorStore:
    def __init__(self, persist_directory: str = "./data/chromadb") -> None:
        """
        Initializes the VectorStore class.

        Args:
            persist_directory (str, optional): The directory to persist the Chroma database. Defaults to "./data/chromadb".
        """        
        self.persist_directory = persist_directory
        self.embedding = OpenAIEmbeddings()
        # Check if the persist_directory exists and delete it if it does
        if os.path.exists(self.persist_directory):
            shutil.rmtree(self.persist_directory)
            print(f"Deleted previous Chroma database at: {self.persist_directory}")

    def add_texts(self, splits: List[Document]) -> None:
        """
        Adds the given text splits to the Chroma vector store.

        Args:
            splits (List[Document]): A list of Document objects containing the text to be added to the vector store.
        """    
        print(f"adding {len(splits)} splits to Chroma vector store...")
        try:
            self.vectordb = Chroma.from_documents(
                documents=splits,
                embedding=self.embedding,
                persist_directory=self.persist_directory
            )
            print("Vector DB Initialized:", self.vectordb)
        except Exception as e:
            print(f"Error initializing vector DB: {e}")

        print(f"added {self.vectordb._collection.count()} of documents in the vector store.")        
        # print(self.vectordb.get(include=['embeddings', 'documents', 'metadatas']))        
        # results = self.vectordb.get()


    def query(self, query: str, k: int = 5) -> List[Tuple[Document, float]]:
        """
        Queries the Chroma vector store and returns the top k most similar documents.

        Args:
            query (str): The query string to search for.
            k (int, optional): The number of most similar documents to return. Defaults to 5.

        Returns:
            List[Tuple[Document, float]]: A list of tuples, where each tuple contains a Document object and its similarity score.
        """
        # return self.vectordb.similarity_search(query, k=k)
        return self.vectordb.similarity_search_with_score(query, k=k)
