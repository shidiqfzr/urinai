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
        return "Tidak ada atau kadar sangat rendah urobilinogen dalam urine. Ini biasanya merupakan hasil normal dan menunjukkan kesehatan normal dalam hal metabolisme bilirubin."
    elif urobilinogrn_result == "1 (Neg)":
        return "Tidak ada atau kadar sangat rendah urobilinogen dalam urine. Ini biasanya merupakan hasil normal dalam hal metabolisme bilirubin."
    elif urobilinogrn_result == "2 (Pos)":
        return "Terindentifikasi adanya kadar urobilinogen yang sedikit lebih tinggi dalam urine. Ini bisa disebabkan oleh beberapa faktor seperti metabolisme bilirubin yang lebih tinggi atau interaksi dengan obat-obatan tertentu."
    elif urobilinogrn_result == "4 (Pos)":
        return "Peningkatan lebih lanjut pada kadar urobilinogen dalam urine. Bisa mengindikasikan adanya faktor yang lebih signifikan yang mempengaruhi metabolisme bilirubin."
    elif urobilinogrn_result == "8 (Pos)":
        return "Konsentrasi urobilinogen yang lebih tinggi dalam urine. Bisa menunjukkan masalah yang lebih serius dalam metabolisme bilirubin atau masalah hati."
    elif urobilinogrn_result == "12 (Pos)":
        return "Konsentrasi urobilinogen yang tinggi dalam urine. Bisa menjadi tanda masalah serius dalam metabolisme bilirubin atau gangguan hati yang perlu penanganan medis lebih lanjut."