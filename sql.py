import pandas as pd
import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()


class DB:
    """
    A database interface class for connecting to and querying a MySQL database.

    This class uses pymysql to connect to a MySQL database and retrieve query results in the form of a pandas DataFrame.
    """

    def __init__(self):
        """
        Initializes a connection to the MySQL database using environment variables.

        The database credentials, such as password, are securely retrieved from environment variables.
        """
        try:
            # Establish the database connection
            self.conn = pymysql.connect(
                host="localhost",
                user="root",
                password=os.getenv("DB_PASSWORD"),
                database="football"
            )
            self.mycursor = self.conn.cursor()
            # print("Connection established successfully.")

        except pymysql.MySQLError as e:
            print(f"Connection failed! MySQL error: {e}")

        except Exception as e:
            print(f"Connection failed! General error: {e}")

    def query(self, sql_query: str) -> pd.DataFrame:
        """
        Executes an SQL query and returns the results as a pandas DataFrame.

        Parameters:
            sql_query (str): The SQL query to execute.

        Returns:
            pd.DataFrame: A DataFrame containing the results of the query.
        """
        try:
            # Execute the SQL query
            self.mycursor.execute(sql_query)

            # Fetch all rows of query result
            data = self.mycursor.fetchall()

            # Get column names from the cursor description
            cols = [desc[0] for desc in self.mycursor.description]

            # Convert the result into a DataFrame
            df = pd.DataFrame(data, columns=cols)

            return df

        except pymysql.MySQLError as e:
            print(f"Query failed! MySQL error: {e}")
            return pd.DataFrame()  # Return empty DataFrame on error

        except Exception as e:
            print(f"Query failed! General error: {e}")
            return pd.DataFrame()  # Return empty DataFrame on error

        finally:
            # Optional: Close the cursor if query execution is complete
            self.mycursor.close()