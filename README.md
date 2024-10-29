# Chat With PDF
================

A project that enables users to chat with PDF files.

## Description
---------------

This project aims to provide a innovative way of interacting with PDF files by allowing users to chat with them.

## Prerequisites 
--------------------
1. `Python 3.10` 
2. `flask` 
3. `PyPDF2`
4. `pinecone` 
5. `firebase_admin`
6. `python-dotenv`
7. `google-generativeai` 
8. `langchain`
9. `langchain-google-genai` 
10. `profanity-check` 

## Getting Started
-------------------

To get started with the project, follow these steps:

1. Clone the repository: `git clone https://github.com/Atiqur78/Chat_With_Pdf.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Create .env file and write the required `PINCONE_API_KEY | FIREBASE_API_KEY`
4. Run the application: `python main.py`
5. Using UI interface upload the `.pdf` file and ask the `Query` related to pdf


## Api Testing
------------

document_upload: `curl -X POST -F "chat_name=your_chat_name" -F "file=@path_to_your_file.pdf" http://localhost:5000/upload`


query: `curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "query_chat_name=your_chat_name&question=your_question" http://localhost:5000/query`


Video Link : https://drive.google.com/file/d/1ktCYGWvk9gwHBMXv6f8MBh4VSP-3Kxuz/view?usp=sharing

## Authors
-----------

* [Atiqur Rahman]