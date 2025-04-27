import os
import uuid
import streamlit as st

# Função para obter o caminho do arquivo de tarefas do usuário
def get_user_filepath():
    """Retorna o caminho do arquivo de dados único para cada usuário."""
    user_id = str(uuid.uuid4())  # Gera um identificador único
    return f"todos_{user_id}.txt"

# Função para carregar as tarefas do arquivo específico do usuário
def get_todos():
    """Carrega a lista de tarefas do arquivo de dados único do usuário."""
    filepath = get_user_filepath()
    if not os.path.exists(filepath):
        return []  # Retorna uma lista vazia se o arquivo não existir
    with open(filepath, 'r', encoding="utf-8") as file:
        todos = file.readlines()
    return [todo.strip() for todo in todos]  # Remove quebras de linha

# Função para salvar as tarefas no arquivo específico do usuário
def write_todos(todos):
    """Grava a lista de tarefas no arquivo de dados único do usuário."""
    filepath = get_user_filepath()
    with open(filepath, 'w', encoding="utf-8") as file:
        for todo in todos:
            file.write(f"{todo}\n")

# Inicializa a lista de tarefas no session_state se não estiver presente
if "todos" not in st.session_state:
    st.session_state.todos = get_todos()

def add_todo():
    """Adiciona uma nova tarefa à lista e atualiza o session_state."""
    new_todo = st.session_state["new_todo"].strip()
    if new_todo:
        st.session_state.todos.append(new_todo)
        write_todos(st.session_state.todos)
        st.session_state["new_todo"] = ""  # Limpa o campo de entrada

# Título e descrição do aplicativo
st.title("Minha Lista de Tarefas")
st.subheader("Esta é a minha lista de tarefas.")

# Exibe as tarefas com caixas de seleção
for index, todo in enumerate(st.session_state.todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        st.session_state.todos.pop(index)
        write_todos(st.session_state.todos)
        st.rerun()

# Campo de entrada para adicionar novas tarefas
st.text_input("Adicionar nova tarefa", key="new_todo", on_change=add_todo)
