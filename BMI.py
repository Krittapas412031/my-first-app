import streamlit as st

#page 
st.markdown("# :red[BMI Calculator]")
st.write ("please input your weight to check your health") 

#input weight and height 
weight = st.number_input("Enter your weight (kg): ", min_value = 1.0, value = 1.0)
height_cm = st.number_input("Enter your height (cm): ", min_value = 1.0, value = 1.0)


#calculate and calculate button
if st.button("Calculate."):
#Convert centimeters - metres
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    st.write("---")
    st.header(f"Your BMI is: **{BMI:.2f}**") 

# classification 
    if bmi <= 18.5 < 25:
        st.category = ("underweight (too thin)")
    elif bmi <= 25 < 30:
      st.category = ("Normal weight (perfect.)") 
    elif bmi <= 30:
      st.category = ("Overweight (a little bit fat)")
    else:
      st.category = ("Obesity.")
      st.write(f"Category: {category}") 

st.divider() 
st.write("นายกฤตภาส สายทอง ม.4/12 เลขที่ 36")
