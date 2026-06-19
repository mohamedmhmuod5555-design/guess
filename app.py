import streamlit  as st
import random 
number=random.randint(1,20)
st.title("أهلا بك في لعبتنا التابعه للبروفييسير الاستاذ محمد احمد رياض ")
name = st.text_input("من فضلك اعطيني اسمك")

print("من فضلك ادخل تخمينك ")
guess=int(input())
if guess == number:
    print("you are winner")
if guess > number:
    print("you are loser the number was ",number)  
if guess < number:
    print("you are loser the number was ",number)       
