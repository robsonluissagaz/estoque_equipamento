import os
import shutil
import PySimpleGUI as sg

caminho_da_pasta = os.path.join(os.path.expanduser("~"), "Documents", "Estoque_TI")
os.makedirs(caminho_da_pasta, exist_ok=True)

def menu():
    layout = [
        [sg.Text('Selecione uma opção:')],
        [sg.Button('Cadastrar Equipamento'), sg.Button('Verificar Equipamentos')],
        [sg.Button('Excluir Equipamento'), sg.Button('Inserir Nota Fiscal')],
        [sg.Button('Fechar Programa')]
    ]
    
    window = sg.Window('Menu Principal', layout)

    while True:
        event, _ = window.read()
        if event in (sg.WIN_CLOSED, 'Fechar Programa'):
            break
        elif event == 'Cadastrar Equipamento':
            cadastro()
        elif event == 'Verificar Equipamentos':
            verificar()
        elif event == 'Excluir Equipamento':
            excluir()
        elif event == 'Inserir Nota Fiscal':
            fiscal()
    
    window.close()

def cadastro():
    layout = [
        [sg.Text('Nome do Equipamento'), sg.Input(key='nome')],
        [sg.Text('Setor do Equipamento'), sg.Input(key='setor')],
        [sg.Text('Usuário'), sg.Input(key='usuario')],
        [sg.Text('Serial Key'), sg.Input(key='serial')],
        [sg.Text('Componente'), sg.Input(key='componente')],
        [sg.Text('Observação'), sg.Input(key='observacao')],
        [sg.Button('Finalizar')]
    ]
    
    window = sg.Window('Cadastro de Equipamento', layout)
    componentes = []
    observacoes = []

    while True:
        event, values = window.read()
        
        # Fecha a janela ao clicar em "Finalizar"
        if event == sg.WIN_CLOSED:
            break

        # Coletar dados ao clicar em "Finalizar"
        if event == 'Finalizar':
            nome = values['nome'].upper().strip()
            setor = values['setor'].upper().strip()
            usuario = values['usuario'].upper().strip()
            serial = values['serial'].upper().strip()
            componente = values['componente'].upper().strip()
            observacao = values['observacao'].upper().strip()

            # Validação das informações
            if nome == '':
                sg.popup('Por favor, preencha o nome do equipamento.')
                window['nome'].set_focus()  # Coloca o foco no campo de nome
                continue
            if setor == '':
                sg.popup('Por favor, preencha o setor do equipamento.')
                window['setor'].set_focus()  # Coloca o foco no campo de setor
                continue
            if usuario == '':
                sg.popup('Por favor, preencha o usuário do equipamento.')
                window['usuario'].set_focus()  # Coloca o foco no campo de usuário
                continue
            if serial == '':
                sg.popup('Por favor, preencha o serial key do equipamento.')
                window['serial'].set_focus()  # Coloca o foco no campo de serial
                continue

            # Adicionar componentes e observações se fornecidos
            if componente:
                componentes.append(componente)
            if observacao:
                observacoes.append(observacao)

            # Após a coleta
            caminho_equipamento = os.path.join(caminho_da_pasta, nome)
            if os.path.exists(caminho_equipamento):
                sg.popup(f"O equipamento {nome} já está cadastrado.")
            else:
                os.makedirs(caminho_equipamento)
                arquivo_txt = os.path.join(caminho_equipamento, nome + '.txt')

                with open(arquivo_txt, 'w') as arquivo:
                    arquivo.write(f'Nome do equipamento: {nome}\n')
                    arquivo.write(f'Setor do equipamento: {setor}\n')
                    arquivo.write(f'Usuário: {usuario}\n')
                    arquivo.write(f'Serial Key: {serial}\n')
                    if componentes:
                        arquivo.write(f'Componentes: {", ".join(componentes)}\n')
                    if observacoes:
                        arquivo.write(f'Observações: {", ".join(observacoes)}\n')

                sg.popup(f"Equipamento {nome} registrado com sucesso.")
            break  # Fecha a janela após o cadastro bem-sucedido

    window.close()


def verificar():
    lista = os.listdir(caminho_da_pasta)
    if not lista:
        sg.popup('Nenhum equipamento cadastrado.')
        return

    layout = [
        [sg.Text('Escolha um equipamento:')],
        [sg.Listbox(values=lista, size=(30, 6), key='-EQUIPAMENTO-', select_mode=sg.LISTBOX_SELECT_MODE_SINGLE)],
        [sg.Button('Ver Detalhes'), sg.Button('Cancelar')]
    ]

    window = sg.Window('Verificar Equipamentos', layout)
    event, values = window.read()
    window.close()

    if event == 'Ver Detalhes' and values['-EQUIPAMENTO-']:
        equipamento_escolhido = values['-EQUIPAMENTO-'][0]
        os.startfile(os.path.join(caminho_da_pasta, equipamento_escolhido, f'{equipamento_escolhido}.txt'))

def excluir():
    lista = os.listdir(caminho_da_pasta)
    if not lista:
        sg.popup('Nenhum equipamento cadastrado.')
        return

    layout = [
        [sg.Text('Escolha um equipamento para excluir:')],
        [sg.Listbox(values=lista, size=(30, 6), key='-EQUIPAMENTO-', select_mode=sg.LISTBOX_SELECT_MODE_SINGLE)],
        [sg.Button('Excluir'), sg.Button('Cancelar')]
    ]

    window = sg.Window('Excluir Equipamentos', layout)
    event, values = window.read()
    window.close()

    if event == 'Excluir' and values['-EQUIPAMENTO-']:
        equipamento_escolhido = values['-EQUIPAMENTO-'][0]
        caminho_pasta = os.path.join(caminho_da_pasta, equipamento_escolhido)
        shutil.rmtree(caminho_pasta)
        sg.popup(f'O equipamento {equipamento_escolhido} foi excluído com sucesso.')

def fiscal():
    pastas = os.listdir(caminho_da_pasta)
    if not pastas:
        sg.popup("Nenhum equipamento cadastrado.")
        return

    layout = [
        [sg.Text("Equipamentos cadastrados:")],
        [sg.Listbox(values=pastas, size=(30, 6), key='-Pasta-', select_mode=sg.LISTBOX_SELECT_MODE_SINGLE)],
        [sg.Button('Selecionar'), sg.Button('Cancelar')]
    ]
    
    window = sg.Window('Selecionar Equipamento', layout)
    event, values = window.read()
    window.close()

    if event == 'Selecionar' and values['-Pasta-']:
        pasta_equipamento = values['-Pasta-'][0]
        caminho_equipamento = os.path.join(caminho_da_pasta, pasta_equipamento)

        layout_pdf = [
            [sg.Text("Selecione o arquivo PDF da nota fiscal:")],
            [sg.Input(), sg.FileBrowse(file_types=(("PDF Files", "*.pdf"),))],
            [sg.Button('Inserir'), sg.Button('Cancelar')]
        ]

        window_pdf = sg.Window('Selecionar Nota Fiscal', layout_pdf)
        event_pdf, values_pdf = window_pdf.read()
        window_pdf.close()

        if event_pdf == 'Inserir' and values_pdf[0]:
            caminho_pdf = values_pdf[0]
            try:
                shutil.move(caminho_pdf, os.path.join(caminho_equipamento, os.path.basename(caminho_pdf)))
                sg.popup(f"Nota fiscal inserida com sucesso na pasta do equipamento {pasta_equipamento}.")
            except Exception as e:
                sg.popup(f"Erro ao inserir a nota fiscal: {e}")
        else:
            sg.popup("Arquivo inválido ou operação cancelada.")

menu()
