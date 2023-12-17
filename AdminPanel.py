import streamlit as st
import json
import os

st.set_page_config(initial_sidebar_state = "collapsed")

hide_st_style = """
		<style>
		header {visibility: hidden;}
		footer {visibility: hidden;}
  		</style>
  		"""

st.markdown(hide_st_style, unsafe_allow_html = True)

def Scrapper():
  Form = st.form("Login")
  dir = os.listdir("UserAcc")
  MPath = st.selectbox("Users", dir)
  #UserName = Form.text_input("User Name")
  Path = "UserAcc/" + MPath
  Rapo(Path)
def Rapo(Path):
  try:
	  with open(Path, "r") as File:
		  UDetails = File.read()
		  Details = json.loads(UDetails)
		  st.write(Details)
  except FileNotFoundError:
	  st.write("User Not Found")
