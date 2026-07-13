import streamlit as st
import bcrypt
import database

st.set_page_config(
    page_title="FlightDekho",
    page_icon="✈️",
    layout="wide"
)
database.create_database()

class User:
    def __init__(self, name: str,email : str, age: int, gender: str, password: str):
        self.name = name
        self.email = email
        self.age = age
        self.gender = gender
        self.__password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )

    def getuser_info(self):
        return f"Name : {self.name}  Age : {self.age}  Gender : {self.gender}"

    def get_password(self):
        return self.__password.decode()

    def send_to_database(self):
        database.insert_user(
        self.name,
        self.email,
        self.age,
        self.gender,
        self.__password.decode() )


# ---------------- CSS ---------------- #

st.markdown("""
<style>

.stApp{
    background-color:#f5f7fa;
}

.main-title{
    text-align:center;
    font-size:50px;
    font-weight:bold;
    color:#1f2937;
    margin-bottom:5px;
}

.sub-title{
    text-align:center;
    font-size:20px;
    color:#6b7280;
    margin-bottom:35px;
}

div[data-testid="stForm"]{
    background:white;
    padding:30px;
    border-radius:18px;
    border:1px solid #d1d5db;
    box-shadow:0px 8px 20px rgba(0,0,0,0.08);
}

label{
    color:#374151 !important;
    font-size:16px !important;
    font-weight:600 !important;
}

.stButton>button{
    width:100%;
    height:50px;
    background:#2563eb;
    color:white;
    border-radius:10px;
    border:none;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#1d4ed8;
}

.feature-box{
    background:white;
    padding:25px;
    border-radius:18px;
    border:1px solid #d1d5db;
    box-shadow:0px 8px 20px rgba(0,0,0,0.08);
}

.footer{
    text-align:center;
    color:#6b7280;
    margin-top:30px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>✈️ FlightDekho</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='sub-title'>Get your flight information immediately </p>",
    unsafe_allow_html=True,
)

left, right = st.columns([2, 1])

with left:

    with st.form("Person Form"):

        st.subheader("Create Your Account")

        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("👤 Name")
            email = st.text_input("📧 Email")

        with col2:
            age = st.number_input(
                "🎂 Age",
                min_value=16,
                max_value=100,
                step=1
            )

        gender = st.radio(
            "🚻 Gender",
            ["Male", "Female", "Others"],
            horizontal=True
        )

        password = st.text_input(
            "🔒 Password",
            type="password"
        )

        submitted = st.form_submit_button(
            "🚀 Create Account",
            use_container_width=True
        )

with right:

    st.markdown("""
<div class="feature-box">

## ✈️ Features

🛫 Live Flight Tracking

🌍 Airport Information

🕒 Flight Status

📍 Route Details

☁️ Weather Updates

📊 Aviation Statistics

🔜 Flight Delay Prediction

🔜 Airline Analytics

</div>
""", unsafe_allow_html=True)
    
if submitted:

    name = name.strip()
    email = email.strip().lower()

    if not name:
        st.error("Please enter your name.")

    elif not email:
        st.error("Please enter your email.")

    elif database.email_exists(email):
        st.error("Email already exists.")

    elif len(password) < 6:
        st.error("Password must contain at least 6 characters.")

    elif age < 16:
        st.error("Age must be at least 16.")

    else:
        user = User(name, email, age, gender, password)
        user.send_to_database()

        st.session_state["logged_in"] = True
        st.session_state["username"] = name

        st.success("🎉 Registration Successful!")
        st.balloons()

        st.switch_page("pages/dashboard.py")

st.markdown(
    "<div class='footer'>Made with ❤️ by Nishant Ladwal </div>",
    unsafe_allow_html=True,
)
