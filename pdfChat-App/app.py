import streamlit as st
import os
import google.generativeai as genai

from PyPDF2 import PdfReader

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

from dotenv import load_dotenv

# take environment variables from .env.
load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to read PDFs
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)  # Pass each file individually
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# creating chunks
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

# store embeddings
def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")


def get_conversational_chain():

    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    # load the gemini model
    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash",temperature=0.3)

    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain

# handle user input
def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()

    
    response = chain(
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=True)

    print(response)
    st.write("Reply: ", response["output_text"])

def main():
    st.set_page_config("RAG App")
    
    # Custom Styles
    st.markdown(
        """
        <style>
            body {
                background: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
                color: #000000;
                font-family: 'Arial', sans-serif;
            }
            .stButton>button {
                background-color: #4CAF50;
                color: white;
                border-radius: 8px;
            }
            .stTextInput>div>div>input {
                border: 2px solid #4CAF50;
                border-radius: 8px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.header("Chat with Multiple PDF using Gemini💁")
    st.subheader("Upload your PDFs and ask questions interactively")
    
    # user input section
    user_question = st.text_input("Ask a Question from the PDF Files")

    if user_question:
        user_input(user_question)

    # sidebar
    with st.sidebar:
        st.sidebar.title("Gemini RAG Application")
        st.sidebar.markdown(
    """
    <div style="text-align: center;">
        <img src="https://static.vecteezy.com/system/resources/previews/032/807/338/non_2x/rag-creative-icon-design-free-vector.jpg" 
             alt="Your AI Assistant" 
             style="width: 100px; height: auto;">
        <p style="text-align: center;">Your AI Assistant</p>
    </div>
    """,
    unsafe_allow_html=True
)
        
        st.title("Menu:")
        """
            ### Instructions:
            1. Upload PDFs to create a knowledge base.
            2. Ask relevant questions.
            3. Get detailed responses from the AI.
        """
        pdf_docs = st.file_uploader("Upload PDF Files", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Done")

if __name__ == "__main__":
    main()
