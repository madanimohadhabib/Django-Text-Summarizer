# Automatic Text Summarizer

This project is a Django-based web application that allows users to generate automatic summaries of long texts. Users can input text into a form, and the application processes it to generate a concise summary using Natural Language Processing (NLP) techniques.

## Features

- Input text through a simple form.
- Generate a summary of the text automatically.
- Display the summarized text on the same page.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML/CSS
- **NLP Model**: Transformers library (Hugging Face)
- **Dependencies**: TensorFlow or PyTorch, Hugging Face Transformers

## Installation

Follow these steps to set up the project on your local machine:

1. Step 1: Clone the repository:
   ```bash
   git clone https://github.com/madanimohadhabib/Django-Text-Summarizer
   cd Django-Text-Summarizer

2. Step 2: Create a virtual environment:    
    - **For Linux/MacOS**:
        ```bash
        python3 -m venv env
        source env/bin/activate
    - **For Windows**: 
        ```bash
        python3 -m venv env
        env\Scripts\activate

3. Step 3: Install the required dependencies:
    ```bash 
    pip install -r requirements.txt

4. Step 4: Make migrations and start the server
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

5. Step 5: Access the application:
Open your browser and navigate to http://127.0.0.1:8000/