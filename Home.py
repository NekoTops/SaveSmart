import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
import streamlit.components.v1 as components

st.set_page_config(initial_sidebar_state="collapsed")
st.title("SpendSmart")
st.header("INVESTING")
col1, col2, col3 = st.columns(3,gap="small")
with col1:
   st.markdown("[![foo](https://github.com/NekoTops/SaveSmart/blob/main/assets/credit_cards.png?raw=true)](Credit_Cards)")
   st.write("Credit Cards")
   #st.balloons()
with col2:
   st.markdown("[![foo](https://github.com/NekoTops/SaveSmart/blob/main/assets/cryptocurrency.png?raw=true)](Crypto_Currency)")
   st.write("Crypto Currency")
with col3:
   st.markdown("[![foo](https://github.com/NekoTops/SaveSmart/blob/main/assets/stocks.png?raw=true)](Stocks)")
   st.write("Stocks")
st.divider()
st.header("SAVING")
col4, col5, col6, col7 = st.columns(4, gap="small")
with col4:
   st.markdown("[![foo](https://github.com/NekoTops/SaveSmart/blob/main/assets/debt.png?raw=true)](Debt)")
   st.write("Debt")
   

with col5:
   st.markdown("[![foo](https://github.com/NekoTops/SaveSmart/blob/main/assets/retirement_plans.png?raw=true)](Retirement_Plans)")
   st.write("Retirement Plans")

with col6:
    st.markdown("[![foo](https://github.com/NekoTops/SaveSmart/blob/main/assets/financial_aid.png?raw=true)](Financial_Aid)")
    st.write("Financial Aid")
with col7:
    st.markdown("[![foo](https://github.com/NekoTops/SaveSmart/blob/main/assets/budgeting.png?raw=true)](Budgeting)")
    st.write("Budgeting")
st.divider()
