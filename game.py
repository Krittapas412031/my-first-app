import time
import streamlit as st
st.title("⏱️word timing game")

#set start 
if "ans1_val" not in st.session_state:
st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
st.session_state.ans2_val = ""

# Clear button 

def reset_game():
st.session_state.ans1_val = "" # clear word line 1 
st.session_state.ans2_val = "" # clear word line 2
st.session_state.ans3_val = "" # clear word line 3
st.session_state.ans4_val = "" # clear word line 4
st.session_state.start = time.time() # start

st.session_state.is_ended = False # ปิด Dialog

# ----------------------------------------------------
# 📌 ฟังกช์ นั MessageBox (Dialog)
# ----------------------------------------------------

@st.dialog("📊 game result")
def show_result_dialog(ans1, ans2, ans3, ans4):
st.balloons()
score = 0
u_ans1 = ans1.strip().lower()
u_ans2 = ans2.strip().lower()
u_ans1 = ans3.strip().lower()
u_ans2 = ans4.strip().lower()

# line 1 check
if u_ans1 == "apple":
st.success("✅ ขอ้ 1: Correct")
score += 1
else:
st.error(f"❌ ขอ้ 1: Wrong (you use '{u_ans1}')")
# line 2 check
if u_ans2 == "bone":
st.success("✅ ขอ้ 2: Correct")
score += 1
else:
st.error(f"❌ ขอ้ 2: Wrong (you use '{u_ans2}')")
# student custom question 
if u_ans3 == "doctor":
st.success("✅ ขอ้ 1: Correct")
score += 1
else:
st.error(f"❌ ขอ้ 3: Wrong (you use '{u_ans3}')")
# line 2 check
if u_ans4 == "student":
st.success("✅ ขอ้ 4: Correct")
score += 1
else:
st.error(f"❌ ขอ้ 2: Wrong (you use '{u_ans4}')")

st.info(f"🏆 ไดค้ ะแนนรวม: {score} คะแนน")

if score == 4:
st.success("🎉 You win!")
else:
st.error("💀 Bruh")

# ----------------------------------------------------
#1 play button
# ----------------------------------------------------
st.button("🎮 Play", on_click=reset_game) 

# 2. countdown shows
if "start" in st.session_state and not st.session_state.get("is_ended", False):
time_left = int(30 - (time.time() - st.session_state.start))
if time_left > 0:
st.error(f"⏳: {time_left} second left")
else:
st.session_state.is_ended = True
st.rerun()
st.divider()

# 3. answer input 
ans1 = st.text_input(
"ขอ้ 1: An `a _ _ l e` fall form the tree ", 
value=st.session_state.ans1_val,)
ans2 = st.text_input(
"ขอ้ 2: Dogs love to eat `b__e`. ",
value=st.session_state.ans2_val,)
ans3 = st.text_input(
"ขอ้ 3: The `d_c__r` can cure patience ",
value=st.session_state.ans1_val,)
ans4 = st.text_input(
"ขอ้ 4: Be quiet, the `st_d_nt` are learning. ",
value=st.session_state.ans2_val,)

# update new input
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
# student's custom question
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4

# 4. Enter button
if "start" in st.session_state and not st.session_state.get("is_ended", False):
if st.button("📥 Enter"):
st.session_state.is_ended = True
st.rerun()
time.sleep(1)
st.rerun()

# 5. Show Result dialogue
if st.session_state.get("is_ended", False):
show_result_dialog(ans1, ans2, ans3, ans4)
st.divider()
st.write("นายกฤตภาส สายทอง ม.4/12 เลขที่36") 
