import streamlit as st
from transformers import AutoTokenizer, pipeline, AutoModelForCausalLM
from ACCOUNTS import Page

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
Uprompt = st.chat_input("Say Something")

if selected_prompt and st.checkbox("Use Above Prompmts", value = True):
	Uprompt = selected_prompt
prompt = "For ur Specific Query " + Uprompt + " you have to"
model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")
prompter = pipeline("text-generation", model = model, tokenizer = tokenizer, max_new_tokens = 500)
MachineOP = prompter(prompt)
k = st.chat_message("assistant")
k.write(MachineOP[0]['generated_text'])
