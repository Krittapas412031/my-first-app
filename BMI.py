import streamlit as st

print("=== BMI Calculator ===")

weight = float (input("Enter your weight (kg): "))
height = float(input("Enter your height (cm): ")) 

#Convert centimeters - metres
height_m = height / 100

#calculate 
BMI = weight / height_**2) 

print(f"\nYour BMI is: {BMI:.2f}") 

# classification 
if BMI <= 18.5 < 25:
  category = "underweight"
elif BMI <= 25 < 30:
  category = "Normal weight" 
elif BMI <= 30:
  category = "Overweight"
else:
  category = "Obesity"
  print(f"Category: {category}") 

st.divider() 
st.write("นายกฤตภาส สายทอง ม.4/12 เลขที่ 36")
