import streamlit as st
from transformers import AutoTokenizer, pipeline, AutoModelForCausalLM

prompt = st.input("Say Something")

model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")
prompter = pipeline("text-generation", model = model, tokenizer = tokenizer)
MachineOP = prompter(prompt)
st.head(MachineOP)
