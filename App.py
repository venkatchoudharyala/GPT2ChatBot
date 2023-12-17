import streamlit as st
from ACCOUNTS import Page
import AdminPanel as ap

import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return textwrap.indent(text, '> ', predicate=lambda _: True)

hide_st_style = """
		<style>
		header {visibility: hidden;}
		footer {visibility: hidden;}
  	</style>
  	"""

st.markdown(hide_st_style, unsafe_allow_html = True)
Page.main()
if "user" in st.session_state:
	UserDetails = st.session_state["user"]
	#st.write(UserDetails)
	st.session_state["LoginVal"] = True
	#Expand = st.sidebar.expander("Chats")

else:
	st.session_state["LoginVal"] = False
if st.session_state["LoginVal"]:
	UserName = UserDetails["Name"]
	if UserName == "Admin":
		ap.Scrapper()
	else:
		genai.configure(api_key='AIzaSyBE1HLZuDQHbVz1C6MPD9FcvPbkeJqGrQU')
	
		model = genai.GenerativeModel('gemini-pro')
		
		prompts = ["Write a program for tower of Hanoi problem in python.",
		           "Explain concepts of DSA in nutshell.",
		           "Can I know about your model architecture.",
		           "Write a news article about a recent scientific discovery.",
		           "Write a song about your favorite animal.",
		           "Write a script for a short film.",
		           "Write a blog post about the importance of recycling.",
		           "Write a marketing copy for a new product.",
		           "Write a technical document for a new software feature.",
		           "Write a creative story about a world where everyone has superpowers.",
		           "Write a horror story about a haunted house.",
		           "Write a mystery story about a missing person.",
		           "Write a science fiction story about a journey to another planet."]
		
		selected_prompt = st.selectbox("Select a prompt:", prompts)
		prompt = st.chat_input("Or say something Here")
		if selected_prompt and st.checkbox("Use Above Prompts", value = False):
			prompt = selected_prompt
	
		with st.spinner("GeminiAI is Thinking"):
			if prompt:
				response = model.generate_content(prompt)
				
				Frame1, Frame2, Frame3 = st.tabs(["RESPONSE", "CHAT", "DISCLAIMER"])
				
				with Frame1:
					st.subheader("Replying to the Prompt")
					st.write(Prompt)
					st.write(to_markdown(response.text))
				with Frame2:
					st.subheader("Chat with Gemini")
					st.write("In the Next Patch......")
				with Frame3:
					st.write("DISCLAIMER!!")
					st.write(" This is an effort to showcase, the Rapid Evolution of AI")
					st.write(" Exported from Google's GenerativeAI")

