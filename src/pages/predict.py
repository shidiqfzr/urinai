import streamlit as st
import cv2
import pandas as pd
import numpy as np
from sklearn import neighbors

def predict_leukocyte(leukocyte_result):
    if leukocyte_result == "NEGATIF":
        return "Tidak ada kadar sel darah putih yang signifikan (normal)"
    elif leukocyte_result == "+/-":
        return "Konsentrasi leukosit sangat kecil, mungkin menunjukkan infeksi ringan atau respons peradangan ringan"
    elif leukocyte_result == "+":
        return "Terdapat konsentrasi leukosit yang lebih tinggi dalam urine, mungkin menandakan adanya infeksi atau peradangan dalam saluran kemih"
    elif leukocyte_result == "++":
        return "Peningkatan sedang pada jumlah leukosit dalam urine, mengindikasikan potensi infeksi atau peradangan yang lebih signifikan"
    elif leukocyte_result == "+++":
        return "Konsentrasi leukosit yang tinggi dalam urine, mengindikasikan respons peradangan yang kuat atau infeksi yang mungkin serius"
    
def predict_nitrit(nitrit_result):
    if nitrit_result == "NEGATIF":
        return "Tidak ada deteksi nitrit dalam urine. Hasil ini normal dan menunjukkan bahwa tidak ada tanda-tanda infeksi saluran kemih atau masalah lain yang terkait dengan nitrit dalam urine."
    else:
        return "Terindentifikasi nitrit dalam urine. Kehadiran nitrit dalam urine dapat menjadi petunjuk adanya infeksi bakteri tertentu dalam saluran kemih, seperti infeksi saluran kemih atas atau infeksi kandung kemih. Nitrit dapat terbentuk dalam urine ketika bakteri mengubah nitrat menjadi nitrit."

def predict_urobilinogen(urobilinogrn_result):
    if urobilinogrn_result == "0.2 (Neg)":
        return "Tidak ada atau kadar sangat rendah urobilinogen dalam urine, menunjukkan kesehatan normal dalam hal metabolisme bilirubin."
    elif urobilinogrn_result == "1 (Neg)":
        return "Tidak ada atau kadar sangat rendah urobilinogen dalam urine, merupakan hasil normal dalam hal metabolisme bilirubin."
    elif urobilinogrn_result == "2 (Pos)":
        return "Terindentifikasi adanya kadar urobilinogen yang sedikit lebih tinggi dalam urine, dapat disebabkan oleh beberapa faktor seperti metabolisme bilirubin yang lebih tinggi atau interaksi dengan obat-obatan tertentu."
    elif urobilinogrn_result == "4 (Pos)":
        return "Peningkatan lebih lanjut pada kadar urobilinogen dalam urine, terindentifikasi adanya faktor yang lebih signifikan yang mempengaruhi metabolisme bilirubin."
    elif urobilinogrn_result == "8 (Pos)":
        return "Konsentrasi urobilinogen yang lebih tinggi dalam urine, menunjukkan masalah yang lebih serius dalam metabolisme bilirubin atau masalah hati."
    elif urobilinogrn_result == "12 (Pos)":
        return "Konsentrasi urobilinogen yang tinggi dalam urine, bisa menjadi tanda masalah serius dalam metabolisme bilirubin atau gangguan hati yang perlu penanganan medis lebih lanjut."

def predict_protein(protein_result):
    if protein_result == "NEGATIF":
        return " Biasanya, urin sehat tidak mengandung jumlah protein yang tinggi."
    elif protein_result == "+/-":
        return "Terindentifikasi adanya protein, masih dapat dianggap sebagai tanda kecil proteinuria."
    elif protein_result == "+":
        return "Terindentifikasi adanya proteinuria ringan, yang dapat terjadi dalam beberapa situasi, termasuk setelah aktivitas fisik intens atau demam."
    elif protein_result == "++":
        return "Terindentifikasi adanya konsentrasi protein yang lebih tinggi dalam urin. Ini mungkin mengindikasikan adanya masalah kesehatan, seperti infeksi saluran kemih, tekanan darah tinggi, atau gangguan ginjal awal."
    elif protein_result == "+++":
        return "Terindentifikasi tingkat protein yang lebih tinggi lagi dalam urin. Ini dapat mengindikasikan kondisi kesehatan yang lebih serius, seperti kerusakan ginjal yang lebih lanjut atau penyakit ginjal yang berpotensi lebih kompleks."
    elif protein_result == "++++":
        return "Terindentifikasi serius dari masalah ginjal atau masalah kesehatan lainnya yang memengaruhi fungsi ginjal."

def predict_ph(ph_result):
    if ph_result == "5,0":
        return "pH sangat asam, mengindikasikan potensi masalah medis atau masalah diet tertentu."
    elif ph_result == "6,0":
        return "pH urin cenderung sedikit asam, tetapi masih berada dalam kisaran normal. Ini adalah kondisi umum dan biasanya tidak menimbulkan kekhawatiran besar."
    elif ph_result == "6,5":
        return "pH urin cenderung sedikit asam, tetapi masih berada dalam kisaran normal. Ini adalah kondisi umum dan biasanya tidak menimbulkan kekhawatiran besar."
    elif ph_result == "7,0":
        return "pH urin netral. Ini adalah kondisi yang dianggap normal. Sebagian besar orang memiliki pH urin sekitar 6.0 hingga 7.5."
    elif ph_result == "7,5":
        return "pH urin cenderung sedikit basa (alkalis). Ini masih berada dalam kisaran normal dan umumnya tidak menjadi masalah."
    elif ph_result == "8,0":
        return "pH urin cenderung sedikit basa (alkalis). Ini masih berada dalam kisaran normal dan umumnya tidak menjadi masalah."
    elif ph_result == "9,0":
        return "pH urin sangat basa. Seperti pH urin yang sangat asam, kondisi ini juga jarang terjadi dalam keadaan normal dan dapat mengindikasikan potensi masalah medis atau faktor diet yang ekstrem."

def predict_blood(blood_result):
    if blood_result == "NEGATIF":
        return "Tidak ada deteksi darah yang signifikan dalam urin. Ini mengindikasikan bahwa urin tidak mengandung darah dalam jumlah yang dapat dideteksi oleh tes ini."
    elif blood_result == "+/-":
        return "Menunjukkan adanya sedikit jumlah darah dalam urin. Ini bisa mengindikasikan adanya jejak darah, tetapi jumlahnya sangat kecil sehingga tidak terlihat secara visual."
    elif blood_result == "+":
        return "Ini menunjukkan adanya darah dalam urin dalam jumlah sedikit. Ini bisa mengindikasikan adanya masalah seperti infeksi saluran kemih, batu ginjal, atau masalah lainnya yang mempengaruhi saluran kemih atau sistem ginjal."
    elif blood_result == "++":
        return "Ini menunjukkan adanya jumlah darah yang lebih besar dalam urin. Ini bisa mengindikasikan masalah yang lebih serius, seperti peradangan ginjal, infeksi yang lebih parah, atau gangguan ginjal lainnya."
    elif blood_result == "+++":
        return "Ini menunjukkan konsentrasi darah yang lebih tinggi lagi dalam urin. Ini bisa mengindikasikan kondisi yang lebih serius, seperti kerusakan ginjal yang signifikan atau masalah lain yang mempengaruhi sistem kemih."
    elif blood_result == "5-10":
        return "Ini menunjukkan jumlah sel darah merah yang cukup banyak"
    elif blood_result == "50":
        return "Jumlah darah ini mengindikasikan jumlah yang lebih tinggi dalam urin, yang dapat mengindikasikan masalah yang lebih serius. Kemungkinan penyebab mungkin termasuk infeksi saluran kemih yang lebih parah, peradangan yang signifikan pada ginjal atau saluran kemih, batu ginjal yang lebih besar atau menyebabkan kerusakan, cedera pada ginjal, atau masalah darah yang mempengaruhi aliran darah ke ginjal. Angka ini mengarah pada potensi masalah yang memerlukan penanganan medis lebih lanjut untuk mengidentifikasi penyebab dan merencanakan tindakan yang sesuai."

def predict_specificgravity(specificgravity_result):
    if specificgravity_result == 1000:
        return "Ini menunjukkan urin yang sangat encer, dan bisa mengindikasikan bahwa seseorang mungkin dalam kondisi yang sangat terhidrasi."
    elif specificgravity_result == 1005:
        return "Ini masih dianggap urin yang encer, dan bisa mengindikasikan kondisi di mana seseorang cukup terhidrasi."
    elif specificgravity_result == 1010:
        return "Ini mengindikasikan urin yang cukup encer, tetapi mulai sedikit lebih pekat daripada sebelumnya. Ini mungkin menunjukkan bahwa seseorang memiliki keseimbangan cairan yang cukup baik."
    elif specificgravity_result == 1015:
        return "Ini bisa mengindikasikan bahwa seseorang sedang dalam kondisi normal dalam hal keseimbangan cairan."
    elif specificgravity_result == 1020:
        return "Ini bisa mengindikasikan bahwa seseorang mungkin sedang dalam keadaan normal tetapi sedikit terhidrasi."
    elif specificgravity_result == 1025:
        return "Ini mungkin mengindikasikan bahwa seseorang sedang mengalami dehidrasi ringan atau memiliki konsentrasi zat terlarut dalam urin yang lebih tinggi."
    elif specificgravity_result == 1030:
        return "Ini bisa mengindikasikan dehidrasi yang lebih serius atau kondisi medis yang memengaruhi keseimbangan cairan dan elektrolit."

def predict_ketone(ketone_result):
    if ketone_result == "NEGATIF":
        return "Ini mengindikasikan bahwa urin tidak mengandung keton. Ini adalah hasil dalam keadaan normal."
    elif ketone_result == "+/-":
        return "Ini bisa mengindikasikan bahwa tubuh mungkin sedang memecah lemak untuk energi, tetapi level keton masih dalam kisaran normal atau rendah."
    elif ketone_result == "+":
        return "Ini bisa mengindikasikan bahwa tubuh sedang memproduksi lebih banyak keton sebagai sumber energi, dan ini mungkin terkait dengan diet rendah karbohidrat, puasa, atau keadaan lain yang mempengaruhi metabolisme lemak."
    elif ketone_result == "++":
        return "Ini bisa mengindikasikan peningkatan yang lebih signifikan dalam produksi keton dalam tubuh dan dapat mengindikasikan kondisi seperti ketoasidosis ringan."
    elif ketone_result == "+++":
        return "Ini dapat mengindikasikan peningkatan yang lebih signifikan dalam produksi keton dan mungkin menunjukkan kondisi seperti ketoasidosis yang lebih parah."
    elif ketone_result == "++++":
        return "Ini adalah indikasi serius dan dapat mengindikasikan ketoasidosis yang signifikan, yang memerlukan penanganan medis segera."
    
def predict_bilirubin(bilirubin_result):
    if bilirubin_result == "NEGATIF":
        return "Ini mengindikasikan bahwa urin tidak mengandung bilirubin, Biasanya, bilirubin tidak ditemukan dalam urin karena memang normalnya tidak ada."
    elif bilirubin_result == "+":
        return "Ini bisa mengindikasikan adanya masalah dalam hati atau saluran empedu, yang dapat mengakibatkan peningkatan kadar bilirubin dalam darah dan kemudian muncul dalam urin."
    elif bilirubin_result == "++":
        return "Ini dapat mengindikasikan masalah yang lebih serius dalam hati atau saluran empedu yang mempengaruhi kemampuan mereka untuk memproses bilirubin dengan baik."
    elif bilirubin_result == "+++":
        return "Ini menunjukkan konsentrasi bilirubin yang lebih tinggi lagi dalam urin. Ini bisa mengindikasikan masalah yang lebih serius dalam hati atau saluran empedu yang memerlukan perhatian medis lebih lanjut."

def predict_glukosa(glukosa_result):
    if glukosa_result == "NEGATIF":
        return "Ini mengindikasikan bahwa urin tidak mengandung glukosa. Biasanya, glukosa tidak ditemukan dalam urin sehat."
    elif glukosa_result == "+/-":
        return "Ini bisa mengindikasikan bahwa kadar glukosa dalam darah mungkin sedikit meningkat, tetapi masih dalam kisaran normal."
    elif glukosa_result == "+":
        return "Ini menunjukkan adanya glukosa dalam urin dalam jumlah terdeteksi. Ini bisa mengindikasikan bahwa kadar glukosa dalam darah mungkin lebih tinggi dari biasanya. Hal ini dapat terjadi pada kondisi seperti diabetes."
    elif glukosa_result == "++":
        return "Ini dapat mengindikasikan peningkatan yang lebih signifikan dalam kadar glukosa darah, yang bisa menunjukkan masalah seperti diabetes yang lebih serius."
    elif glukosa_result == "+++":
        return "Ini bisa mengindikasikan peningkatan yang lebih signifikan lagi dalam kadar glukosa darah, dan memerlukan evaluasi medis lebih lanjut."
    elif glukosa_result == "++++":
        return "Ini mengindikasikan adanya kadar glukosa darah yang sangat tinggi, yang bisa sangat serius dan mengindikasikan kondisi diabetes yang perlu ditangani dengan cepat."


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

def dipstick_analysis():
    st.markdown("<h1 style='text-align: center; margin-bottom: 1em;'>Dipstick Urinalisis</h1>", unsafe_allow_html=True)
    st.write("Unggah gambar dan dapatkan hasil analisis")

    uploaded_image = st.file_uploader("Pilih gambar", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
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

            # Create a DataFrame for the results
            result_df = pd.DataFrame(result.items(), columns=["Parameter", "Value"])
            result_df['Value'] = result_df['Value'].apply(lambda x: x[0][0])  # Extracting the value from the 2D array

            # data = get_result_df(result_df)
            
            result_df['Keterangan'] = result_df.apply(lambda row: predict_leukocyte(row['Value']) if row['Parameter'] == 'LEUKOSIT'
                                          else predict_nitrit(row['Value']) if row['Parameter'] == 'NITRIT'
                                          else predict_urobilinogen(row['Value']) if row['Parameter'] == 'UROBILINOGEN'
                                          else predict_protein(row['Value']) if row['Parameter'] == 'PROTEIN'
                                          else predict_ph(row['Value']) if row['Parameter'] == 'pH'
                                          else predict_blood(row['Value']) if row['Parameter'] == 'BLOOD'
                                          else predict_specificgravity(row['Value']) if row['Parameter'] == 'SG'
                                          else predict_ketone(row['Value']) if row['Parameter'] == 'KETON'
                                          else predict_bilirubin(row['Value']) if row['Parameter'] == 'BILIRUBIN'
                                          else predict_glukosa(row['Value']) if row['Parameter'] == 'GLUKOSA'
                                          else "", axis=1)


            # Convert the 'Value' column to string
            result_df['Value'] = result_df['Value'].astype(str)
            
            result_df.index = result_df.index + 1
            
            st.table(result_df)

        st.info("Aplikasi ini hanya memberikan hasil prediksi. Disarankan untuk selalu berkonsultasi kepada ahli medis profesional.", icon="ℹ️")
    
    else:
        st.warning("Masukkan hanya gambar dipstick urin yang telah dicrop")
