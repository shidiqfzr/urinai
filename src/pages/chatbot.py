import openai
import streamlit as st

def is_health_related(prompt):
    health_keywords = ["kesehatan", "penyakit", "sakit", "dokter", "rumah sakit", "obat", "sakit", "gizi", "bugar", "makanan sehat", 
                       "pola makan", "kencing", "pipis", "olahraga", "imunisasi", "vaksinasi","vaksin","imun","stress","diet","nutrisi",
                       "mencegah kencing","mencegah diabetes","diabetes", "kolesterol", "darah", "tekanan darah", "pemeriksaan", "diperiksa", 
                       "reproduksi", "air bersih", "air seni", "kebersihan", "bersih", "pengobatan", "terapi", "fisik", "tidur", "pemulihan", "nutrisi"]

    prompt_lower = prompt.lower()
    for keyword in health_keywords:
        if keyword in prompt_lower:
            return True
    return False

def chatbot():
    st.markdown("<h1 style='text-align: center; margin-bottom: 1em;'>Healthbot</h1>", unsafe_allow_html=True)

    openai.api_key = st.secrets["OPENAI_API_KEY"]

    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Kirim pesan"):
        if is_health_related(prompt):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
                for response in openai.ChatCompletion.create(
                    model=st.session_state["openai_model"],
                    messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ],
                    stream=True,
                ):
                    full_response += response.choices[0].delta.get("content", "")
                    message_placeholder.markdown(full_response + " ")
                message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        #jika kata-kata di pertanyaannya tidak ada di list kata kunci
        else:
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.session_state.messages.append({"role": "assistant", "content": "Kami tidak punya pengetahuan apapun mengenai pertanyaan Anda."})
            with st.chat_message("user"):
                st.markdown(prompt)
            with st.chat_message("assistant"):
                st.markdown("Kami tidak punya pengetahuan apapun mengenai pertanyaan Anda.")