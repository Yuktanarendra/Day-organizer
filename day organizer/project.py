import streamlit as st

# Initialize the task list in session state
if 'tasks' not in st.session_state:
    st.session_state['tasks'] = []

# Function to add a task
def add_task():
    st.markdown("### Add a New Task")
    st.markdown("#### 📋 Enter the details below:")
    task_description = st.text_input("📝 Task Description", key="task_input")
    task_time = st.text_input("⏰ Task Time (e.g., '2:00 PM')", key="time_input")
    
    if st.button("Add Task"):
        if task_description and task_time:
            task = {"description": task_description, "time": task_time}
            st.session_state['tasks'].append(task)
            st.success(f'✅ Task "{task_description}" scheduled at {task_time} has been added.')
        else:
            st.error("❗ Both task description and time are required!")

# Function to view all tasks
def view_tasks():
    st.markdown("### Your Task List 📝")
    if len(st.session_state['tasks']) == 0:
        st.warning("Your to-do list is empty. Start by adding tasks!")
    else:
        st.write("#### Here are your current tasks:")
        for index, task in enumerate(st.session_state['tasks']):
            st.markdown(f"*{index + 1}. {task['description']}* (Scheduled at: *{task['time']}*)")
    st.divider()

# Function to delete a task
def delete_task():
    st.markdown("### Delete a Task 🗑️")
    if len(st.session_state['tasks']) == 0:
        st.warning("Your to-do list is empty. Nothing to delete.")
    else:
        task_to_delete = st.selectbox("Select a task to delete", options=range(1, len(st.session_state['tasks']) + 1))
        if st.button("Delete Task"):
            removed_task = st.session_state['tasks'].pop(task_to_delete - 1)
            st.success(f'🗑️ Task "{removed_task["description"]}" scheduled at {removed_task["time"]} has been removed.')

# Function to edit a task
def edit_task():
    st.markdown("### Edit a Task ✏️")
    if len(st.session_state['tasks']) == 0:
        st.warning("Your to-do list is empty. Nothing to edit.")
    else:
        task_to_edit = st.selectbox("Select a task to edit", options=range(1, len(st.session_state['tasks']) + 1))
        selected_task = st.session_state['tasks'][task_to_edit - 1]
        
        new_description = st.text_input("✏️ Edit task description", selected_task['description'], key="edit_description")
        new_time = st.text_input("⏰ Edit task time", selected_task['time'], key="edit_time")
        
        if st.button("Update Task"):
            if new_description and new_time:
                st.session_state['tasks'][task_to_edit - 1] = {"description": new_description, "time": new_time}
                st.success(f'🔄 Task {task_to_edit} has been updated.')
            else:
                st.error("❗ Both description and time must be filled!")

# Main function
def main():
    # Test to ensure Streamlit is working
    st.write("Hello, Streamlit is working!")  # This should display at the top of your app

    # Application Title
    st.title("📝 To-Do List Application with Scheduling ⏰")

    # Sidebar navigation
    st.sidebar.markdown("## Menu")
    option = st.sidebar.selectbox("Choose an action", ["View Tasks", "Add Task", "Edit Task", "Delete Task"])
    
    # Sidebar debug
    st.sidebar.write(f"Selected option: {option}")  # Ensure option is being correctly passed

    # Displaying the selected action
    if option == "Add Task":
        add_task()
    elif option == "View Tasks":
        view_tasks()
    elif option == "Delete Task":
        delete_task()
    elif option == "Edit Task":
        edit_task()

if __name__ == "__main__":
    main()