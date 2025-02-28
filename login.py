import streamlit as st
import sqlite3
import streamlit-option-menu import option-menu
def connectdb():
    con=sqlite3.connect("mydb.db")
    return con
def create_table():
    con = connectdb()
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(name text,password text,roll int,branch) ")
    con.commit()
    con.close()
   

st.title("          login form          ")
def signup():
    name= st.text_input("enter your name")
    pwd=st.text_input("enter your password",type="password")
    rpwd=st.text_input("retype password",type="password")
    rno=st.number_input("enter your rollno",min_value=0)
    branch=st.selectbox("select branch ",options=['cse','aiml','iot'])
    gender=st.select_slider("select gender",['Female','','Male'])
    if st.button("signIn"):
        if pwd != rpwd:
            st.error("pasword does not match")
        else:
            addrecord((name,pwd,rno,branch)) 

signup()
def addrecord():
    con=connectdb()
    cur=con.cursor()
    cur.execute('INSERT INTO STUDENT(name , password,roll,branch) values(?,?,?,?)',data)
    con.commit()
    con.close()
def viewrecord():
    con=connectdb()
    cur=con.cursor()
    cur.execute("select *  from student")
    con.commit()
    con.close()
# st.sidebar.title("Sidebar Title")st.sidebar.markdown("This is the sidebar content")
with st.sidebar(): 
     

