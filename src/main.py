import PySimpleGUI as sg
import os

inputColumn = [[sg.Push(), sg.Text("Visualizador de imagens usando PyGUI"), sg.Push()],
               [sg.Text('Insira o diretório com as imagens'), sg.InputText(size=(25,1), key='NOME_DIRETORIO'), sg.Button('Enviar', key='INSERIR_DIRETORIO')],
               [sg.Listbox(values=[], size=(53,6), key='SELECIONAR_IMAGEM', enable_events=True)],
               [sg.Text(size=29, key='DIRETORIO_ERROR')]]

imageColumn = [[sg.Text('Selecione uma imagem da lista na esquerda!')],
               [sg.Image(key='IMAGEM_SELECIONADA')]]

layout = [[sg.Column(inputColumn), sg.VSeperator(), sg.Column(imageColumn)]]

window = sg.Window(title="Image viewer", layout=layout)

nomeDiretorio = []

while True:

    event, values = window.read()
    window['DIRETORIO_ERROR'].update('')

    if(event == sg.WIN_CLOSED):
        break

    print(event)

    if(event == 'INSERIR_DIRETORIO'):

        nomeDiretorio = values['NOME_DIRETORIO']

        try:

            arquivos = os.listdir(nomeDiretorio)
            window['SELECIONAR_IMAGEM'].update(values=arquivos)

        except:
            window['DIRETORIO_ERROR'].update("Diretório incorreto inserido!")
    
    elif(event == 'SELECIONAR_IMAGEM'):

        imagemSelecionada = nomeDiretorio + '/' + values['SELECIONAR_IMAGEM'][0]
        print(imagemSelecionada)
        window['IMAGEM_SELECIONADA'].update(imagemSelecionada)


window.close()