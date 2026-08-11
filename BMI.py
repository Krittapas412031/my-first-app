import streamlit as st

#1 ส่วนหน้าเว็บ
st. markdown("#: red [ค่าคำนวนดัชนีมวลกาย BMI]")
st.write ("กรอกข้อมูลและน้ำหนักของคุณเพื่อเช็คสุขภาพเบื้องต้น") 

#2 ช่องรับข้อมูลน้ำหนักและส่วนสูง
weight = st.number_input("กรอกน้ำหนักของคุณด้วยกิโลกรัม:", min_value = 1.0, value = 1.0) 
height_cm = st.number_input("กรอกส่วนสูงของคุณด้วยเซนติเมตร:", min_value = 1.0, value = 1.0) 

#3 ปุ่มกดคำณวน 
if st.button("คำณวนค่า BMI"):

  #แปลง cm เป็น m เพื่อหาค่า BMI 
  height_m = height_cm / 100 
BMI = weight / (height_m ** 2) 

st.write ("---") 
st.header(f"ค่า BMI ของคุณคือ: **{BMI:.2f}**") 

#4 แปลงค่า BMI ตามเกณท์ 
if BMI < 18.5:
  st.warning("ผอมเกินไป")
elif 18.5 <= BMI < 23.0:
st.success ("ผอมพอดีตามเกณฑ์")

elif 23.0 <=BMI < 25.0:
st.info ("ท้วมมากกว่าเกณฑ์นิดหน่อย") 

else:
st.error ("อ้วนมากกกกกกกกกก ควรรักษาสุขภาพและออกกำลังกาย")

st.divider() 
st.write("นายกฤตภาส สายทอง ม.4/12 เลขที่ 36")
