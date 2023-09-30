
import streamlit as st
import os

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
"""
# Open Ai Based ChatBot

"""

os.environ['OPENAI_API_KEY'] = st.secrets["OPENAI_API_KEY"]
st.write("Please type a question regarding the vision pro headet lets see if this updates!!")
st.text_input("Question", key="question")
query = st.session_state.question

def store_data_in_db(texts):
  persistent_directory = 'db'
  embedding = OpenAIEmbeddings()
  vectordb = Chroma.from_documents(documents=texts,embedding=embedding,persist_directory=persistent_directory)
  return vectordb
def retrieve_db():
    embedding = OpenAIEmbeddings()
    return Chroma(persist_directory='db',embedding_function=embedding)
def read_files(folder_path):
    loader = DirectoryLoader(folder_path, glob="./*.txt", loader_cls=TextLoader)
    return loader.load()
def generate_texts(files):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(files)
    return texts
def process_llm_response(llm_response):
    st.write(llm_response['result'])
    st.write('\n\nSources:')
    for source in llm_response["source_documents"]:
        st.write(source.metadata['source'])
vector_db = retrieve_db()
num_items_in_db = len(vector_db.get()["ids"])
if num_items_in_db == 0:
    files = read_files("./Documents")
    texts = generate_texts(files)
    vector_db = store_data_in_db(texts=texts)
retriever = vector_db.as_retriever(search_kwargs = {"k":1})
qa_chain = RetrievalQA.from_chain_type(llm=OpenAI(),chain_type="stuff",retriever=retriever,return_source_documents=True)
if(len(query) != 0):
    llm_response = qa_chain(query)
    process_llm_response(llm_response)