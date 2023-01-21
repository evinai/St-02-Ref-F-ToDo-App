import streamlit as st
import functions

st.set_page_config(page_title="My Todo App", page_icon=":memo:", layout="centered", initial_sidebar_state="auto")
st.markdown("""
<style>
.big-font {
    font-size:50px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">My ToDo App !!</p>', unsafe_allow_html=True)


# 1. App title and description
st.subheader("This is my todo app")
st.write("This is a todo app that I made using streamlit")

# 2.Get the todos from the file
todos = functions.get_todos()


# 3. Get the new to do from the user and add it to the todos
def add_todo():
    todo_var = st.session_state["new_todo"]
    if todo_var != "":
        todos.append(todo_var + "\n")
        functions.write_todos(todos)
    else:
        pass


# 4. Create checkboxes for each to do
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

# 5. Create text input for the new to do and a onchange function to add it to the todos
st.text_input(label="",
              placeholder="Enter a new to do",
              key="new_todo",
              on_change=add_todo)

st.session_state
