import streamlit  as st
import random 
number=random.randint(1,20)
st.title("أهلا بك في لعبتنا التابعه للبروفييسير الاستاذ محمد احمد رياض ")
name = st.text_input("من فضلك اعطيني اسمك")
if name:
 st.write("welcome to our guess game "+name )
guess=st.number_input("ادخل تخمينك ")
if st.button("تاكد من التخمين "):
  if guess == number:
     st.success("you are winner")
  if guess > number:
      st.error("you are loser the number was "+number)  
  if guess < number:
      st.error("you are loser the number was "+number)       
