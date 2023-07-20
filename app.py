import streamlit as st
import pandas as pd
import numpy as np

st.title('My first app')
# st.write("hello world")
# st.image("./cat.jpg")

st.sidebar.title('My first app')
# st.sidebar.write("hello world")
# st.sidebar.image("./cat.jpg")

# with st.sidebar:
#     st.write('hello world')
#     rt = st.radio("radio", ["apple", "banana", "berry"])
#     st.write(rt)
#     st.image('./cat.jpg')

# ##############################
# col1, col2, col3 = st.columns(3)
# col1.image('./cat.jpg')
# col2.image('./dog.jpg')
# col3.image('./dog.jpg')

# ######################################
# col1, col2 = st.columns([2, 1])
# col1.subheader('A cat')
# col2.subheader("A dog")

# col1.image('./cat.jpg')
# col2.image('./dog.jpg')

# #########################
# col1, col2 = st.columns([2, 1])
# with col1:
#     st.subheader("A cat")
#     st.image("./cat.jpg")


# with col2:
#     st.subheader("A dog")
#     st.image("./dog.jpg")
#     st.write('hello dog')
# st.write("hello world")

#######################
# 탭 사용하기

# t1, t2, t3 = st.tabs(['Cat', 'Dog', "Owl"])

# with t1:
#     st.header("A cat")
#     st.image("./cat.jpg", width = 400)

# with t2:
#     st.header("A dog")
#     st.image("./dog.jpg", width = 400)

# with t3:
#     st.markdown("A owl")
#     st.image("./owl.jpg", width = 400)

############################3
# container 사용

# ct1 = st.container()
# st.image("./owl.jpg") ###
# ct2 = st.container()

# ct1.title("cat!!!")
# ct2.title("dog!!!")

# col1, col2 = st.columns([2, 1])
# with col1:
#     st.subheader("A cat")
#     st.image("./cat.jpg")
#     ct1.write("catttt")


# with col2:
#     st.subheader("A dog")
#     st.image("./dog.jpg")
#     ct2.write("dogggg")

# ct1.image("./cat.jpg", width = 400)
# ct2.image("./dog.jpg", width=400)

#############################
import time
cn = st.container()
cn.text("hello world1")
cn.text("hello world2")
cn.text("hello world3")
cn.text("hello world4")

st.image("./dog.jpg", width=400)

emp = st.empty() # 하나만 컨트롤 할 수 있음

emp.title("hello world1")
time.sleep(3)
emp.title("hello world2")
time.sleep(3)
emp.image("./dog.jpg", width=400)
time.sleep(3)
emp.image("./cat.jpg", width = 400)