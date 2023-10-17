import streamlit as st
from transformers import AutoTokenizer, pipeline, AutoModelForCausalLM
import warnings

hide_st_style = """
		<style>
		header {visibility: hidden;}
		footer {visibility: hidden;}
  	</style>
  	"""
warnings.filterwarnings("ignore")

st.markdown(hide_st_style, unsafe_allow_html = True)

st.subheader("For example, you can prompt GPT-2 to write a poem in the style of Shakespeare, or to generate a code snippet in a specific programming language.)
prompt = st.chat_input("Say Something")

model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")
prompter = pipeline("text-generation", model = model, tokenizer = tokenizer)
MachineOP = prompter(prompt)
k = st.chat_message("assistant")
k.write(MachineOP[0]['generated_text'])
