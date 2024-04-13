import streamlit as st
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
import  os
# Set OpenAI API key
os.environ['OPENAI_API_KEY'] = "Your_API_KEY"

# Load the saved Chroma database and embeddings
persist_dir = 'db'
embeddings = OpenAIEmbeddings()
vectordb = Chroma(persist_directory=persist_dir, embedding_function=embeddings)
retriever = vectordb.as_retriever()

# Create a RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type='stuff', retriever=retriever, return_source_documents=True)

# Define a function to process queries and get responses
def process_query(query):
    llm_response = qa_chain(query)
    return llm_response['result']

# Streamlit UI

st.markdown("<h1 style='text-align: center;'>RAG⛓️</h1>", unsafe_allow_html=True)
# Create a layout with two columns
col1, col2 = st.columns(2)

# Input prompt and "Get Answer" button in the first column
prompt = col1.text_input("Enter your prompt:")
if col1.button("Get Answer"):
    if prompt:
        answer = process_query(prompt)
        col1.text_area("Answer:", value=answer, height=200)
    else:
        col1.warning("Please enter a prompt.")

# "Clear" button in the second column
if col1.button("Clear"):
    prompt = ""



# Add technology used list in the bottom menu with uploaded icons
st.sidebar.title("Technologies Used")
st.sidebar.markdown("*  Python")
st.sidebar.markdown("*  ChatGPT")
st.sidebar.markdown("*  Streamlit")
st.sidebar.markdown("*  OpenAI API")
st.sidebar.markdown("*  Langchain")
st.sidebar.markdown("*  ChromaDb")







