from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Button('Entrar')]
]

# Janela
Janela = sg.Window('Tela de Login', layout)

# Ler os eventos
while True:
    eventos, valores = Janela.read()  # Alterado para 'Janela' (com "J" maiúsculo)
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'João' and valores['senha'] == '123456':
            print('Bem-vindo ao Loss Control')
