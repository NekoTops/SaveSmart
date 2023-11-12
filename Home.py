import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config

st.title("SpendSmart")
st.header("INVESTING")
col1, col2, col3 = st.columns(3,gap="small")
with col1:
   st.markdown("[![foo](https://github.com/NekoTops/SaveSmart/blob/main/assets/credit_cards.png?raw=true)](Credit_Cards)")
   #st.balloons()
with col2:
   st.markdown("[![foo](https://github.com/NekoTops/SaveSmart/blob/main/assets/cryptocurrency.png?raw=true)](Crypto_Currency)")
with col3:
   st.markdown("[![foo](https://github.com/NekoTops/SaveSmart/blob/main/assets/stocks.png?raw=true)](Stocks)")
st.divider()
st.header("BUDGETING")
col4, col5, col6 = st.columns(3, gap="small")
with col4:
   st.markdown("[![foo](https://github.com/NekoTops/SaveSmart/blob/main/assets/debt.png?raw=true)](Debt)")
   

with col5:
   st.markdown("[![foo](https://github.com/NekoTops/SaveSmart/blob/main/assets/retirement_plans.png?raw=true)](Retirement_Plans)")

with col6:
    st.markdown("[![foo](https://github.com/NekoTops/SaveSmart/blob/main/assets/financial_aid.png?raw=true)](Financial_Aid)")
st.divider()
