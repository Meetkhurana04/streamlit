import streamlit as st
import sqlite3
from streamlit_option_menu import option_menu
def connectdb():
    con=sqlite3.connect("mydb.db")
    return con
def create_table():
    con = connectdb()
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(name text,password text,roll int primary key,branch text) ")
    con.commit()
    con.close()

def addrecord(data):
    con = connectdb()
    cur = con.cursor()
    try:
        cur.execute('INSERT INTO student(name, password,roll,branch) values (?,?,?,?)', data)
        con.commit()
        con.close()
    except sqlite3.IntegrityError :
        print("an error")

def viewrecord():
    st.title("          View Record         ")
    con=connectdb()
    cur=con.cursor()
    cur.execute("select * from student")
    rows = cur.fetchall()
    
    st.table(rows)
    con.close()
# def display():
#     data=viewrecord()
#     print(data)
    # st.write(data)

   


def signup():
    st.title("          login form          ")
    name= st.text_input("enter your name")
    pwd=st.text_input("enter your password",type="password")
    rpwd=st.text_input("retype password",type="password")
    rno=st.number_input("enter your rollno",min_value=0,step=None)
    branch=st.selectbox("select branch ",options=['cse','aiml','iot'])
    # gender=st.select_slider("select gender",['Female','','Male'])
    if st.button("signIn"):
        if pwd != rpwd:
            st.error("pasword does not match")
        else:
            addrecord((name,pwd,rno,branch)) 
            st.write("succesfull added")


create_table()

with st.sidebar:
    selected = option_menu('select from here', ['SignUp','Display All Record'])

if selected == 'SignUp':
    signup()
else:
    viewrecord()

