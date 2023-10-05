import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def predict_leukocyte(leukocyte_result):
    if leukocyte_result == "NEGATIF":
        return ["Tidak ada kadar sel darah putih yang signifikan (normal)", 1]
    elif leukocyte_result == "+/-":
        return ["Konsentrasi leukosit sangat kecil, mungkin menunjukkan infeksi ringan atau respons peradangan ringan", 1]
    elif leukocyte_result == "+":
        return ["Terdapat konsentrasi leukosit yang lebih tinggi dalam urine, mungkin menandakan adanya infeksi atau peradangan dalam saluran kemih", 0]
    elif leukocyte_result == "++":
        return ["Peningkatan sedang pada jumlah leukosit dalam urine, mengindikasikan potensi infeksi atau peradangan yang lebih signifikan", 0]
    elif leukocyte_result == "+++":
        return ["Konsentrasi leukosit yang tinggi dalam urine, mengindikasikan respons peradangan yang kuat atau infeksi yang mungkin serius", 0]
    
def predict_nitrit(nitrit_result):
    if nitrit_result == "NEGATIF":
        return ["Tidak ada deteksi nitrit dalam urine. Hasil ini normal dan menunjukkan bahwa tidak ada tanda-tanda infeksi saluran kemih atau masalah lain yang terkait dengan nitrit dalam urine.", 1]
    else:
        return ["Terindentifikasi nitrit dalam urine. Kehadiran nitrit dalam urine dapat menjadi petunjuk adanya infeksi bakteri tertentu dalam saluran kemih, seperti infeksi saluran kemih atas atau infeksi kandung kemih. Nitrit dapat terbentuk dalam urine ketika bakteri mengubah nitrat menjadi nitrit.", 0]

def predict_urobilinogen(urobilinogen_result):
    if urobilinogen_result == "0.2 (Neg)":
        return ["Tidak ada atau kadar sangat rendah urobilinogen dalam urine, menunjukkan kesehatan normal dalam hal metabolisme bilirubin.", 1]
    elif urobilinogen_result == "1 (Neg)":
        return ["Tidak ada atau kadar sangat rendah urobilinogen dalam urine, merupakan hasil normal dalam hal metabolisme bilirubin.", 1]
    elif urobilinogen_result == "2 (Pos)":
        return ["Terindentifikasi adanya kadar urobilinogen yang sedikit lebih tinggi dalam urine, dapat disebabkan oleh beberapa faktor seperti metabolisme bilirubin yang lebih tinggi atau interaksi dengan obat-obatan tertentu.", 0]
    elif urobilinogen_result == "4 (Pos)":
        return ["Peningkatan lebih lanjut pada kadar urobilinogen dalam urine, terindentifikasi adanya faktor yang lebih signifikan yang mempengaruhi metabolisme bilirubin.", 0]
    elif urobilinogen_result == "8 (Pos)":
        return ["Konsentrasi urobilinogen yang lebih tinggi dalam urine, menunjukkan masalah yang lebih serius dalam metabolisme bilirubin atau masalah hati.", 0]
    elif urobilinogen_result == "12 (Pos)":
        return ["Konsentrasi urobilinogen yang tinggi dalam urine, bisa menjadi tanda masalah serius dalam metabolisme bilirubin atau gangguan hati yang perlu penanganan medis lebih lanjut.", 0]

def predict_protein(protein_result):
    if protein_result == "NEGATIF":
        return ["Biasanya, urin sehat tidak mengandung jumlah protein yang tinggi.", 1]
    elif protein_result == "+/-":
        return ["Terindentifikasi adanya protein, masih dapat dianggap sebagai tanda kecil proteinuria.", 1]
    elif protein_result == "+":
        return ["Terindentifikasi adanya proteinuria ringan, yang dapat terjadi dalam beberapa situasi, termasuk setelah aktivitas fisik intens atau demam.", 0]
    elif protein_result == "++":
        return ["Terindentifikasi adanya konsentrasi protein yang lebih tinggi dalam urin. Ini mungkin mengindikasikan adanya masalah kesehatan, seperti infeksi saluran kemih, tekanan darah tinggi, atau gangguan ginjal awal.", 0]
    elif protein_result == "+++":
        return ["Terindentifikasi tingkat protein yang lebih tinggi lagi dalam urin. Ini dapat mengindikasikan kondisi kesehatan yang lebih serius, seperti kerusakan ginjal yang lebih lanjut atau penyakit ginjal yang berpotensi lebih kompleks.", 0]
    elif protein_result == "++++":
        return ["Terindentifikasi serius dari masalah ginjal atau masalah kesehatan lainnya yang memengaruhi fungsi ginjal.", 0]

def predict_ph(ph_result):
    if ph_result == "5,0":
        return ["pH sangat asam, mengindikasikan potensi masalah medis atau masalah diet tertentu.", 1]
    elif ph_result == "6,0":
        return ["pH urin cenderung sedikit asam, tetapi masih berada dalam kisaran normal. Ini adalah kondisi umum dan biasanya tidak menimbulkan kekhawatiran besar.", 1]
    elif ph_result == "6,5":
        return ["pH urin cenderung sedikit asam, tetapi masih berada dalam kisaran normal. Ini adalah kondisi umum dan biasanya tidak menimbulkan kekhawatiran besar.", 0]
    elif ph_result == "7,0":
        return ["pH urin netral. Ini adalah kondisi yang dianggap normal. Sebagian besar orang memiliki pH urin sekitar 6.0 hingga 7.5.", 0]
    elif ph_result == "7,5":
        return ["pH urin cenderung sedikit basa (alkalis). Ini masih berada dalam kisaran normal dan umumnya tidak menjadi masalah.", 0]
    elif ph_result == "8,0":
        return ["pH urin cenderung sedikit basa (alkalis). Ini masih berada dalam kisaran normal dan umumnya tidak menjadi masalah.", 0]
    elif ph_result == "9,0":
        return ["pH urin sangat basa. Seperti pH urin yang sangat asam, kondisi ini juga jarang terjadi dalam keadaan normal dan dapat mengindikasikan potensi masalah medis atau faktor diet yang ekstrem.", 0]

def predict_blood(blood_result):
    if blood_result == "NEGATIF":
        return ["Tidak ada deteksi darah yang signifikan dalam urin. Ini mengindikasikan bahwa urin tidak mengandung darah dalam jumlah yang dapat dideteksi oleh tes ini.", 1]
    elif blood_result == "+/-":
        return ["Menunjukkan adanya sedikit jumlah darah dalam urin. Ini bisa mengindikasikan adanya jejak darah, tetapi jumlahnya sangat kecil sehingga tidak terlihat secara visual.", 1]
    elif blood_result == "+":
        return ["Ini menunjukkan adanya darah dalam urin dalam jumlah sedikit. Ini bisa mengindikasikan adanya masalah seperti infeksi saluran kemih, batu ginjal, atau masalah lainnya yang mempengaruhi saluran kemih atau sistem ginjal.", 1]
    elif blood_result == "++":
        return ["Ini menunjukkan adanya jumlah darah yang lebih besar dalam urin. Ini bisa mengindikasikan masalah yang lebih serius, seperti peradangan ginjal, infeksi yang lebih parah, atau gangguan ginjal lainnya.", 1]
    elif blood_result == "+++":
        return ["Ini menunjukkan konsentrasi darah yang lebih tinggi lagi dalam urin. Ini bisa mengindikasikan kondisi yang lebih serius, seperti kerusakan ginjal yang signifikan atau masalah lain yang mempengaruhi sistem kemih.", 1]
    elif blood_result == "5-10":
        return ["Ini menunjukkan jumlah sel darah merah yang cukup banyak", 0]
    elif blood_result == "50":
        return ["Jumlah darah ini mengindikasikan jumlah yang lebih tinggi dalam urin, yang dapat mengindikasikan masalah yang lebih serius. Kemungkinan penyebab mungkin termasuk infeksi saluran kemih yang lebih parah, peradangan yang signifikan pada ginjal atau saluran kemih, batu ginjal yang lebih besar atau menyebabkan kerusakan, cedera pada ginjal, atau masalah darah yang mempengaruhi aliran darah ke ginjal. Angka ini mengarah pada potensi masalah yang memerlukan penanganan medis lebih lanjut untuk mengidentifikasi penyebab dan merencanakan tindakan yang sesuai.", 0]

def predict_specificgravity(specificgravity_result):
    if specificgravity_result == 1000:
        return ["Ini menunjukkan urin yang sangat encer, dan bisa mengindikasikan bahwa seseorang mungkin dalam kondisi yang sangat terhidrasi.", 1]
    elif specificgravity_result == 1005:
        return ["Ini masih dianggap urin yang encer, dan bisa mengindikasikan kondisi di mana seseorang cukup terhidrasi.", 1]
    elif specificgravity_result == 1010:
        return ["Ini mengindikasikan urin yang cukup encer, tetapi mulai sedikit lebih pekat daripada sebelumnya. Ini mungkin menunjukkan bahwa seseorang memiliki keseimbangan cairan yang cukup baik.", 0]
    elif specificgravity_result == 1015:
        return ["Ini bisa mengindikasikan bahwa seseorang sedang dalam kondisi normal dalam hal keseimbangan cairan.", 0]
    elif specificgravity_result == 1020:
        return ["Ini bisa mengindikasikan bahwa seseorang mungkin sedang dalam keadaan normal tetapi sedikit terhidrasi.", 0]
    elif specificgravity_result == 1025:
        return ["Ini mungkin mengindikasikan bahwa seseorang sedang mengalami dehidrasi ringan atau memiliki konsentrasi zat terlarut dalam urin yang lebih tinggi.", 0]
    elif specificgravity_result == 1030:
        return[ "Ini bisa mengindikasikan dehidrasi yang lebih serius atau kondisi medis yang memengaruhi keseimbangan cairan dan elektrolit.", 0]

def predict_ketone(ketone_result):
    if ketone_result == "NEGATIF":
        return ["Ini mengindikasikan bahwa urin tidak mengandung keton. Ini adalah hasil dalam keadaan normal.", 1]
    elif ketone_result == "+/-":
        return ["Ini bisa mengindikasikan bahwa tubuh mungkin sedang memecah lemak untuk energi, tetapi level keton masih dalam kisaran normal atau rendah.", 0]
    elif ketone_result == "+":
        return ["Ini bisa mengindikasikan bahwa tubuh sedang memproduksi lebih banyak keton sebagai sumber energi, dan ini mungkin terkait dengan diet rendah karbohidrat, puasa, atau keadaan lain yang mempengaruhi metabolisme lemak.", 0]
    elif ketone_result == "++":
        return ["Ini bisa mengindikasikan peningkatan yang lebih signifikan dalam produksi keton dalam tubuh dan dapat mengindikasikan kondisi seperti ketoasidosis ringan.", 0]
    elif ketone_result == "+++":
        return ["Ini dapat mengindikasikan peningkatan yang lebih signifikan dalam produksi keton dan mungkin menunjukkan kondisi seperti ketoasidosis yang lebih parah.", 0]
    elif ketone_result == "++++":
        return ["Ini adalah indikasi serius dan dapat mengindikasikan ketoasidosis yang signifikan, yang memerlukan penanganan medis segera.", 0]
    
def predict_bilirubin(bilirubin_result):
    if bilirubin_result == "NEGATIF":
        return ["Ini mengindikasikan bahwa urin tidak mengandung bilirubin, Biasanya, bilirubin tidak ditemukan dalam urin karena memang normalnya tidak ada.", 1]
    elif bilirubin_result == "+":
        return ["Ini bisa mengindikasikan adanya masalah dalam hati atau saluran empedu, yang dapat mengakibatkan peningkatan kadar bilirubin dalam darah dan kemudian muncul dalam urin.", 0]
    elif bilirubin_result == "++":
        return ["Ini dapat mengindikasikan masalah yang lebih serius dalam hati atau saluran empedu yang mempengaruhi kemampuan mereka untuk memproses bilirubin dengan baik.", 0]
    elif bilirubin_result == "+++":
        return ["Ini menunjukkan konsentrasi bilirubin yang lebih tinggi lagi dalam urin. Ini bisa mengindikasikan masalah yang lebih serius dalam hati atau saluran empedu yang memerlukan perhatian medis lebih lanjut.", 0]

def predict_glukosa(glukosa_result):
    if glukosa_result == "NEGATIF":
        return ["Ini mengindikasikan bahwa urin tidak mengandung glukosa. Biasanya, glukosa tidak ditemukan dalam urin sehat.", 1]
    elif glukosa_result == "+/-":
        return ["Ini bisa mengindikasikan bahwa kadar glukosa dalam darah mungkin sedikit meningkat, tetapi masih dalam kisaran normal.", 1]
    elif glukosa_result == "+":
        return ["Ini menunjukkan adanya glukosa dalam urin dalam jumlah terdeteksi. Ini bisa mengindikasikan bahwa kadar glukosa dalam darah mungkin lebih tinggi dari biasanya. Hal ini dapat terjadi pada kondisi seperti diabetes.", 1]
    elif glukosa_result == "++":
        return ["Ini dapat mengindikasikan peningkatan yang lebih signifikan dalam kadar glukosa darah, yang bisa menunjukkan masalah seperti diabetes yang lebih serius.", 1]
    elif glukosa_result == "+++":
        return ["Ini bisa mengindikasikan peningkatan yang lebih signifikan lagi dalam kadar glukosa darah, dan memerlukan evaluasi medis lebih lanjut.", 0]
    elif glukosa_result == "++++":
        return ["Ini mengindikasikan adanya kadar glukosa darah yang sangat tinggi, yang bisa sangat serius dan mengindikasikan kondisi diabetes yang perlu ditangani dengan cepat.", 0]

def analysis_result(data):
    result_df = pd.DataFrame(data.items(), columns=["Parameter", "Value"])
    result_df['Value'] = result_df['Value'].apply(lambda x: x[0][0])

    params = {
        'LEUKOSIT': predict_leukocyte(result_df.loc[result_df['Parameter'] == 'LEUKOSIT', 'Value'].values[0] if 'LEUKOSIT' in result_df['Parameter'].values else "")[1],
        'NITRIT' : predict_nitrit(result_df.loc[result_df['Parameter'] == 'NITRIT', 'Value'].values[0] if 'NITRIT' in result_df['Parameter'].values else "")[1],
        'UROBILINOGEN' : predict_urobilinogen(result_df.loc[result_df['Parameter'] == 'UROBILINOGEN', 'Value'].values[0] if 'UROBILINOGEN' in result_df['Parameter'].values else "")[1],
        'PROTEIN' : predict_protein(result_df.loc[result_df['Parameter'] == 'PROTEIN', 'Value'].values[0] if 'PROTEIN' in result_df['Parameter'].values else "")[1],
        'pH' : predict_ph(result_df.loc[result_df['Parameter'] == 'pH', 'Value'].values[0] if 'pH' in result_df['Parameter'].values else "")[1],
        'BLOOD' : predict_blood(result_df.loc[result_df['Parameter'] == 'BLOOD', 'Value'].values[0] if 'BLOOD' in result_df['Parameter'].values else "")[1],
        'SG' : predict_specificgravity(result_df.loc[result_df['Parameter'] == 'SG', 'Value'].values[0] if 'SG' in result_df['Parameter'].values else "")[1],
        'KETON' : predict_ketone(result_df.loc[result_df['Parameter'] == 'KETON', 'Value'].values[0] if 'KETON' in result_df['Parameter'].values else "")[1],
        'BILIRUBIN' : predict_bilirubin(result_df.loc[result_df['Parameter'] == 'BILIRUBIN', 'Value'].values[0] if 'BILIRUBIN' in result_df['Parameter'].values else "")[1],
        'GLUKOSA' : predict_glukosa(result_df.loc[result_df['Parameter'] == 'GLUKOSA', 'Value'].values[0] if 'GLUKOSA' in result_df['Parameter'].values else "")[1],
    }
    sums = 0
    notone = []

    for variable_name, variable_value in params.items():
        if variable_value == 1:
            sums += 1
        elif variable_value != 1:
            notone.append(variable_name)

    
    col1, col2 = st.columns([1, 2])

    with col1:
        labels = ['Normal', 'Tidak Normal']
        sizes = [sums, 10 - sums]  # These values should add up to 100

        # Create a smaller donut chart with a transparent background
        fig, ax = plt.subplots(figsize=(1, 1), facecolor='none')  # Set the figure size and background color to transparent

        # Define text properties, including fontsize and color (white)
        text_props = {'fontsize': 7, 'color': 'white'}

        # colors = ['blue', 'orange']

        ax.pie(sizes, labels=labels, autopct='%1.0f%%', startangle=90, wedgeprops=dict(width=0.5), textprops=text_props)  # Adjust fontsize, color, and specify colors

        # Add a smaller circle at the center to transform it into a smaller donut chart
        circle = plt.Circle((0, 0), 0.3, color='none')
        fig.gca().add_artist(circle)

        # Set aspect ratio to be equal
        ax.axis('equal')

        # Display the smaller donut chart using Streamlit
        st.pyplot(fig)
    
    with col2:
        if sums == 10:
            st.write("Dari 10 parameter yang disebutkan, semuanya memiliki hasil negatif atau dalam kisaran normal. Ini adalah tanda positif bahwa seluruh komponen dalam urin Anda tidak menunjukkan adanya masalah kesehatan yang signifikan dalam hal parameter-parameter tersebut.")
        
        elif sums >= 7:
            st.write(f"Sebagian besar parameter urin Anda tampak normal berdasarkan hasil analisis yang diberikan. Dari 10 parameter yang disebutkan, {sums} di antaranya memiliki hasil negatif atau dalam kisaran normal. Parameter yang tidak negatif diantaranya adalah {', '.join(notone)}")
        
        elif sums < 7:
            st.write(f"Dari 10 parameter yang disebutkan, hanya {sums} yang memiliki hasil negatif atau dalam kisaran normal. Parameter yang tidak negatif diantaranya adalah {', '.join(notone)}. Ini mungkin mengindikasikan adanya masalah kesehatan yang perlu diperhatikan dalam hal parameter-parameter tersebut.")