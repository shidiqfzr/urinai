import streamlit as st
from streamlit_option_menu import option_menu
from src.pages.analysis import dipstick_analysis
from src.pages.chatbot import chatbot

# hide_st_style = """ 
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True) # hide streamlit menu

def main():
    with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",
                options=["Analisis", "Konsultasi"],
                icons=["clipboard-plus", "robot"],
                menu_icon="cast",
                default_index=0
            )

    if selected == "Analisis":
        dipstick_analysis()
    
    elif selected == "Konsultasi":
        chatbot()

if __name__ == "__main__":
    main()