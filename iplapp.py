import streamlit as st
import pandas as pd
from Team_Selection import *
st.set_page_config(
    page_title="IPL Team Selection",
    page_icon="https://bl-i.thgim.com/public/incoming/1ogk5e/article25940328.ece/alternates/FREE_1200/IPL-400x400jpg",
    layout="wide",
)

base="dark"
primaryColor="#3fe682"
backgroundColor="#000000"
secondaryBackgroundColor="#9055d6"
font="monospace"


original_title = '<h1 style="font-family: monospace; color:cyan; font-size: 60px;">IPL Team Selection </h1>'
st.markdown(original_title, unsafe_allow_html=True)
st.markdown(
    """
    ## Welcome to IPL Team Selection! Select your players and playing ground from the options below.
    """
)

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://wallpapercave.com/wp/wp7486102.jpg");
    background-size: 100vw 100vh; 
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""
st.markdown(background_image, unsafe_allow_html=True)
batting_teams,all_rounders, bowling_teams, grounds = get_datas()

col1, col2,col3,col4= st.columns(4)

with col1:
    batsman = st.multiselect(' Select Batsman', sorted(batting_teams))
    selected_batters = list(batsman)


with col2:
    all_rounder = st.multiselect(' Select All Rounder', sorted(all_rounders))
    selected_allrounder = list(all_rounder)
    

with col3:
    bowler=st.multiselect('Select Bowlers',sorted(bowling_teams))
    selected_bowler = list(bowler)

with col4:
        ground = st.selectbox(' Select Playing Ground', sorted(grounds))
if st.button("Result"):
    st.write("Playing Ground:", ground)
    selected_batters,selected_all_rounders,selected_bowlers = selection(selected_batters, selected_allrounder, selected_bowler, ground)
    selected_players = {
        "Batsmen": selected_batters,
        "All-Rounders": selected_all_rounders,
        "Bowlers": selected_bowlers
    }

    all_selected_players = []

    for players in selected_players.values():
        all_selected_players.extend(players)

    st.write("Selected Players:")
    st.write(pd.DataFrame(all_selected_players, columns=["Selected Players"]))







