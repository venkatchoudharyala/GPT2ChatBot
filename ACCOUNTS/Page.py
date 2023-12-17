import streamlit as st
import os
import json
import warnings
import bcrypt
import datetime
import pytz

warnings.filterwarnings("ignore", category=DeprecationWarning)

#@st.cache_data(experimental_allow_widgets=True)
def main():
	Page = st.session_state.get('page', 'LoginPage')

	if(Page == "LoginPage"):
		LoginPage()
	elif(Page == "SignUpPage"):
		SignUpPage()
	elif(Page == EmptyPage):
		EmptyPage()

#@st.cache_data(experimental_allow_widgets=True)
def LoginPage():
	ExceptFlag = 0
	st.header("Login Page")
	InpForm = st.form("Login")
	RePassd = "ImNoWhere!!!"
	UserName = InpForm.text_input("User Name")
	Passd = InpForm.text_input("Password", type = "password")

	if InpForm.form_submit_button("Submit"):
		UserPath = "UserAcc/" + UserName.strip() + ".ua"
		time = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))

		try:
			with open(UserPath, "r") as File:
				Details = json.load(File)
				RePassd = Details["Password"]
				LoTimes = int(Details["NoLog"])

			if CheckPasswdHash(Passd.strip(), RePassd):
				LoTimes += 1
				Details["NoLog"] = str(LoTimes)
				Details["TimeStamps"].append(str(time))
				with open(UserPath, "w") as File:
					json.dump(Details, File)
				st.session_state["user"] = Details
				st.write("Login Successful")
				st.session_state['page'] = 'EmptyPage'
				st.experimental_rerun()
				#st.stop()
			elif(ExceptFlag == 0):
				st.write("Invalid Password")
		except FileNotFoundError:
			ExceptFlag = 1
			st.write("User Not Found")

	st.write("New User ? Try Sigining up!!!")
	if st.button("Signup"):
		st.session_state['page'] = 'SignUpPage'
		st.experimental_rerun()

#@st.cache_data(experimental_allow_widgets=True)
def SignUpPage():
	st.header("Sign Up Page")
	Form = st.form("SignUp Form")
	UserName = Form.text_input("User Name")
	Passd = Form.text_input("Password", type = "password", key = "password")
	ConfPassd = Form.text_input("Confirm Password", type = "password", key = "Cpassword")

	if Form.form_submit_button("Submit"):
		if UserName == "":
			st.write("Enter a Valid User Name!!!")
		elif Passd.strip() != ConfPassd.strip():
			st.write("Re-enter Password")

		else:
			path = "UserAcc/" + UserName.strip() + ".ua"
			try:
				with open(path, "r") as File:
					st.write("UserName Already Exists!! Try another..")

			except FileNotFoundError:

				Details = {"Name":UserName.strip(),"Chats":{},"Blocked":{UserName.strip():"1"},"Password":HashPasswd(Passd.strip()), "NoLog":"0", "TimeStamps":[]}
				UDetails = json.dumps(Details)
				Path = os.path.join("UserAcc", UserName.strip() + ".ua")
				with open(Path, "w") as File:
					File.write(UDetails)

				st.write("Signup Successful")
				st.write("Be Marked with ur Account Credentials..")
				st.write("As we don't host any Integrity System, we can't have Password CHANGE option.. ")
				st.write("Therefore if Credentials were lost the chats and Account will be in-accessible!!")
				st.session_state['page'] = 'LoginPage'
				if st.button("Back to Login"):
					#st.session_state['page'] = 'LoginPage'
					st.experimental_rerun()

#@st.cache_data(experimental_allow_widgets=True)
def EmptyPage():
	#To Replace the previous page
	st.empty()

def HashPasswd(password):
	salt = bcrypt.gensalt()
	hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
	return hashed_password.decode('utf-8')

def CheckPasswdHash(password, hashed_password):
	return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

if __name__ == "__main__":
	main()
