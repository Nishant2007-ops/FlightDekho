import pandas as pd

def flight_dataframe(data):

    rows = []

    for flight in data["response"]:

        # Skip codeshare duplicates
        if flight.get("cs_flight_iata") is not None:
            continue

        rows.append({

            "Airline": flight.get("airline_iata"),

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
