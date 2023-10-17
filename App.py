import streamlit as st
from transformers import AutoTokenizer, pipeline, AutoModelForCausalLM

hide_st_style = """
		<style>
		header {visibility: hidden;}
		footer {visibility: hidden;}
  	</style>
  	"""

st.markdown(hide_st_style, unsafe_allow_html = True)

prompt = st.input("Say Something")

model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")
prompter = pipeline("text-generation", model = model, tokenizer = tokenizer)
MachineOP = prompter(prompt)
st.head(MachineOP)
