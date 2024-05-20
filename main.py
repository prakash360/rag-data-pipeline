import os
import openai
from dotenv import load_dotenv, find_dotenv
from rag_data_pipeline.read_pdfs import PDFReader
from rag_data_pipeline.split_pdfs import DocumentSplitter
from rag_data_pipeline.vector_store import VectorStore


if __name__ == "__main__":
    print("Start of the main function inside rag data pipeline, reading PDFs....\n")
        
    pdf_paths = [
        './data/2405.10276v1.pdf',
        './data/2405.10317v1.pdf'
    ]
    
    pdf_text = []
    for pdf_path in pdf_paths:
        pdf_reader = PDFReader(pdf_path)
        pdf_text.extend(pdf_reader.read_pdf())

    print("Readin PDFs completed, splitting documents into chunks...")
    document_splitter = DocumentSplitter(pdf_text)
    chunk_splits = document_splitter.split_documents(method='chunk', chunk_size=500, chunk_overlap=100)
    print(f"Number of chunks: {len(chunk_splits)}. Printing a first few chunks...")
    
    for i, chunk in enumerate(chunk_splits[:2]):
        print(f"Chunk {i + 1}:\n{chunk.page_content}\n")

    _ = load_dotenv(find_dotenv())
    # Access the OpenAI API key from environment variables
    openai.api_key = os.environ['OPENAI_API_KEY']

    print("OpenAI API Key Loaded:", openai.api_key is not None)

    print("Creating vector store...")
    vector_store = VectorStore()    
    vector_store.add_texts(chunk_splits)

    # Query for similar vectors
    query = "What are the key limitations of small-scale language models like LLaMa when used as optimizers for automated prompt engineering techniques like OPRO?"
    print("Query text:: ", query)
    similar_results = vector_store.query(query, k=3)
    
    for result in similar_results:
        # print(f"result: {result.page_content}")
        print(result)

    print("\nend of the main function.\n")