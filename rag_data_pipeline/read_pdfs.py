import unittest
from unittest.mock import patch, mock_open
from rag_data_pipeline.read_pdfs import PDFReader
from rag_data_pipeline.split_pdfs import Document

class TestPDFReader(unittest.TestCase):
    def setUp(self):
        self.file_path = "/path/to/test.pdf"
        self.pdf_reader = PDFReader(self.file_path)

    def test_init(self):
        self.assertEqual(self.pdf_reader.file_path, self.file_path)
        self.assertIsInstance(self.pdf_reader.loader, PyPDFLoader)
        self.assertIsNone(self.pdf_reader.documents)

    @patch('rag_data_pipeline.read_pdfs.PyPDFLoader.load')
    def test_read_pdf_with_documents(self, mock_load):
        mock_documents = [
            Document(page_content="This is a test document."),
            Document(page_content="This is another test document.")
        ]
        mock_load.return_value = mock_documents
        documents = self.pdf_reader.read_pdf()
        self.assertIsNotNone(documents)
        self.assertEqual(len(documents), 2)
        self.assertEqual(documents[0].page_content, "This is a test document.")
        self.assertEqual(documents[1].page_content, "This is another test document.")

    @patch('rag_data_pipeline.read_pdfs.PyPDFLoader.load')
    def test_read_pdf_with_no_documents(self, mock_load):
        mock_load.return_value = []
        documents = self.pdf_reader.read_pdf()
        self.assertIsNone(documents)

    def test_clean_text(self):
        test_text = "   This is a test document.   \n\n123 Header\nFooter 456\n●•◆ Test ◆•● "
        expected_text = "This is a test document. Test"
        cleaned_text = self.pdf_reader.clean_text(test_text)
        self.assertEqual(cleaned_text, expected_text)

if __name__ == '__main__':
    unittest.main()
