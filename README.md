# Sistema de Gerenciamento de Estoque de Livraria

Este projeto é uma aplicação desenvolvida em Python utilizando a biblioteca `customtkinter` para criar uma interface gráfica. O sistema permite gerenciar o estoque de uma livraria, adicionando e removendo livros, além de calcular estatísticas sobre a distribuição dos gêneros literários.

## Estrutura do Código

### 1. Importação de Bibliotecas
```python
import customtkinter as ctk
```
A biblioteca `customtkinter` é utilizada para criar uma interface gráfica moderna e customizável.

### 2. Definição de Constantes
```python
GENERO_FICCAO = 10
GENERO_ROMANCE = 12
GENERO_BIOGRAFIA = 8
GENERO_MISTERIO = 6
```
Essas constantes definem os limites máximos de quantidade para cada gênero de livro no estoque.

### 3. Lista de Estoque
```python
estoque = []
```
A lista `estoque` armazena os livros cadastrados na livraria.

### 4. Função para Calcular o Total de Livros no Estoque
```python
def calcular_total_estoque():
    return sum(livro['quantidade'] for livro in estoque)
```
Esta função soma a quantidade total de livros disponíveis no estoque.

### 5. Função para Calcular a Porcentagem de um Gênero
```python
def calcular_porcentagem_genero(genero):
    total_estoque = calcular_total_estoque()
    quantidade_genero = sum(livro['quantidade'] for livro in estoque if livro['genero'] == genero)
    if total_estoque == 0:
        return 0
    return (quantidade_genero / total_estoque) * 100
```
Esta função calcula a porcentagem de um gênero específico dentro do estoque.

### 6. Função para Adicionar Livros ao Estoque
```python
def adicionar_livro(titulo, genero, quantidade):
    if genero == 'Ficção' and quantidade > GENERO_FICCAO:
        return f"A quantidade máxima para Ficção é {GENERO_FICCAO}."
    elif genero == 'Romance' and quantidade > GENERO_ROMANCE:
        return f"A quantidade máxima para Romance é {GENERO_ROMANCE}."
    elif genero == 'Biografia' and quantidade > GENERO_BIOGRAFIA:
        return f"A quantidade máxima para Biografia é {GENERO_BIOGRAFIA}."
    elif genero == 'Mistério' and quantidade > GENERO_MISTERIO:
        return f"A quantidade máxima para Mistério é {GENERO_MISTERIO}."
    estoque.append({'titulo': titulo, 'genero': genero, 'quantidade': quantidade})
    atualizar_porcentagens()
    return None
```
Esta função adiciona livros ao estoque, respeitando os limites máximos definidos para cada gênero.

### 7. Atualizar Porcentagem dos Gêneros
```python
def atualizar_porcentagens():
    porcentagem_ficcao = calcular_porcentagem_genero('Ficção')
    porcentagem_romance = calcular_porcentagem_genero('Romance')
    porcentagem_biografia = calcular_porcentagem_genero('Biografia')
    porcentagem_misterio = calcular_porcentagem_genero('Mistério')
```
Atualiza as porcentagens de cada gênero e exibe na interface gráfica.

### 8. Atualizar a Exibição do Estoque
```python
def atualizar_estoque_display():
    for widget in frame_estoque.winfo_children():
        widget.destroy()
    for livro in estoque:
        ctk.CTkLabel(frame_estoque, text=f"Título: {livro['titulo']}, Gênero: {livro['genero']}, Quantidade: {livro['quantidade']}", font=fonte_padrao).pack(pady=2)
```
Esta função exibe os livros cadastrados na interface gráfica.

### 9. Função para Remover Livros do Estoque
```python
def remover_livro(titulo):
    global estoque
    estoque = [livro for livro in estoque if livro['titulo'].lower() != titulo.lower()]
    atualizar_estoque_display()
    atualizar_porcentagens()
```
Remove um livro do estoque com base no título.

### 10. Interface Gráfica

#### Configuração da Janela Principal
```python
app = ctk.CTk()
app.title('Sistema de Gerenciamento de Estoque Livraria')
app.geometry('600x400')
```
Criação da janela principal da aplicação.

#### Campos de Entrada para Adicionar Livros
```python
entry_titulo = ctk.CTkEntry(frame_entrada, font=fonte_padrao)
combo_genero = ctk.CTkComboBox(frame_entrada, values=['Ficção', 'Romance', 'Biografia', 'Mistério'], font=fonte_padrao)
entry_quantidade = ctk.CTkEntry(frame_entrada, font=fonte_padrao)
```
Campos onde o usuário insere o título, gênero e quantidade de livros a serem adicionados.

#### Botão para Adicionar Livro
```python
botao_adicionar = ctk.CTkButton(frame_entrada, text='Adicionar Livro', command=on_adicionar_livro, font=fonte_padrao)
```
Botão que aciona a função `on_adicionar_livro()` para adicionar um livro ao estoque.

#### Campos de Entrada para Remover Livros
```python
entry_remover_titulo = ctk.CTkEntry(frame_remocao, font=('Poppins', 12))
botao_remover = ctk.CTkButton(frame_remocao, text='Remover Livro', command=on_remover_livro, font=('Poppins', 12))
```
Campos onde o usuário insere o título do livro a ser removido.

#### Inicialização da Aplicação
```python
app.mainloop()
```
Inicia o loop principal da interface gráfica, permitindo a interação do usuário.

## Conclusão
Este sistema permite gerenciar um pequeno estoque de livros de forma simples e eficiente, fornecendo uma interface gráfica interativa e controles para adição, remoção e monitoramento do estoque de livros, dessa forma atuando como um CRUD.

