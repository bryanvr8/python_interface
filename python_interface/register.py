from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('User'), sg.Input(key='user', size=(20,1))],
    [sg.Text('Password'), sg.Input(key='password', password_char='*', size=(20,1))],
    [sg.Checkbox('Save login?')],
    [sg.Button('Enter')]
]
#Janela
window = sg.Window('Login screen', layout)
#Ler eventos
while True:
    events, values = window.read()
    if events == sg.WINDOW_CLOSED:
        break
    if events == 'Enter':
        if values['user'] == 'Bryan' and values['password'] == '123':
            print('Login successful!')