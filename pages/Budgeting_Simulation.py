import streamlit as st
import numpy as np
from streamlit_extras.switch_page_button import switch_page

st.title("Budgeting Simulation")

total = 300
j = st.slider(label="Groceries",value =0)
s = st.slider(label="Retail Therapy",value =0)
e = st.slider(label = "Emergency Funds",value =0)
d = st.slider(label = "Debt Payment",value =0)
l = st.slider(label = "Savings",value =0)
st.write("Lets start you out with $300 to last you the next month. The goal is to budget 100% of your money, but keep in mind somethings hit the wallet harder than others! When you are done check the graph to see your quality of life trajectory")
st.write("$ remaining:")
total - (j + (s*2) + e +(d*3)+l)
x1 = np.array([j])
x2 = np.array([e])
x3 = np.array([s])
x4 = np.array([d])
x5 = np.array([l])
hist_data = [x1, x2, x3, x4, x5]
st.line_chart(hist_data)
st.write("This graph represents your quality of life, Y, versus time in weeks, X")
st.write("Reading The Graph: If the slope is negitive, over time feelings of financial security and overall mood would decrease. If the slope is positive then your feelings of financial security and overall mood would increase.")
st.write("WARNING!!!: the negitive amount of your total comes from next months $300, try not to go overboard with your spending.")
if st.button("Home"):
   switch_page("Home")
if st.button("Return to Budgeting Lesson"):
   switch_page("Budgeting")