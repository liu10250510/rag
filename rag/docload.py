from langchain_community.document_loaders import CSVLoader, PyPDFLoader


# Load data from a CSV file using CSVLoader
def csv_loader(file_path):
	loader = CSVLoader(file_path)
	return loader.load()

# Load data from a PDF file using PyPDFLoader
def pdf_loader(file_path):
	try:
		loader = PyPDFLoader(file_path)
	except Exception as e:
		print(f"Error loading PDF document: {e}")
		return None
	# Load the PDF document and return the list of documents
	return loader.load()

if __name__ == "__main__":
	# Example usage
	try:
		pdf_documents = pdf_loader("./data/resume.pdf")
	except Exception as e:
		print(f"Error loading PDF document: {e}")
	# Print the number of documents loaded
	if pdf_documents:
		print(f"Loaded {len(pdf_documents)} documents from the PDF file.")
	else:
		print("No documents loaded from the PDF file.")