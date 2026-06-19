import streamlit  as st
import random 
number=random.randint(1,20)
st.title("أهلا بك في لعبتنا التابعه للبروفييسير الاستاذ محمد احمد رياض ")
name = st.text_input("من فضلك اعطيني اسمك")
guess=st.text_input("ادخل تخمينك ")
if guess == number:
    st.write("you are winner")
if guess > number:
   st.write("you are loser the number was ",number)  
if guess < number:
    st.write("you are loser the number was ",number)       
