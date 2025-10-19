import streamlit as st
import requests

API_URL = "http://backend:8000"

st.title(" AI Ticket Resolver")

st.subheader("Create a New Ticket")
title = st.text_input("Ticket Title")
desc = st.text_area("Ticket Description")

if st.button("Submit Ticket"):
    payload = {"title": title, "description": desc}
    response = requests.post(f"{API_URL}/tickets/", json=payload)
    if response.status_code == 200:
        st.success(" Ticket processed successfully!")
        data = response.json()["data"]
        st.json(data)
    else:
        st.error(" Failed to submit ticket.")

st.divider()
st.subheader("All Tickets")

if st.button("Load Tickets"):
    resp = requests.get(f"{API_URL}/tickets/")
    if resp.status_code == 200:
        tickets = resp.json()
        st.json(tickets)
