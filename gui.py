import FreeSimpleGUI as sg
from backend import get_todos,set_todos
import time

sg.theme("Reddit")
label = sg.Text("This is a to-do app")
ibox = sg.InputText(tooltip="Enter todo :-",key='ibox')
add_button = sg.Button(key="Add",image_filename="add.png",
                       mouseover_colors='red',size=10,tooltip="Add Button")
list_box = sg.Listbox(values=get_todos(),key='lbox',enable_events=True
                      ,size=(45,10))
edit_button = sg.Button("Edit",mouseover_colors='red')
time_text = sg.Text(key="twidget",text_color='blue')
c_button = sg.Button(key="Complete",image_filename="complete.png",mouseover_colors='red')
e_button = sg.Button("Exit",mouseover_colors='red')


layout = [[time_text],[label],[ibox,add_button],[list_box,edit_button]
    ,[c_button,e_button]]
window = sg.Window("Todo App",layout=layout,font=('Calibara',10))

while True:
    event,values = window.read(timeout=200)
    timeval = time.strftime("%I:%M:%S %p")
    window['twidget'].update(value=timeval)
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
            except IndexError:
                sg.popup("Please select a value to edit")
        case 'lbox':
            window['ibox'].update(value=values['lbox'][0])
        case 'Complete':
            try:
                todos = get_todos()
                todo_complete = values['lbox'][0]
                todos.remove(todo_complete)
                set_todos(todos)
                window['lbox'].update(values=todos)
                window['ibox'].update(value='')
            except IndexError:
                sg.popup("Please select a value to complete first")
        case 'Exit':
            exit()
        case sg.WINDOW_CLOSED:
            break



window.close()