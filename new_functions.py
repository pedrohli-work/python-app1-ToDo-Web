import streamlit as st

# Refactored function to retrieve todos from session state
def get_todos():
    """Retrieve the list of todos from Streamlit's session state."""
    if "todos" not in st.session_state:
        st.session_state.todos = []  # Initialize an empty list if no todos are found
    return st.session_state.todos

# Refactored function to write todos to session state (no file writing)
def write_todos(todos_arg):
    """Save the list of todos to session state."""
    st.session_state.todos = todos_arg  # Store the list in session state


