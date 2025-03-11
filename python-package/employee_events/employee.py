# Import the QueryBase class
#### YOUR CODE HERE

from query_base import QueryBase

# Import dependencies needed for sql execution
# from the `sql_execution` module
#### YOUR CODE HERE
from sqlite3 import connect
import pandas as pd

# Define a subclass of QueryBase
# called Employee
#### YOUR CODE HERE
class Employee(QueryBase):

    # Set the class attribute `name`
    # to the string "employee"
    #### YOUR CODE HERE
    name = "employee"

    # Define a method called `names`
    # that receives no arguments
    # This method should return a list of tuples
    # from an sql execution
    #### YOUR CODE HERE
    def names(self):
        
        # Query 3
        # Write an SQL query
        # that selects two columns 
        # 1. The employee's full name
        # 2. The employee's id
        # This query should return the data
        # for all employees in the database
        #### YOUR CODE HERE
        query = """
                SELECT first_name || ' ' || last_name AS full_name, employee_id
                FROM employee
                """
        connection = connect("employee_events.db")
        cursor = connection.cursor()
        result = cursor.execute(query).fetchall()
        connection.close()
        return result

    # Define a method called `username`
    # that receives an `id` argument
    # This method should return a list of tuples
    # from an sql execution
    #### YOUR CODE HERE
    def username(self, id):
        
        # Query 4
        # Write an SQL query
        # that selects an employees full name
        # Use f-string formatting and a WHERE filter
        # to only return the full name of the employee
        # with an id equal to the id argument
        #### YOUR CODE HERE
        query = f"""
                SELECT first_name || ' ' || last_name AS full_name
                FROM employee
                WHERE employee_id = {id}
                """
        connection = connect("employee_events.db")
        cursor = connection.cursor()
        result = cursor.execute(query).fetchall()
        connection.close()
        return result

    # Below is method with an SQL query
    # This SQL query generates the data needed for
    # the machine learning model.
    # Without editing the query, alter this method
    # so when it is called, a pandas dataframe
    # is returns containing the execution of
    # the sql query
    #### YOUR CODE HERE
    def model_data(self, id):
        query = f"""
                SELECT SUM(positive_events) positive_events
                     , SUM(negative_events) negative_events
                FROM {self.name}
                JOIN employee_events
                    USING({self.name}_id)
                WHERE {self.name}.{self.name}_id = {id}
                """

        # Execute the query and return the result as a pandas DataFrame
        connection = connect("employee_events.db")
        df = pd.read_sql_query(query, connection)
        connection.close()
        return df