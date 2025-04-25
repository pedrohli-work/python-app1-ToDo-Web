import streamlit as st
import new_functions

# Initialize todos in session state if not already set
if "todos" not in st.session_state:
    # Load the todos from the functions (from session state)
    st.session_state.todos = new_functions.get_todos()  

def add_todo():
    """Add a new todo to the list and update session state."""
    new_todo = st.session_state["new_todo"].strip() + "\n"
    # Add new todo to session state
    st.session_state.todos.append(new_todo)
    # Save updated list back to session state  
    new_functions.write_todos(st.session_state.todos)
    # Clear the input field  
    st.session_state["new_todo"] = ""

# Set the main title and description of the app
st.title("My Todo App")
st.subheader("This is my todo app.")

# Loop through the todos and create checkboxes for each one
for index, todo in enumerate(st.session_state.todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        # Remove the completed to-do
        st.session_state.todos.pop(index)
        # Save updated list  
        new_functions.write_todos(st.session_state.todos)
        # Refresh the page to reflect the changes  
        st.rerun()  

# Input field for adding new to-dos
st.text_input(label="Add new To Do", placeholder="Press enter to add it.", on_change=add_todo, key='new_todo')
