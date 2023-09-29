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
                options=["Analisis", "History", "Konsultasi", "Map"],
                icons=["clipboard-plus", "list-task", "robot", "geo-alt"],
                menu_icon="cast",
                default_index=0
            )

    if selected == "Analisis":
        dipstick_analysis()
    
    elif selected == "History":
        history()
    
    elif selected == "Konsultasi":
        chatbot()

    elif selected == "Map":
        find_hospitals_nearby()


if __name__ == "__main__":
    main()