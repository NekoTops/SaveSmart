import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(initial_sidebar_state="collapsed")
st.title("Debt")
st.image("https://s.hdnux.com/photos/01/32/17/57/23657431/3/rawImage.jpg")
st.write("Debt is a financial obligation that arises when an individual, organization, or government borrows money from a lender with the agreement to repay the borrowed sum along with interest over a specified period. This borrowed capital allows borrowers to make significant purchases, investments, or cover expenses that exceed their immediate financial capacity.")
st.write("Most find it hard to remember how much debt they are really in. Try tracking your debt with our debt calculator:")
if st.button("Debt Calculator"):
   switch_page("Debt Calculator")
if st.button("Home"):
   switch_page("Home")