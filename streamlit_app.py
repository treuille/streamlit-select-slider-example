import streamlit as st
import string


def set_letter_range(min_letter, max_letter):
    st.session_state.letter_range = (min_letter, max_letter)


if "letter_range" not in st.session_state:
    set_letter_range("u", "b")

result = st.select_slider(
    "Select a letter range", string.ascii_letters, key="letter_range"
)

st.write("You selected", result, st.session_state.letter_range)


col1, col2 = st.columns(2)
col1.button("Select lowercase letters", on_click=set_letter_range, args=("a", "z"))
col2.button("Select uppercase letters", on_click=set_letter_range, args=("A", "Z"))
