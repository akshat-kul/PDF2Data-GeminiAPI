# Create-Paper---Extract-Info---ZuAI-Task
The Sample Paper Management System is a FastAPI application designed to create, retrieve, update, and delete sample papers for academic purposes. The application allows users to store paper details in a MongoDB database and interact with these records through a RESTful API.

## Features

- **Extract Information from PDF Files**: Utilize the Gemini API to extract relevant details from PDF files and store them in the papers collection.
- **Extract Information from Plain Text**: Use the Gemini API to extract information from plain text prompts, then store the data in the papers collection.
- **Task Management**: Use task IDs to fetch details of ongoing, failed, or completed tasks related to paper creation and processing.
- **Create a Sample Paper**: Add new sample papers by sending JSON data including title, type, time, marks, parameters, tags, chapters, and sections.
- **Retrieve a Sample Paper**: Get details of a specific paper by its ID.
- **Update a Sample Paper**: Modify the details of an existing paper.
- **Delete a Sample Paper**: Remove a paper from the database.

## Technologies Used

- **FastAPI**: For building the RESTful API.
- **MongoDB**: For storing sample paper data.
- **Pydantic**: For data validation and serialization.
- **Redis**: Used for caching GET operations to improve performance.
- **Gemini API**: Utilized for extracting information from PDF files and plain text.
- **pytest**: For testing the API endpoints.

## Getting Started

To run this project locally, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/akshat-kul/Create-Paper---Extract-Info---ZuAI-Task.git
cd <repository_name>
```

### 2. Set up the virtual environment

```bash
Install the virtualenv library, if installed then Create virtual environment using
virtualenv venv
Then activate it using:
On Windows
venv/Scripts/activate

On Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Up MongoDB Ensure you have MongoDB installed and running. You can set up a local instance or use a cloud service like MongoDB Atlas.

### 3. Run the App

```bash
python main.py
```
