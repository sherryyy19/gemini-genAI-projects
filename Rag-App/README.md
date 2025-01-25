# Chat with PDF using Gemini (RAG App)

## Introduction
The **Chat with PDF using Gemini** application leverages Retrieval-Augmented Generation (RAG) to enable users to upload PDF documents and interact with them via a chatbot. It combines advanced language modeling (Gemini LLM) and PDF parsing for contextual question-answering. This app is perfect for extracting insights from PDF files in an intuitive, conversational manner.

## Features
- Upload multiple PDF files.
- Extract and process text from uploaded documents.
- Ask context-specific questions and get detailed answers.
- Uses Gemini LLM for high-quality, accurate responses.
- Provides a user-friendly Streamlit interface.

## Setup Instructions

### 1. Create a Virtual Environment
To ensure all dependencies are isolated and the environment is consistent, create a virtual environment using Conda:

`conda create -p venv python=3.12.8 -y`

### 2. Install Required Libraries
Once the virtual environment is set up, install all the required libraries using the provided `requirements.txt` file:

`pip install -r requirement.txt`

### 3. Set Up Environment Variables
- Create a `.env` file in the project directory.
- Add your Google API key in the following format:
- 
  `GOOGLE_API_KEY= "your_google_api_key_here"`
  
## Tools and Technologies Used
- **Programming Language:** Python 3.12.8
- **Framework:** Streamlit, Langchain
- **FAISS:** Vector search engine for similarity-based document retrieval.
- **AI API:** Google Generative AI (Gemini)
- **Libraries:**
  - `dotenv` for environment variable management
  - `PyPDF2` to read and extract data from PDF's
  - `google-generativeai` for AI capabilities

## How to Run
- Open terminal in VS Code and run the command:
   
   `streamlit run ragapp.py`

