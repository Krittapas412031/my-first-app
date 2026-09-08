import time
import streamlit as st

st.title("💖 Heartbeat: Word Timing Game")
st.caption("How quickly can you connect with your emotions?")

# Initialize Session State Variables
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""
if "is_ended" not in st.session_state:
    st.session_state.is_ended = False

# Function to reset the game state
def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False

# ----------------------------------------------------
# 📌 MessageBox Function (Dialog)
# ----------------------------------------------------
@st.dialog("💭 Emotional Reflection")
def show_result_dialog(ans1, ans2, ans3, ans4):
    st.balloons()
    score = 0
    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()

    # Question 1 Check
    if u_ans1 == "happy":
        st.success("✅ ข้อ 1: Pure Sunshine! Correct.")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: Missed a beat (you entered '{u_ans1}')")

    # Question 2 Check
    if u_ans2 == "lonely":
        st.success("✅ ข้อ 2: Understood completely. Correct.")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: Missed a beat (you entered '{u_ans2}')")

    # Question 3 Check
    if u_ans3 == "excited":
        st.success("✅ ข้อ 3: High energy! Correct.")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: Missed a beat (you entered '{u_ans3}')")

    # Question 4 Check
    if u_ans4 == "peaceful":
        st.success("✅ ข้อ 4: Calm and serene. Correct.")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: Missed a beat (you entered '{u_ans4}')")

    # Final Score
    st.divider()
    st.info(f"✨ Emotional Alignment: {score} / 4 correct")
    if score == 4:
        st.success("🌸 You are deeply in touch with feelings today!")
    elif score >= 2:
        st.warning("🌿 A good try! Feelings take time to process.")
    else:
        st.error("🌧️ Don't worry, every emotion comes and goes. Try again!")

# ----------------------------------------------------
# 1. Play Button
# ----------------------------------------------------
st.button("🌱 Begin Reflection", on_click=reset_game)

# ----------------------------------------------------
# 2. Countdown Display
# ----------------------------------------------------
if "start" in st.session_state and not st.session_state.is_ended:
    time_left = int(30 - (time.time() - st.session_state.start))
    if time_left > 0:
        st.warning(f"⏳ Pulse: {time_left} seconds remaining...")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# ----------------------------------------------------
# 3. Answer Inputs (Feeling-themed prompts)
# ----------------------------------------------------
ans1 = st.text_input(
    "ข้อ 1: Smiling wide, full of joy and laughter — `h _ _ p y`",
    value=st.session_state.ans1_val,
    key="input1"
)
ans2 = st.text_input(
    "ข้อ 2: Sitting alone in a quiet room, missing company — `l _ n _ l y`",
    value=st.session_state.ans2_val,
    key="input2"
)
ans3 = st.text_input(
    "ข้อ 3: Heart racing before a big adventure! — `e x _ _ t e d`",
    value=st.session_state.ans3_val,
    key="input3"
)
ans4 = st.text_input(
    "ข้อ 4: Listening to gentle rain without any worries — `p e _ c e _ u l`",
    value=st.session_state.ans4_val,
    key="input4"
)

# Sync inputs to session state
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4

# ----------------------------------------------------
# 4. Enter / Submit Button
# ----------------------------------------------------
if "start" in st.session_state and not st.session_state.is_ended:
    if st.button("💌 Submit Emotions"):
        st.session_state.is_ended = True
        st.rerun()

# ----------------------------------------------------
# 5. Show Result Dialog
# ----------------------------------------------------
if st.session_state.is_ended:
    show_result_dialog(
        st.session_state.ans1_val,
        st.session_state.ans2_val,
        st.session_state.ans3_val,
        st.session_state.ans4_val
    )

st.divider()
st.write("นายกฤตภาส สายทอง ม.4/12 เลขที่ 36")
