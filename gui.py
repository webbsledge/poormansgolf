import PySimpleGUI as sg
import time
import os

# check if data store exists
if not os.path.exists("feed.csv"):
    with open("feed.csv", "w") as file:
        pass

# change the theme
sg.theme('DarkGray')

# main window elements
clock = sg.Text('', key='clock')
label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter your to-do', key='todo')
list_box = sg.Listbox(values=functions.read_todos(), key='todo_list',
                      enable_events=True, size=(45, 10))
# buttons
add_button = sg.Button(
                       # button_text='Add',
                       key="Add",
                       tooltip='Add',
                       image_source="assets/add.png",
                       size=2,
                       mouseover_colors="LightBlue2")
clear_button = sg.Button('Clear')
edit_button = sg.Button('Edit')
complete_button = sg.Button(
                            # button_text='Complete',
                            key="Complete",
                            tooltip='Complete',
                            image_source="assets/complete.png",
                            size=2,
                            mouseover_colors="LightBlue2")
exit_button = sg.Button('Exit')

# layout
layout = [[clock],
          [label],
          [input_box, add_button, complete_button],
          [list_box],
          [edit_button, clear_button, exit_button]]

# main window definitions
window = sg.Window('My To-Do App',
                   layout=layout,
                   font=('Helvetica', 18))

# event cases for button presses
while True:
    event, values = window.read(timeout=1000)
    window["clock"].update(value=time.strftime("%d/%m/%Y %H:%M:%S"))
#    print(1, event)
#    print(2, values)
#    print(3, values['todo_list'])
    match event:
        case 'Add':
            todos = functions.read_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todo_list'].update(values=todos)
            window['todo'].update(value="")
        case 'Clear':
            window['todo'].update(value="")
        case 'Edit':
            try:
                todo_to_edit = values['todo_list'][0]
                new_todo = values['todo']
                todos = functions.read_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todo_list'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 18))
        case 'Complete':
            try:
                todo_to_complete = values['todo_list'][0]
                todos = functions.read_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todo_list'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 18))
        case 'todo_list':
            window['todo'].update(value=values['todo_list'][0])
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()
