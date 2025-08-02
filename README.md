# 🩺 Medical Chatbot (RAG-based) 🤖

<div align="center">

[![License](https://img.shields.io/badge/License-Apache_2.0-blue?style=plastic)](https://opensource.org/licenses/Apache-2.0)&nbsp;&nbsp;[![Build](https://img.shields.io/badge/Build-Passing-green?style=plastic&logo=githubactions)](https://github.com/adityajayashankar/Med_Chatbot/actions/workflows/medical_chatbot_ci.yml)&nbsp;&nbsp;![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue?style=plastic&logo=githubactions&logoColor=white)&nbsp;&nbsp;![Python](https://img.shields.io/badge/Python-3.11-blue?style=plastic&logo=python&logoColor=white)&nbsp;&nbsp;![LangChain](https://img.shields.io/badge/LangChain-0.1.x-orange?style=plastic&logo=chainlink)

![Flask](https://img.shields.io/badge/Backend-Flask-black?style=plastic&logo=flask)&nbsp;&nbsp;![Pinecone](https://img.shields.io/badge/VectorDB-Pinecone-1f66c1?style=plastic&logo=pinecone)&nbsp;&nbsp;![Groq](https://img.shields.io/badge/Groq-LPU_Powered-black?style=plastic)&nbsp;&nbsp;![Render](https://img.shields.io/badge/Deployed_on-Render-3C3C3D?style=plastic&logo=render)&nbsp;&nbsp;![Platform](https://img.shields.io/badge/Platform-Windows_|_Linux_|_Mac-success?style=plastic)

</div>

Med_Chatbot is an intelligent, conversational AI designed to provide information from medical literature. It leverages a **Retrieval-Augmented Generation (RAG)** pipeline to deliver accurate and context-aware answers based on a foundational medical text.

This project is built using **LangChain** to orchestrate the workflow, **Pinecone** as the vector database for efficient knowledge retrieval, and **Grok** as the core Large Language Model for generating human-like responses. The application is served through a clean web interface built with Flask and is deployed on **Render** with a full CI/CD pipeline.
> ⚠️ **Important Note:** The live Render deployment is currently paused as the application's memory requirements exceed the free tier limits. However, the project is fully functional and can be run on your local machine by following the setup instructions below.

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen?style=plastic&logo=rocket)](https://med-chatbot.onrender.com)

## ✨ Features

* **Retrieval-Augmented Generation (RAG):** Answers are grounded in the provided medical text (`Medical_book.pdf`), reducing hallucinations and ensuring factual accuracy.
* **High-Performance Vector Search:** Utilizes **Pinecone** to store and retrieve relevant text embeddings with high speed and efficiency.
* **Advanced LLM:** Powered by the **Grok** model for nuanced and coherent response generation.
* **Interactive UI:** A simple and intuitive web interface built with **Flask** and HTML/CSS for real-time interaction.
* **Automated CI/CD:** Continuous Integration pipeline using **GitHub Actions** to automatically lint, test, and scan the code before deployment.
* **Cloud Deployment:** Seamlessly deployed and scalable on the **Render** platform.

***
## 🛠️ Tech Stack

| Layer        | Technology                  |
|--------------|-----------------------------|
| Backend      | Python 3.11, LangChain      |
| LLM          | Groq                        |
| Vector Store | Pinecone                    |
| Frontend     | Flask                       |
| CI/CD        | GitHub Actions              |
| Deployment   | Render                      |

---

***
## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

* Python 3.10+
* A Pinecone account to get an API key and environment name.
* A Grok account to get an API key.

### 1. Clone the Repository

```bash
1. git clone [https://github.com/adityajayashankar/Med_Chatbot.git](https://github.com/adityajayashankar/Med_Chatbot.git)
   cd Med_Chatbot


2. Create a Virtual Environment
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate


3. Install Dependencies
   pip install -r requirements.txt


4. Set Up Environment Variables
   Create a file named .env in the root of the project directory and add your secret keys.

  Code snippet
  # .env.example
  PINECONE_API_KEY="YOUR_PINECONE_API_KEY"
  PINECONE_API_ENV="YOUR_PINECONE_ENVIRONMENT_NAME" # e.g., "gcp-starter"
  GROK_API_KEY="YOUR_GROK_API_KEY"

5. Data Ingestion (One-Time Setup)
  The Pinecone vector index needs to be populated with the knowledge from Medical_book.pdf.
  (Note: This implementation assumes the index is already created and populated. You can adapt the code in research/trials.ipynb or create a separate ingest.py        script to perform this one-time data ingestion.)

6. Run the Application
   Start the Flask server:

flask run
Open your web browser and navigate to http://127.0.0.1:5000 to start chatting with the bot!

```

## ☁️ Deployment
This application is configured for deployment on Render.<br>
The service is set to auto-deploy upon successful CI checks on the main branch, ensuring a smooth and automated deployment workflow.

You can access the live application here:
https://medical-chatbot-mc0g.onrender.com

## 🤖 CICD Pipeline
The Continuous Integration pipeline is configured in .github/workflows/ci.yml and performs the following checks on every push to the main branch:
Code Linting: Checks for code style and quality using flake8.
Unit & Integration Testing: Runs the test suite using pytest.

## 📝 License
This project is licensed under the Apache License 2.0. See the LICENSE file for more details.



## 🙌 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

## Developed by Aditya Jayashankar
📧 adityajayashankar@gmail.com
