from langchain.text_splitter import TokenTextSplitter, RecursiveCharacterTextSplitter
from typing import List


class Document:
    """
    Represents a document with page content and optional metadata.

    Attributes:
        page_content (str): The content of the document.
        metadata (Optional[Dict[str, Any]]): The metadata associated with the document.
    """
    def __init__(self, page_content, metadata=None):
        self.page_content = page_content
        self.metadata = metadata if metadata else {}

class DocumentSplitter:

    def __init__(self, documents: List[Document]) -> None:
        """
        Initializes the DocumentSplitter class which splits documents into smaller chunks or paragraphs.

        Attributes:
            documents (List[Document]): The list of documents to be split.
        """        
        self.documents = documents

    def split_by_chunk(self, chunk_size: int, chunk_overlap: int) -> List[Document]:
        """
        Splits the documents into chunks of a specified size with a given overlap.

        Args:
            chunk_size (int): The size of each chunk.
            chunk_overlap (int): The amount of overlap between chunks.

        Returns:
            List[Document]: The list of document chunks.
        """
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        splits = text_splitter.split_documents(self.documents)
        return [Document(split.page_content, split.metadata) for split in splits]

    def split_by_paragraph(self) -> List[Document]:
        """
        Splits the documents into paragraphs.

        Returns:
            List[Document]: The list of document paragraphs.
        """
        text_splitter = TokenTextSplitter()
        splits = text_splitter.split_documents(self.documents)
        return [Document(split.page_content, split.metadata) for split in splits]

    def split_documents(self, method: str = 'chunk', chunk_size: int = 1000, chunk_overlap: int = 200) -> List[Document]:
        """
        Splits the documents using the specified method.

        Args:
            method (str): The splitting method to use, either 'chunk' or 'paragraph'.
            chunk_size (int): The size of each chunk (used only when method is 'chunk').
            chunk_overlap (int): The amount of overlap between chunks (used only when method is 'chunk').

        Returns:
            List[Document]: The list of split documents.

        Raises:
            ValueError: If the specified method is invalid.
        """
        if method == 'chunk':
            return self.split_by_chunk(chunk_size, chunk_overlap)
        elif method == 'paragraph':
            return self.split_by_paragraph()
        else:
            raise ValueError("Invalid splitting method. Use 'chunk' or 'paragraph'.")