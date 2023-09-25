import streamlit as st
from streamlit_option_menu import option_menu
from src.pages.chatbot import chatbot
from src.pages.predict import dipstick_analysis

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