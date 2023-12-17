import streamlit as st
from ACCOUNTS import Page

import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

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
	prompts = ["Write a story about a robot who falls in love with a human.",
	           "Write a poem about the beauty of nature.",
	           "Write a letter to your future self.",
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
	if selected_prompt and st.checkbox("Use Above Prompts"):
		prompt = selected_prompt

	genai.configure(api_key='AIzaSyBE1HLZuDQHbVz1C6MPD9FcvPbkeJqGrQU')

	model = genai.GenerativeModel('gemini-pro')
	
	with st.spinner("GPT2 is Thinking"):
		if prompt:
			response = model.generate_content(prompt)
			
			Frame1, Frame2, Frame3 = st.tabs(["DISCLAIMER", "RESPONSE", "CHAT"])
			with Frame1:
				st.write("DISCLAIMER!!")
				st.write(" This is an effort to showcase, the Rapid Evolution of AI")
				#st.write(" As the earlier version, GPT 2 may generate inconsistent results that are not Refined!!")
				#st.write(" Built on Hugging Face and Streamlit.")
			with Frame2:
				st.subheader("REPLY")
				k = to_markdown(response.text))
				st.write(k)
			with Frame3:
				st.subheader("Chat with Gemini")
				st.write("In the Next Patch......")

