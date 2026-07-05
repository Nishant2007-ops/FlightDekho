import pandas as pd

AIRLINES = {
    "AI": "Air India",
    "6E": "IndiGo",
    "SG": "SpiceJet",
    "UK": "Akasa Air",
    "IX": "Air India Express",
    "QP": "Akasa Air Express",
    "I5": "AirAsia India",
    "G8": "Go First",
    "EK": "Emirates",
    "EY": "Etihad Airways",
    "QR": "Qatar Airways",
    "SV": "Saudia",
    "KU": "Kuwait Airways",
    "GF": "Gulf Air",
    "WY": "Oman Air",
    "RJ": "Royal Jordanian",
    "BA": "British Airways",
    "LH": "Lufthansa",
    "AF": "Air France",
    "KL": "KLM",
    "LX": "Swiss International Air Lines",
    "OS": "Austrian Airlines",
    "IB": "Iberia",
    "AZ": "ITA Airways",
    "AY": "Finnair",
    "SK": "Scandinavian Airlines",
    "TP": "TAP Air Portugal",
    "EI": "Aer Lingus",
    "AA": "American Airlines",
    "DL": "Delta Air Lines",
    "UA": "United Airlines",
    "WN": "Southwest Airlines",
    "AS": "Alaska Airlines",
    "B6": "JetBlue Airways",
    "AC": "Air Canada",
    "WS": "WestJet",
    "SQ": "Singapore Airlines",
    "CX": "Cathay Pacific",
    "TG": "Thai Airways",
    "MH": "Malaysia Airlines",
    "JL": "Japan Airlines",
    "NH": "All Nippon Airways",
    "KE": "Korean Air",
    "OZ": "Asiana Airlines",
    "CI": "China Airlines",
    "BR": "EVA Air",
    "CZ": "China Southern Airlines",
    "MU": "China Eastern Airlines",
    "CA": "Air China"
}

def flight_dataframe(data):

    rows = []

    for flight in data["response"]:

        # Skip codeshare duplicates
        if flight.get("cs_flight_iata") is not None:
            continue

        airline_code = flight.get("airline_iata")
        airline_name = AIRLINES.get(airline_code, airline_code)

        rows.append({

            "Airline": airline_name,

            "Flight": flight.get("flight_iata"),

            "From": flight.get("dep_iata"),

            "To": flight.get("arr_iata"),

            "Departure": flight.get("dep_time"),

            "Arrival": flight.get("arr_time"),

            "Status": flight.get("status"),

            "Terminal": flight.get("dep_terminal"),

            "Gate": flight.get("dep_gate"),

            "Duration": flight.get("duration"),

            "Delay": flight.get("delayed")

        })

    return pd.DataFrame(rows)
