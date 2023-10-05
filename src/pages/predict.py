import streamlit as st
import cv2
import pandas as pd
import numpy as np
from sklearn import neighbors
from datetime import datetime

from src.pages.history import add_to_history
from src.pages.analysis import analysis_result
from src.pages.analysis import predict_leukocyte, predict_nitrit, predict_urobilinogen, predict_protein, predict_ph, predict_blood, predict_specificgravity, predict_ketone, predict_bilirubin, predict_glukosa

def rectangle(image):
    # draw rectangle into original image
    imgR = cv2.resize(image, (38, 638)) 
    cv2.rectangle(imgR, (25, 35), (10, 15), (0, 0, 255), 1)   # Parameter 1
    cv2.rectangle(imgR, (25, 85), (10, 65), (0, 0, 255), 1)   # Parameter 2
    cv2.rectangle(imgR, (25, 135), (10, 115), (0, 0, 255), 1) # Parameter 3
    cv2.rectangle(imgR, (25, 185), (10, 165), (0, 0, 255), 1) # Parameter 4
    cv2.rectangle(imgR, (25, 235), (10, 215), (0, 0, 255), 1) # Parameter 5
    cv2.rectangle(imgR, (25, 285), (10, 265), (0, 0, 255), 1) # Parameter 5
    cv2.rectangle(imgR, (25, 335), (10, 315), (0, 0, 255), 1) # Parameter 7
    cv2.rectangle(imgR, (25, 385), (10, 365), (0, 0, 255), 1) # Parameter 8
    cv2.rectangle(imgR, (25, 435), (10, 415), (0, 0, 255), 1) # Parameter 9
    cv2.rectangle(imgR, (25, 485), (10, 465), (0, 0, 255), 1) # Parameter 10

    return imgR

def process_dipstick(image):
    imS = cv2.resize(image, (38, 638))  # Resize the image

    #koordinat masing2 paramater uji
    crop_1=imS[15:35,10:25]     #Parameter 1()
    crop_2=imS[65:85,10:25]     #Parameter 2()
    crop_3=imS[115:135,10:25]   #Parameter 3()
    crop_4=imS[165:185,10:25]   #Parameter 4()
    crop_5=imS[215:235,10:25]   #Parameter 5()
    crop_6=imS[265:285,10:25]   #Parameter 6()
    crop_7=imS[315:335,10:25]   #Parameter 7()
    crop_8=imS[365:385,10:25]   #Parameter 8()
    crop_9=imS[415:435,10:25]   #Parameter 9()
    crop_10=imS[465:485,10:25]  #Parameter 10()
    koordinat = [crop_1, crop_2, crop_3, crop_4, crop_5, crop_6, crop_7, crop_8, crop_9, crop_10]

    # Define a dictionary to store parameter labels
    parameter_labels = {
        1: 'LEUKOSIT',
        2: 'NITRIT',
        3: 'UROBILINOGEN',
        4: 'PROTEIN',
        5: 'pH',
        6: 'BLOOD',
        7: 'SG',
        8: 'KETON',
        9: 'BILIRUBIN',
        10: 'GLUKOSA'
    }

    dipstick_result = {}

    for nomor, i in enumerate(koordinat, start=1):
        img = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)
    
        lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    
        inputLAB = cv2.mean(lab)

        xLAB = inputLAB[0]
        yLAB = inputLAB[1]
        zLAB = inputLAB[2]

        inputLAB = np.array([xLAB, yLAB, zLAB]).reshape(1, -1)

        data = pd.read_csv('./src/csv/crop/crop_' + str(nomor) + '.csv')  #

        xLAB = np.array(data[['l', 'a', 'b']])  ###
        yLAB = np.array(data[['hasil']])
        yLAB = np.array(yLAB.ravel())

        knnLAB = neighbors.KNeighborsClassifier(metric='manhattan', n_neighbors=1)

        knnLAB.fit(xLAB, yLAB)

        hasilLAB = knnLAB.predict(inputLAB).reshape(1, -1)

        parameter_label = parameter_labels[nomor]
        dipstick_result[parameter_label] = hasilLAB
        
    return dipstick_result

def pre_analysis():
    with st.expander("Ikuti langkah berikut ini untuk melakukan analisis"):
        st.write("""
                 1. Persiapkan Wadah Urin: Siapkan wadah urin yang bersih dan kering.
                 2. Kumpulkan Sampel: Ambil sampel urin ke dalam wadah. Pastikan jumlahnya cukup.
                 3. Celupkan Dipstick: Masukkan ujung strip tes urin (dipstick) ke dalam wadah urin.
                 4. Tunggu Sebentar: Biarkan selama beberapa detik sesuai petunjuk.
                 5. Scan: Foto hasil disptick urin dengan pencahayaan yang baik.
                 6. Upload: Kirim hanya foto dipstick urin yang telah dicrop.
                 """)

    agree = st.checkbox("Saya mengerti")


def dipstick_analysis():
    st.markdown("<h1 style='text-align: center; margin-bottom: 1em;'>Dipstick Urinalisis</h1>", unsafe_allow_html=True)

    with st.expander("Langkah-langkah melakukan analisis"):
        st.write("""
                1. **Persiapkan Wadah Urin:** Siapkan wadah urin yang bersih dan kering.
                2. **Kumpulkan Sampel:** Ambil sampel urin ke dalam wadah. Pastikan jumlahnya cukup.
                3. **Celupkan Dipstick:** Masukkan ujung strip tes urin (dipstick) ke dalam wadah urin.
                4. **Tunggu Sebentar:** Biarkan selama beberapa detik sesuai petunjuk agar dipstick bisa bereaksi dengan urin.
                5. **Scan:** Gunakan kamera ponsel untuk mengambil foto dipstick urin. Pastikan pencahayaan cukup baik.
                6. **Upload:** Unggah foto dipstick urin yang telah dicrop.
                """)

    agree = st.checkbox("Saya mengerti")

    if not agree:
        st.info("Pahami dan Ikuti lagkah-langkah diatas sebelum melakukan analisis")

    if agree:
        st.write("Unggah gambar dan dapatkan hasil analisis")

        uploaded_image = st.file_uploader("Pilih gambar", type=["jpg", "jpeg", "png"])

        if uploaded_image is not None:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            image = cv2.imdecode(np.frombuffer(uploaded_image.read(), np.uint8), 1)

            st.write("Hasil Analisis:")

            col1, col2 = st.columns([1, 10])

            
            with col1:
                # Process the image and draw rectangles
                image = rectangle(image)
            
                # Convert BGR image to RGB format
                rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                
                # Display the RGB image
                st.image(rgb_image)
                

            with col2:
                result = process_dipstick(image)

                add_to_history(result, image, current_time)

                # Create a DataFrame for the results
                result_df = pd.DataFrame(result.items(), columns=["Parameter", "Value"])
                result_df['Value'] = result_df['Value'].apply(lambda x: x[0][0])  # Extracting the value from the 2D array
                
                result_df['Keterangan'] = result_df.apply(lambda row: predict_leukocyte(row['Value'])[0] if row['Parameter'] == 'LEUKOSIT'
                                            else predict_nitrit(row['Value'])[0] if row['Parameter'] == 'NITRIT'
                                            else predict_urobilinogen(row['Value'])[0] if row['Parameter'] == 'UROBILINOGEN'
                                            else predict_protein(row['Value'])[0] if row['Parameter'] == 'PROTEIN'
                                            else predict_ph(row['Value'])[0] if row['Parameter'] == 'pH'
                                            else predict_blood(row['Value'])[0] if row['Parameter'] == 'BLOOD'
                                            else predict_specificgravity(row['Value'])[0] if row['Parameter'] == 'SG'
                                            else predict_ketone(row['Value'])[0] if row['Parameter'] == 'KETON'
                                            else predict_bilirubin(row['Value'])[0] if row['Parameter'] == 'BILIRUBIN'
                                            else predict_glukosa(row['Value'])[0] if row['Parameter'] == 'GLUKOSA'
                                            else "", axis=1)


                # Convert the 'Value' column to string
                result_df['Value'] = result_df['Value'].astype(str)
                
                result_df.index = result_df.index + 1
                
                st.table(result_df)

            analysis_result(result)

            st.info("Aplikasi ini hanya memberikan hasil prediksi. Disarankan untuk selalu berkonsultasi kepada ahli medis profesional.", icon="ℹ️")
        
        else:
            st.warning("Masukkan hanya gambar dipstick urin yang telah dicrop")
