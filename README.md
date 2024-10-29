# Text-to-SQL Application

This project is a Text-to-SQL application that converts natural language questions into SQL queries using Google's Gemini model and retrieves results from a MySQL database. It is built using Streamlit for the frontend, and leverages a custom `DB` class to interact with a MySQL database.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Environment Variables](#environment-variables)
- [Dependencies](#dependencies)
- [Acknowledgments](#acknowledgments)

---

## Overview

The application allows users to enter questions in plain English about football player stats. Using Google's Gemini-1.5 LLM model, it interprets these questions and generates SQL queries to retrieve data from a MySQL database table called `top_scorers`. The application is particularly useful for querying complex datasets without requiring SQL knowledge.

## Features

- **Natural Language Processing**: Converts natural language questions to SQL queries.
- **Database Query Execution**: Executes generated SQL queries on a local MySQL database and displays the results.
- **Streamlit Interface**: Interactive UI for entering questions and viewing results.
  
## Setup

### Prerequisites
- **Python 3.8+**
- **MySQL Database**: The data table (`top_scorers`) must exist with columns:
  - `Country`, `League`, `Club`, `Player Names`, `Matches_Played`, `Substitution`, `Mins`, `Goals`, `xG`, `xG Per Avg Match`, `Shots`, `OnTarget`, `Shots Per Avg Match`, `On Target Per Avg Match`, `Year`
- **Google API Key**: For accessing the Gemini LLM.

### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/text-to-sql.git
    cd text-to-sql
    ```

2. **Set Up Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Requirements**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Environment Variables**:
   Create a `.env` file in the root directory with the following content:
    ```env
    GOOGLE_API_KEY=your_google_api_key
    DB_PASSWORD=your_mysql_password
    ```

### Database Setup

Ensure that the MySQL database `football` contains a table `top_scorers` with the columns mentioned in the overview. The table must be locally accessible (host `localhost`, user `root`).

## Usage

1. **Run the Streamlit Application**:
    ```bash
    streamlit run app.py
    ```

2. **Interact with the App**:
    - Enter a question about player stats (e.g., "Who scored the most goals in 2022?")
    - Click **Generate SQL** to produce and execute the SQL query.
    - View the retrieved data in the table displayed on the page.

## Project Structure

```plaintext
text-to-sql/
├── app.py                   # Main Streamlit application
├── sql.py                   # DB class for database connection and querying
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── .env                     # Environment variables (not included in repo)
└── .gitignore               # Files and directories to ignore in Git
```

## Environment Variables

- `GOOGLE_API_KEY`: Your API key for Google’s Gemini model.
- `DB_PASSWORD`: Password for the MySQL database.

These should be stored in a `.env` file in the root of your project.

## Dependencies

Listed in `requirements.txt.` Main dependencies:

- `streamlit`: For the web interface
- `pandas`: Data handling and DataFrame creation
- `pymysql`: MySQL database connectivity
- `google-generativeai`: Access to Google’s Gemini LLM API
- `python-dotenv`: Loading environment variables from .env file

## Acknowledgments

- **Google** for providing the Gemini model for LLM capabilities.
- **Streamlit** for an interactive UI that makes it easy to work with ML-based applications.
- The open-source community for continued support and resources.
