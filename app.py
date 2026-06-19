import streamlit  as st
import random 
number=random.randint(1,20)
st.title("أهلا بك في لعبتنا التابعه للبروفييسير الاستاذ محمد احمد رياض ")
print(" ما اسمك ")
name=input()
st.write(" أهلا بك"+name)
print("من فضلك ادخل تخمينك ")
guess=int(input())
if guess == number:
    print("you are winner")
if guess > number:
    print("you are loser the number was ",number)  
if guess < number:
    print("you are loser the number was ",number)       
