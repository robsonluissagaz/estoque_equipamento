# estoque_equipamento
Um programa que criei para controlar o estoque de equipamentos do departamento de TI para uma empresa.


## estoque.exe
Este é o arquivo que o usuário irá usar para controlar o estoque.


## estoque.py
Este arquivo contém todas as linhas de códigos que usei no projeto do programa.


## Instruções do programa
ao iniciar o programa pela primeira vez abrirá uma caixa interativa do módulo PySimpleGUI. Este módulo é usado para gerenciar arquivos no windows. Você deve se registrar no site para obter uma chave de acesso gratuita e poder usar o gerenciador de arquivos no programa.


### Funcionalidade 1 do programa
Nesta opção você fará o cadastro de um equipamento. Nesta opção o programa irá pedir informações como:

1. Nome do equipamento
2. Setor do equipamento
3. Usuário do equipamento
4. Serial key do equipamento
5. Componentes do equipamento. EX: COMUTADOR_SETOR_FISCAL = [CPU03, MONITOR01, TECLADO05, MOUSE02]
6. Observação do equipamento. EX: COMPUTADOR USADO PARA GERENCIAR NOTAS FISCAIS DA EMPRESA

ADD: Todas as opção podem ficar em branco se for do agrado do usuário, podendo ser adicionadas a qualquer momento na opção 2 do programa.


### Funcionalidade 2 do programa
Nesta opção você poderá verificar os equipamentos cadastrados no sistema, uma lista dos equipamentos aparecerá na tela, use os índices mostrados na tela para selecionar o equipamento que deseja analizar.

1. após você selecionar o equipamento, o programa automaticamente abrirá um arquivo txt que contém todas as informações inseridas na funcionalidade 1. Após o arquivo txt ser aberto você pode alterar ou remover informações do equipamento da maneira que quiser. Lembre-se de salvar as informações alteradas quando fechar o arquivo txt.


### Funcionalidade 3 do programa
Nesta opção o programa irá mostrar uma lista dos equipamentos cadastrados no sistema, use os índices mostrados na tela para excluir um equipamento do sistema. Esta ação não pode ser revertida, certifique-se antes de excluir um equipamento.


### Funcionalidade 4 do programa
Nesta opção você vinculará uma nota fiscal ao equipamento, útil se futuramente precisar revisar orçamentos dos mesmos.

1. Uma caixa interativa aparecerá mostrando uma lista dos equipamentos registrados no sistema, selecione o equipamento que deseja vincular a nota fiscal e clique em selecionar, uma outra caixa aparecerá pedindo o caminho do arquivo da nota fiscal, clique em Browse ou digite o caminho do arquivo, após clicar em Browse a jenala do windows abrirá para você procurar o arquivo PDF no seu computador. Encontre o arquivo, clique duas vezes ou clique uma vez para selecionar o arquivo e depois clique em abrir na caixa interativa. Após isto o arquivo foi enviado automaticamente para o sistema e já consta nos arquivos locais do programa.


### Funcionalidade 5 do programa
Fecha o programa.
