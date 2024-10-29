import streamlit as st
import google.generativeai as genai
import os
from sql import DB
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Configure the Google Generative AI with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize database connection and generative model
db = DB()
model = genai.GenerativeModel('gemini-1.5-pro-exp-0801')


def getGeminiResponse(question: str, prompt: str) -> str:
    """
    Generate SQL query from a natural language question using the Google Gemini model.

    Parameters:
        question (str): The user input question in natural language.
        prompt (str): The instructional prompt provided to guide the model.

    Returns:
        str: Generated SQL query in text format.
    """
    try:
        # Generate SQL content based on question and prompt
        response = model.generate_content([question, prompt])
        return response.text
    except Exception as e:
        st.error(f"Failed to generate response from model: {e}")
        return ""


# Define the SQL generation prompt with instructions and column details
prompt = '''
    You are provided with a table containing the following columns: 'Country', 'League', 'Club', 'Player Names', 
    'Matches_Played', 'Substitution', 'Mins', 'Goals', 'xG', 'xG Per Avg Match', 'Shots', 'OnTarget', 
    'Shots Per Avg Match', 'On Target Per Avg Match', 'Year'. Whenever you find a column name that contains a ' ' 
    (space or multiple spaces), put it inside backticks (`column name`) while performing SELECT. For example, 
    'xG Per Avg Match' will be `xG Per Avg Match`. Given a question in natural language, your task is to interpret 
    the question and create an SQL query that will retrieve the desired information from this table.

    Remember one thing - the name of the table is top_scorers. The SQL query should:

    Directly address the user’s question by selecting, filtering, or aggregating the appropriate columns.
    Use efficient filtering if specific conditions are requested, such as particular players, countries, leagues, 
    or years.
    Avoid unnecessary columns or tables that are not directly relevant to the question.
    Exclude any commentary or formatting markers such as '```' and the word 'sql'.
    If you don't get the answer, just say that you don't know.

    Ensure the generated SQL query matches this format directly.
'''

# Streamlit app setup
st.set_page_config(page_title="Text to SQL", page_icon=":robot:")
st.header("Text to SQL")

# Text area for user input question
question = st.text_area("Input:", key='input')

# Button to generate SQL query
btn = st.button("Generate SQL")

if btn:
    # Get SQL query from model response
    response = getGeminiResponse(question, prompt)

    if response:
        try:
            # Query the database with the generated SQL
            df = db.query(response)

            # Display results in a DataFrame
            st.dataframe(df)
        except Exception as e:
            st.error(f"Database query failed: {e}")