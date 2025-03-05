# Gemini LLM QA Chatbot

## Introduction
The **Gemini LLM QA Chatbot** is an interactive application that uses Google Generative AI (Gemini) to provide real-time answers to user queries. The chatbot maintains a chat history for the session, enabling users to review past interactions. Built with Streamlit, the application delivers a user-friendly interface for seamless communication with an advanced LLM.

## Features
- **Real-Time Responses**: Leverages Gemini LLM for fast and accurate answers.
- **Session Chat History**: Keeps track of the conversation during the session.
- **Interactive UI**: Simple and clean interface for user interaction.
- **Customizable**: Extendable for various use cases.
  
## Setup Instructions

### 1. Create a Virtual Environment
To ensure all dependencies are isolated and the environment is consistent, create a virtual environment using Conda:

```sh
conda create -p venv python=3.12.8 -y
```

### 2. Install Required Libraries
Once the virtual environment is set up, install all the required libraries using the provided `requirements.txt` file:

```sh
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
- Create a `.env` file in the project directory.
- Add your Google API key in the following format:
- 
  `GOOGLE_API_KEY= "your_google_api_key_here"`

## Tools and Technologies Used
- **Programming Language:** Python 3.12.8
- **Framework:** Streamlit
- **AI API:** Google Generative AI (Gemini)
- **Libraries:**
  - `dotenv` for environment variable management
  - `google-generativeai` for AI capabilities

## How to Run
- Open terminal in VS Code and run the command:
   
   ```sh
  streamlit run chatapp.py
   ```
