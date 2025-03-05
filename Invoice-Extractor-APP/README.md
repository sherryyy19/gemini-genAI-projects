# Gemini Invoice Q&A Chatbot

## Introduction
The **Gemini Invoice Q&A Chatbot** is an intelligent application that leverages Google Generative AI to analyze uploaded invoice images and answer user questions about their content. It provides a streamlined and user-friendly interface for extracting meaningful insights from invoices in real-time.

## Key Insights
- This application demonstrates the integration of AI for practical, real-world applications such as invoice processing.
- It uses Google Generative AI (Gemini) to process images and provide contextual answers to user queries.
- The Streamlit framework powers the intuitive user interface, making it accessible and easy to use.

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
    streamlit run app.py
    ```
