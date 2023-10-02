import streamlit as st
import pandas as pd
import numpy as np

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

def delete_data_history():
  # Load the CSV data (assuming you have a CSV file named 'data.csv' with headers)
  df = pd.read_csv('./src/csv/history/history.csv')

  df_header = df.iloc[:0]

  # Save the updated DataFrame back to the CSV file (excluding the index)
  df_header.to_csv('./src/csv/history/history.csv', index=False)
  
# Function to display the history
def history():
  st.markdown("<h1 style='text-align: center; margin-bottom: 1em;'>Riwayat Analisis</h1>", unsafe_allow_html=True)
  data = pd.read_csv('./src/csv/history/history.csv')
  history_data = pd.DataFrame(data)
  st.dataframe(history_data)
  if st.button("Delete Data"):
    delete_data_history()