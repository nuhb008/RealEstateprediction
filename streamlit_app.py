import streamlit as st


# --- PAGE SETUP ---
about_page = st.Page(
    "Client/app.js",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)




# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        #"Projects": [project_1_page, project_2_page],
    }
)




# --- RUN NAVIGATION ---
pg.run()