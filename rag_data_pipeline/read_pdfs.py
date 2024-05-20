from langchain_community.document_loaders import PyPDFLoader
import re
from typing import List, Optional

from rag_data_pipeline.split_pdfs import Document


class PDFReader:
    def __init__(self, file_path: str) -> None:
        """
        Initializes the PDFReader class.

        Args:
            file_path (str): The file path of the PDF document.
        """
        self.file_path = file_path
        self.loader = PyPDFLoader(self.file_path)
        self.documents = None

    def clean_text(self, text: str) -> str:
        """
        Cleans up the given text by removing extra whitespace, numbers, and header/footer lines.
        
        Args:
            text (str): The text to be cleaned.
        
        Returns:
            str: The cleaned text.
        """
        # Normalize whitespace 
        cleaned_text = re.sub(r'\s+', ' ', text)
        # Remove html tags
        cleaned_text = re.sub(r'<.*?>', '', cleaned_text)
        # remove header and footers
        cleaned_text = re.sub(r'^\w+\s\d+$', '', cleaned_text, flags=re.MULTILINE)
        # Remove Special Character 
        cleaned_text = re.sub(r'[●•◆]', '', cleaned_text)
        # Keep only alphanumeric characters and some punctuation
        cleaned_text = re.sub(r'[^a-zA-Z0-9,.?!;:\'\"()\s]', '', cleaned_text)
        return cleaned_text.strip()


    def read_pdf(self) -> Optional[List[Document]]:
        """
        Reads the PDF document and returns the cleaned text.

        Returns:
            Optional[List[Document]]: The list of documents loaded from the PDF, or None if no documents were loaded.
        """
        self.documents = self.loader.load()
        if self.documents:
            print(f"Loaded {len(self.documents)} document(s) from the PDF.")
            for doc in self.documents:
                doc.page_content = self.clean_text(doc.page_content)
            print(f"First document content preview: {self.documents[0].page_content[:500]}")
        else:
            print("No documents loaded.")
        return self.documents
