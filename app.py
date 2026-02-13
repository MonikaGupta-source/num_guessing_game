import streamlit as st
import random

st.set_page_config(page_title="Number Guessing Game", page_icon="🎯")

st.title("🎯 Number Guessing Game")
st.write("Guess a number between 1 and 100")

# Initialize session state
if "computer_guess" not in st.session_state:
    st.session_state.computer_guess = random.randint(1, 100)
    st.session_state.tries = 0
    st.session_state.game_over = False

# Input from user
user_guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Submit Guess") and not st.session_state.game_over:
    st.session_state.tries += 1

    if user_guess < st.session_state.computer_guess:
        st.warning("🔼 Guess Higher!")
    elif user_guess > st.session_state.computer_guess:
        st.warning("🔽 Guess Lower!")
    else:
        st.success(f"🎉 Correct! You guessed it in {st.session_state.tries} tries.")
        st.session_state.game_over = True

# Restart button
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.computer_guess = random.randint(1, 100)
        st.session_state.tries = 0
        st.session_state.game_over = False
        st.experimental_rerun()
