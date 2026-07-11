import FreeSimpleGUI as sg

sg.theme("Reddit")

label = sg.Text("This is a to-do app")
ibox = sg.InputText(tooltip="Enter todo :-")
add_button = sg.Button("Add")

layout = [[label],[ibox,add_button]]

window = sg.Window("Todo App",layout=layout,font=('Calibara',20))

window.read()
window.close()