import streamlit as st
from streamlit_option_menu import option_menu
from src.pages.chatbot import chatbot
from src.pages.predict import dipstick_analysis
from src.pages.map import find_hospitals_nearby
from src.pages.history import history

def main():
    with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",
                options=["Analisis", "Konsultasi", "Map", "History"],
                icons=["clipboard-plus", "robot", "geo-alt", "list-task"],
                menu_icon="cast",
                default_index=0
            )

    if selected == "Analisis":
        dipstick_analysis()
    
    elif selected == "Konsultasi":
        chatbot()

    elif selected == "Map":
        find_hospitals_nearby()

    elif selected == "History":
        history()


if __name__ == "__main__":
    main()