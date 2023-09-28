import streamlit as st
import pandas as pd
import numpy as np

def parsing_result(result):
    formatted_data = []

    # Iterate through the dictionary and format the data
    for key, value in result.items():
        # Extract the value from the nested array
        if isinstance(value, np.ndarray):
            value = value[0][0]
        
        formatted_data.append(f"{key}: {value}\n")

    # Convert the formatted data to a single string
    formatted_string = "\n".join(formatted_data)

    print(formatted_string)
    return formatted_string

def add_to_history(result, image, time):
  data = pd.read_csv('./src/csv/history/history.csv')

  df = pd.DataFrame(result.items()).T
  df.columns = df.iloc[0]
  df = df[1:]
  df = df.apply(lambda x: x.str[0] if x.dtype == 'object' else x)
  df.insert(0, 'Times', time)

  # Concatenate the existing DataFrame with the new data DataFrame, excluding the "time" column from new_data
  updated_data = pd.concat([data, df], ignore_index=True)

  # Save the updated data back to the CSV file without index column
  updated_data.to_csv('./src/csv/history/history.csv', index=False)
  
# Function to display the history
def history():
  st.title("History")
  data = pd.read_csv('./src/csv/history/history.csv')
  history_data = pd.DataFrame(data)
  st.table(history_data)