import streamlit as st
from airports import AIRPORTS
from datetime import date
from api import search_flights
from parser import flight_dataframe
import pandas as pd

if not st.session_state.get("logged_in", False):
    st.warning("Please login first.")
    st.switch_page("code.py")
    st.stop()

st.markdown("""
<style>
.stApp {
    background-color: #F5F7FA;
}
</style>
""", unsafe_allow_html=True)

airport_list = sorted(list(AIRPORTS.keys()))

col1,col2 = st.columns([5,3])
with col1:
    st.markdown("""
    <h1 style="
    text-align:center;
    background: linear-gradient(to right, #1e90ff, #00c6ff);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;">
    Welcome to FlightDekho
    </h1>
    """, unsafe_allow_html=True)
    st.subheader("Search for any airline information ")
    #st.write("Every destination starts with one click . Find affordable flights and let your adventure take off.")
    st.markdown("""
    <p style='font-size:20px; color:#444444; text-align:center;'>
    Every destination starts with one click .<br>
    Find affordable flights and let your adventure take off.
    </p>
    """, unsafe_allow_html=True)

with col2: 
    st.image("flightdekho.png",width = 150)
    st.info("🌍 Search flights across the world")

st.image("0C6EBDB7-5059-4701-8199-65239178AF9B_4_5005_c.jpeg",width = 500)

user_name = st.session_state.get("username", "Guest")

st.subheader(f"Dear {user_name} ✈️")

with st.form("flight_search"):

    from_airport = st.selectbox("From", airport_list)
    to_airport = st.selectbox("To", airport_list)
    from_code = AIRPORTS[from_airport]
    to_code = AIRPORTS[to_airport]
    travel_date = st.date_input(
        "Travel Date",
        min_value=date.today()
    )

    submitted = st.form_submit_button(
        "🔍 Search Flights",
        use_container_width=True
    )

if submitted:

    with st.spinner("✈️ Searching for available flights..."):

        try:
            data = search_flights(from_code, to_code)
            df = flight_dataframe(data)

            if df.empty:
                st.warning("No flights found.")
                st.stop()

            st.success(f"Found {len(df)} flights")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("🛫 Flights", len(df))

            with col2:
                st.metric("From", from_code)

            with col3:
                st.metric("To", to_code)

            with col4:
                st.metric("Date", str(travel_date))

            st.divider()

            # ---------- Flight Cards ----------

            st.subheader("Available Flights")

            for _, row in df.iterrows():

                with st.container(border=True):

                    c1, c2, c3 = st.columns([3,3,2])

                    with c1:
                        st.markdown(f"### ✈️ {row['Airline']}")
                        st.write(f"**Flight:** {row['Flight']}")

                    with c2:
                        st.write(f"🛫 **Departure:** {row['Departure']}")
                        st.write(f"🛬 **Arrival:** {row['Arrival']}")

                    with c3:

                        status = row["Status"].lower()

                        if status == "scheduled":
                            st.success("🟢 Scheduled")

                        elif status == "active":
                            st.info("🔵 Active")

                        elif status == "delayed":
                            st.warning("🟡 Delayed")

                        elif status == "cancelled":
                            st.error("🔴 Cancelled")

                        else:
                            st.write(row["Status"])

            st.divider()

            with st.expander("📊 Show Detailed Table"):

                st.dataframe(
                    df,
                    use_container_width=True,
                    hide_index=True
                )

        except Exception as e:
            st.error(f"Unable to fetch flight data.\n\n{e}")

