import streamlit as st
import random

# حفظ الرقم العشوائي في الذاكرة حتى لا يتغير مع كل ضغطة زر
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 20)

st.title("أهلاً بك في لعبتنا التابعة للبروفيسير الأستاذ محمد أحمد رياض")

# 1. أخذ الاسم وعرض الترحيب بشكل صحيح
name = st.text_input("من فضلك اعطيني اسمك")
if name:
    st.write(f"أهلاً بك {name}")

# 2. أخذ التخمين من خلال واجهة Streamlit
guess = st.number_input("من فضلك ادخل تخمينك (من 1 إلى 20):", min_value=1, max_value=20, step=1)

# زر للتحقق من النتيجة
if st.button("تحقق من التخمين"):
    if guess == st.session_state.number:
        st.success("You are winner! 🎉")
        # إعادة تعيين رقم جديد بعد الفوز
        del st.session_state.number
    elif guess > st.session_state.number:
        st.error("Too high! Try a smaller number.")
    else:
        st.error("Too low! Try a bigger number.")
