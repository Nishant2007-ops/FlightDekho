# ✈️ FlightDekho

FlightDekho is a modern flight information web application built using **Python**, **Streamlit**, and **Supabase**. It enables users to create secure accounts, store user information in a cloud PostgreSQL database, and search for real-time flight information using an aviation API.

The project demonstrates full-stack Python development by combining user authentication, cloud database integration, API consumption, and an interactive web interface.

---

## Features

* 🔐 Secure user registration
* 🔒 Password hashing using `bcrypt`
* ☁️ Cloud database powered by **Supabase (PostgreSQL)**
* 📧 Email-based user accounts
* ✈️ Real-time flight information using an Aviation API
* 🛫 Airport selection using IATA airport codes
* 📊 Clean and responsive Streamlit interface
* ⚠️ User-friendly validation and error handling

---

## Technologies Used

* Python 3
* Streamlit
* Supabase (PostgreSQL)
* bcrypt
* Pandas
* Requests
* Aviation API
* Git & GitHub

---

## Project Structure

```text
FlightDekho/
│
├── code.py                  # Main application
├── api.py                   # Handles Aviation API requests
├── parser.py                # Processes API responses
├── database.py              # Database operations
├── supabase_client.py       # Supabase connection
├── airports.py              # Airport data
├── pages/
│   └── dashboard.py         # Dashboard page
├── .streamlit/
│   └── secrets.toml         # Local secrets (not committed)
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Nishant2007-ops/FlightDekho.git
cd FlightDekho
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Streamlit Secrets

Create the file:

```text
.streamlit/secrets.toml
```

Add your credentials:

```toml
Aviation_api_key = "YOUR_AVIATION_API_KEY"

SUPABASE_URL = "YOUR_SUPABASE_PROJECT_URL"
SUPABASE_KEY = "YOUR_SUPABASE_PUBLISHABLE_KEY"
```

> **Important:** Never commit `secrets.toml` to GitHub.

### 4. Run the application

```bash
streamlit run code.py
```

---

## How It Works

1. Users create an account with their name, email, age, gender, and password.
2. Passwords are securely hashed using `bcrypt`.
3. User information is stored in a Supabase PostgreSQL database.
4. Users can search for flight information.
5. FlightDekho fetches live flight data from the Aviation API.
6. Search results are displayed in an easy-to-read interface.

---

## Security

* Passwords are never stored in plain text.
* Passwords are hashed using `bcrypt`.
* API keys and Supabase credentials are stored in Streamlit Secrets.
* Sensitive files are excluded using `.gitignore`.

---

## Future Improvements

* 🔑 User login
* 🔐 Google Sign-In
* ❤️ Favourite airports
* 📜 Flight search history
* 📍 Saved routes
* 🌤 Weather information for destinations
* 📱 Improved mobile responsiveness
* 🌙 Dark mode
* 📈 Flight analytics dashboard

---

## Lessons Learned

This project helped me gain practical experience with:

* Object-Oriented Programming (OOP)
* REST API integration
* Cloud database management using Supabase
* Password hashing with `bcrypt`
* Streamlit web application development
* PostgreSQL fundamentals
* Git and GitHub
* Deploying Python applications

---

## Author

**Nishant Ladwal**

Mathematics and Computing
Indian Institute of Technology (IIT) Ropar

---

## License

This project is intended for educational and learning purposes.
