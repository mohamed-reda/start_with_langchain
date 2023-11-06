from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings

import os

os.environ['OpenAI_API_KEY'] = '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'

llm = OpenAI(
    model_name="text-ada-001",
)

our_query = "What is the last name of Mohamed?"
print(llm(our_query))

data = PdfReader("text-ada-001.pdf")
combined_text = ""
for i, page in enumerate(data.pages):
    text = page.extract_text()
    if text:
        combined_text += text
print(combined_text)

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200,
    chunk_overlap=20,
    length_function=len
)
find_data = text_splitter.split_text(combined_text)
print(len(find_data))

embedding = OpenAIEmbeddings()

document_search = FAISS.from_texts(find_data, embedding)

chain = load_qa_chain(OpenAI(), chain_type="stuff")

our_query = "What is the last name of Mohamed?"
docs = document_search.similarity_search(our_query)

print(chain.run(input_documents=docs, question=our_query))
