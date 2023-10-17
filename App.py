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
	prompt = st.chat_input("Say Something")
	if selected_prompt and st.checkbox("Use Above Prompts", value = True):
		prompt = selected_prompt
	model = AutoModelForCausalLM.from_pretrained("gpt2")
	tokenizer = AutoTokenizer.from_pretrained("gpt2")
	prompter = pipeline("text-generation", model = model, tokenizer = tokenizer, max_new_tokens = 250)
	with st.spinner("GPT2 is Thinking"):
		if prompt:
			MachineOP1 = prompter(prompt)
			MachineOP2 = prompter(prompt)
			Frame1, Frame2, Frame3 = st.tabs(["DISCLAIMER", "RESPONSE - 1", "RESPONSE - 2"])
			with Frame1:
				st.write("THIS IS A DISCLAIMER!!")
			with Frame2:
				st.subheader("REPLY DRAFT 1")
				st.write(MachineOP1[0]['generated_text'])
			with Frame3:
				st.subheader("REPLY DRAFT 2")
				st.write(MachineOP2[0]['generated_text'])

