import FreeSimpleGUI as sg
from backend import get_todos,set_todos

sg.theme("Reddit")

label = sg.Text("This is a to-do app")
ibox = sg.InputText(tooltip="Enter todo :-",key='ibox')
add_button = sg.Button("Add")
layout = [[label],[ibox,add_button]]
window = sg.Window("Todo App",layout=layout,font=('Calibara',10))

while True:
    event,values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = get_todos()
            add_value = values['ibox'] + '\n'
            todos.append(add_value)
            set_todos(todos)
        case sg.WINDOW_CLOSED:
            exit()


window.read()
window.close()