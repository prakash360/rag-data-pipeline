# RAG Data Pipeline

## Overview

This project demonstrates how to read a PDF file, split the text into chunks, vectorize the text, and store the vectors in a vector store for efficient querying.

## Features

- Read a PDF file and extract the text content

- Split the text into smaller chunks for better processing

- Vectorize the text chunks using a text vectorization model

- Store the text chunks and their corresponding vectors in a vector store

- Query the vector store to find the most similar text chunks to a given query

## Requirements
- Python 3.9 or higher

- Either Poetry or Docker

- OpenAI API key (for accessing the text vectorization model)

## Installation & Setup
#### 1. Clone the repository:

```bash 
git clone https://github.com/prakash360/rag-data-pipeline.git 
```

#### 2. Navigate to the project directory:

```bash
cd rag-data-pipeline
```

#### 3. Set the OpenAI API key in .env file. The easiest way is to create a .env file from the provided example:

```bash
cp .env.example .env
```
And then populate your `.env` file with your own OpenAI API Key.

## Installation & Running the Project

#### Option 1: Using Poetry

- Install Poetry (if not already installed)
- Install the project dependencies using `poetry install`
- Run the project using `poetry run python main.py`

#### Option 2: Using Docker

- Build the Docker image:

```bash
docker build -t rag-data-pipeline .
```

- Run the Docker container:

```bash
docker run --env-file .env -it rag-data-pipeline
```

## Usage



Run of the `main.py` script will:

- Reads PDF files from specified paths.
- Split the text into chunks of 500 characters with 100 characters of overlap
- Uses OpenAI's text vectorization model to generate vectors for each text chunk
- Stores the text chunks and their corresponding vectors in a vector database
- Query the vector store for the top 3 most similar text chunks for the added query 
- Print the content of the similar text chunks

To Customize the script:

- Modify the pdf_paths list in the script to include the paths of the PDF files you want to process. Makes sure to copy the files in the respective folders
- Change the chunk_size and chunk_overlap parameters in the split_documents method call if needed
- Change the query variable to search for different texts

