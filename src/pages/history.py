import streamlit as st
import pandas as pd
import numpy as np

def add_to_history(result, image, time):
  data = pd.read_csv('./src/csv/history/history.csv')

  result_df = pd.DataFrame(result.items(), columns=["Parameter", "Value"])
  result_df['Value'] = result_df['Value'].apply(lambda x: x[0][0])
  result_df = result_df.T
  result_df.columns = result_df.iloc[0]
  result_df = result_df[1:]
  result_df.insert(0, 'Times', time)

  # Concatenate the existing DataFrame with the new data DataFrame, excluding the "time" column from new_data
  updated_data = pd.concat([data, result_df], ignore_index=True)

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
  if st.button("Hapus Riwayat"):
    delete_data_history()