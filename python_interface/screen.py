from PySimpleGUI import PySimpleGUI as sg

class ScreenPython:
    def __init__(self):
        #Tema
        sg.change_look_and_feel('LightGrey1')
        #Layout
        layout = [
            [sg.Text('Name', size=(5,0)), sg.Input(size=(15,0), key='name')],
            [sg.Text('Age', size=(5,0)), sg.Input(size=(15,0), key='age')],
            [sg.Text('Which email providers are accepted?')],
            [sg.Checkbox('Gmail',key='gmail'), sg.Checkbox('Outlook',key='outlook'), sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Text('Accept card')],
            [sg.Radio('Yes', 'cards', key='accepted_card'), sg.Radio('No', 'cards', key='not_accept_card')],
            [sg.Slider(range=(0,255), default_value=0, orientation='h', size=(15,20), key='slider_speed')],
            [sg.Button('Send data')],
            [sg.Output(size=(30,20))]
        ]
        #Janela
        self.window = sg.Window('User data').layout(layout)

    def Start(self):
        
        while True:
            #Extrair dados da tela
            self.button, self.values = self.window.Read()
            name = self.values['name']
            age = self.values['age']
            accepted_gmail = self.values['gmail']
            accepted_outlook = self.values['outlook']
            accepted_yahoo = self.values['yahoo']
            accepted_card = self.values['accepted_card']
            not_accept_card = self.values['not_accept_card']
            speed_script = self.values['slider_speed']
            print(f'Name: {name}')
            print(f'Age: {age}')
            print(f'Accepted Gmail: {accepted_gmail}')
            print(f'Accepted Outlook: {accepted_outlook}')
            print(f'Accepted Yahoo: {accepted_yahoo}')
            print(f'Accepted card: {accepted_card}')
            print(f'Not accept card: {not_accept_card}')
            print(f'Speed of scripts: {speed_script} \n')

screen = ScreenPython()
screen.Start()