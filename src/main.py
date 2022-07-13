import PySimpleGUI as sg

inputColumn = [[sg.Push(), sg.Text("Visualizador de imagens usando PyGUI"), sg.Push()],
               [sg.Text('Insira o diretório com as imagens'), sg.InputText(), sg.Button('Enviar', key='INSERIR_DIRETORIO')],
               [sg.Listbox(values=[], size=(30,6))]]

imageColumn = [[sg.Text('Selecione uma imagem da lista na esquerda!')]]

layout = [[sg.Column(inputColumn)],
          [sg.VSeparator()],
          [sg.Column(imageColumn)]]

window = sg.Window(title="Image viewer", layout=layout)

while True:

    event, values = window.read()

    if(event == 'INSERIR_DIRETORIO'):
        print(values[0])

    break

window.close()