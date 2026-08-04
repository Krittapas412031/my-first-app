import streamlit as st
st.title ("แปลง พ.ศ. เป็น ค.ศ.")

bh_year =  st.number_input("กรอกปี พ.ศ. ที่ต้องการแปลง", value = 2569)
ch_year = bh_year-543
st.header(f"ปี ค.ศ. คือ : {ch_year} ")
