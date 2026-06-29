# ✈️ FlightDekho

FlightDekho is a modern flight search web application built using **Python** and **Streamlit**. It enables users to create an account, log in securely, and search for real-time flight information through an aviation API. The project combines user authentication, database management, API integration, and an intuitive web interface into a single application.

This project was developed as my **CS50P (CS50's Introduction to Programming with Python) Final Project**, demonstrating practical Python programming skills and the integration of multiple technologies.

---

## Features

* 🔐 Secure user registration and login
* 🔒 Password hashing using `bcrypt`
* 🗄️ SQLite database for user management
* ✈️ Real-time flight search using an aviation API
* 🛫 Airport selection using airport codes
* 📊 Clean presentation of flight information
* 🎨 Modern and responsive Streamlit interface
* ⚠️ User-friendly error handling and validation

---

## Technologies Used

* Python 3
* Streamlit
* SQLite
* Pandas
* Requests
* bcrypt
* Aviation API

---

## Project Structure

```text
FlightDekho/
│
├── code.py                # Main application
├── api.py                 # Handles API requests
├── parser.py              # Processes API responses
├── database.py            # Database functions
├── airports.py            # Airport code data
├── air_users.db           # SQLite database (generated locally)
├── pages/
│   └── dashboard.py       # Dashboard page
├── assets/                # Images and logos (if applicable)
├── requirements.txt
├── README.md
└── .streamlit/
    └── secrets.toml       # Local API secrets (not committed)
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/FlightDekho.git
cd FlightDekho
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your API key

Create a `.streamlit/secrets.toml` file:

```toml
API_KEY = "YOUR_API_KEY"
```

Replace `YOUR_API_KEY` with your own API key.

### 4. Run the application

```bash
streamlit run code.py
```

The application will open automatically in your browser.

---

## How It Works

1. Register a new account.
2. Log in securely using your credentials.
3. Choose departure and destination airports.
4. Submit your search request.
5. FlightDekho retrieves flight data from the aviation API.
6. The application processes and displays the results in a user-friendly format.

---

## Security

* Passwords are never stored in plain text.
* User passwords are hashed using `bcrypt`.
* API keys are stored in Streamlit Secrets and are not uploaded to GitHub.
* Sensitive files such as databases and secret keys are excluded using `.gitignore`.

---

## Future Improvements

Some features planned for future versions include:

* ❤️ Favorite routes
* 📅 Flight history
* 🌍 Interactive route maps
* 💸 Fare comparison charts
* 🔔 Flight price alerts
* 🤖 AI-powered travel recommendations
* 📱 Mobile-responsive enhancements
* 🌙 Dark mode

---

## Lessons Learned

This project helped me gain practical experience with:

* Object-Oriented Programming
* API integration
* SQLite database management
* User authentication
* Password hashing
* Data processing using Pandas
* Streamlit application development
* Git and GitHub
* Deploying Python web applications

---

## Author

**Nishant LADWAL**

Student, Mathematics and Computing
Indian Institute of Technology (IIT) Ropar

---
