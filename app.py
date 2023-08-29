import cv2
import numpy as np
import pandas as pd
import streamlit as st

from src.python.predict import rectangle, process_dipstick

hide_st_style = """ 
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True) # hide streamlit menu
    
def main():
    st.markdown("<h1 style='text-align: center; margin-bottom: 1em;'>Dipstick Analysis</h1>", unsafe_allow_html=True)
    st.write("Unggah gambar dan dapatkan hasil")

    uploaded_image = st.file_uploader("Pilih gambar...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = cv2.imdecode(np.frombuffer(uploaded_image.read(), np.uint8), 1)

        col1, col2 = st.columns([1, 4])
        
        with col1:
            # Process the image and draw rectangles
            image = rectangle(image)
        
            # Convert BGR image to RGB format
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            # Display the RGB image
            st.image(rgb_image)
            

        with col2:
            result = process_dipstick(image)
            st.write("Results:")

            # Create a DataFrame for the results
            result_df = pd.DataFrame(result.items(), columns=["Parameter", "Value"])
            result_df['Value'] = result_df['Value'].apply(lambda x: x[0][0])  # Extracting the value from the 2D array
            
            # Convert the 'Value' column to string
            result_df['Value'] = result_df['Value'].astype(str)

            # Add 'Keterangan' column based on the parameter's value
            result_df['Keterangan'] = ""

            for idx, row in result_df.iterrows():
                param = row['Parameter']
                value = row['Value']

                # if param == "LEUKOSIT":
                #     result_df.at[idx, 'Keterangan'] = predict_leukocyte(value)
                # elif param == "NITRIT":
                #     result_df.at[idx, 'Keterangan'] = predict_nitrit(value)
                # elif param == "UROBILINOGEN":
                #     result_df.at[idx, 'Keterangan'] = predict_urobilinogen(value)
                # Add conditions for other parameters here

            result_df.index = result_df.index + 1
            st.dataframe(result_df)
    
    else:
        st.warning("Masukkan hanya gambar dipstick yang telah dicrop")

if __name__ == "__main__":
    main()