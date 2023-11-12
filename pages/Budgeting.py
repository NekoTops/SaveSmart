import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(initial_sidebar_state="collapsed")
st.title("Budgeting")
st.image('https://happay.com/blog/wp-content/uploads/sites/12/2023/05/capital-budgeting.webp')
st.write("What is a budget? A budget is a plan for your spending. Tracking your purchases and living within a budget allows you to be confident that you've got the money to cover your essential living expenses. You'll also be ready when unplanned expenses pop up, and even you're able to pursue the things in life that are important to you.")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.write("test your budgeting skills with our budgeting simulation")
if st.button("Start Simulation"):
   switch_page("Budgeting Simulation")
if st.button("Home"):
   switch_page("Home")