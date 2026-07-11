import FreeSimpleGUI as sg
from backend import get_todos,set_todos

sg.theme("Reddit")

label = sg.Text("This is a to-do app")
ibox = sg.InputText(tooltip="Enter todo :-",key='ibox')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=get_todos(),key='lbox',enable_events=True
                      ,size=(45,10))
edit_button = sg.Button("Edit")

layout = [[label],[ibox,add_button],[list_box,edit_button]]
window = sg.Window("Todo App",layout=layout,font=('Calibara',10))

while True:
    event,values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            try:
                todos = get_todos()
                add_value = values['ibox'] + '\n'
                todos.append(add_value)
                set_todos(todos)
                window['lbox'].update(values=todos)
                window['ibox'].update(value='')
            except ValueError:
                sg.popup("Please enter a value to add")
        case "Edit":
            try:
                todos = get_todos()
                edit_item = values['lbox'][0]
                edit_index = todos.index(edit_item)
                new_value = values['ibox']+'\n'
                todos[edit_index] = new_value
                set_todos(todos)
                window['lbox'].update(values=todos)
                window['ibox'].update(value='')
            except ValueError:
                sg.popup("Please enter a value to edit")
        case 'lbox':
            window['ibox'].update(value=values['lbox'][0])
        case sg.WINDOW_CLOSED:
            exit()


window.read()
window.close()