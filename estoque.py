import os
import shutil
import PySimpleGUI as sg

caminho_da_pasta = os.path.join(os.path.expanduser("~"), "Documents", "Estoque_TI")
os.makedirs(caminho_da_pasta, exist_ok=True)

def menu():
    while True:
        resp = input('''[1] Cadastrar equipamento
[2] Verificar equipamentos cadastrados
[3] Excluir equipamento
[4] Inserir nota fiscal
[5] Fechar programa
Digite a opção desejada: ''')
        
        if resp == '1':
            cadastro()
        elif resp == '2':
            verificar()
        elif resp == '3':
            excluir()
        elif resp == '4':
            fiscal()
        elif resp == '5':
            print('Fechando programa')
            break
        else:
            print('Opção inválida. Tente novamente.')

def cadastro():
    resp = input('Digite o nome do equipamento ou [M] para retornar ao menu: ').upper().strip()
    if resp == 'M':
        return
    
    caminho_equipamento = os.path.join(caminho_da_pasta, resp)
    
    if os.path.exists(caminho_equipamento):
        print(f"O equipamento {resp} já está cadastrado.")
        return
    
    os.makedirs(caminho_equipamento)
    arquivo_txt = os.path.join(caminho_equipamento, resp + '.txt')

    with open(arquivo_txt, 'w') as arquivo:
        arquivo.write(f'Nome do equipamento: {resp}\n')
        setor = input('Digite o setor do equipamento: ').upper().strip()
        arquivo.write(f'Setor do equipamento: {setor}\n')
        user = input('Digite o usuário do equipamento: ').upper().strip()
        arquivo.write(f'Usuário: {user}\n')
        key = input('Digite o serial key: ').upper().strip()
        arquivo.write(f'Serial Key: {key}\n')
        
        componente = []
        while True:
            componente.append(input('Digite o nome do componente: ').upper().strip())
            if input('Mais algum componente?[S/N]: ').upper().strip() == 'N':
                break
        arquivo.write(f'Componentes: {", ".join(componente)}\n')

        obs = []
        while True:
            obs.append(input('Digite uma observação: ').upper().strip())
            if input('Mais alguma observação?[S/N]: ').upper().strip() == 'N':
                break
        arquivo.write(f'Observação: {", ".join(obs)}\n')

    print(f"Equipamento {resp} registrado com sucesso.")

def verificar():
    lista = os.listdir(caminho_da_pasta)
    if not lista:
        print('Nenhum equipamento cadastrado.')
        return

    print('Escolha com o índice correspondente o equipamento que deseja verificar:')
    for l, n in enumerate(lista):
        print(f'ID_[{l}] {n}')
    
    resp = int(input('Digite o ID desejado: '))
    if 0 <= resp < len(lista):
        os.startfile(os.path.join(caminho_da_pasta, lista[resp], f'{lista[resp]}.txt'))
    else:
        print('ID inválido.')

def excluir():
    lista = os.listdir(caminho_da_pasta)
    if not lista:
        print('Nenhum equipamento cadastrado.')
        return

    print('Escolha com o índice correspondente o equipamento que deseja excluir:')
    for l, n in enumerate(lista):
        print(f'ID_[{l}] {n}')
    
    resp = int(input('Digite o ID desejado: '))
    if 0 <= resp < len(lista):
        caminho_pasta = os.path.join(caminho_da_pasta, lista[resp])
        shutil.rmtree(caminho_pasta)
        print(f'O equipamento {lista[resp]} foi excluído com sucesso.')
    else:
        print('ID inválido.')

def fiscal():
    pastas = os.listdir(caminho_da_pasta)
    if not pastas:
        print("Nenhum equipamento cadastrado.")
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
                print(f"Nota fiscal inserida com sucesso na pasta do equipamento {pasta_equipamento}.")
            except Exception as e:
                print(f"Erro ao inserir a nota fiscal: {e}")
        else:
            print("Arquivo inválido ou operação cancelada.")

menu()
