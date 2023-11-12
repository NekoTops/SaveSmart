import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(initial_sidebar_state="collapsed")
st.title("Stocks")
st.write("Coming Soon!")
if st.button("Home"):
   switch_page("Home")