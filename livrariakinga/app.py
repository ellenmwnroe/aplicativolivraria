import customtkinter as ctk

# Definindo as constantes para o limite de quantidade de livros por gênero
GENERO_FICCAO = 10
GENERO_ROMANCE = 12
GENERO_BIOGRAFIA = 8
GENERO_MISTERIO = 6

# Lista de livros no estoque
estoque = []

# Função para calcular o total de livros no estoque
def calcular_total_estoque():
    return sum(livro['quantidade'] for livro in estoque)

# Função para calcular a porcentagem de livros de um gênero no estoque
def calcular_porcentagem_genero(genero):
    total_estoque = calcular_total_estoque()
    quantidade_genero = sum(livro['quantidade'] for livro in estoque if livro['genero'] == genero)
    if total_estoque == 0:
        return 0
    return (quantidade_genero / total_estoque) * 100

# Função para adicionar livros ao estoque com verificação do limite
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

# Função para atualizar a porcentagem de livros por gênero
def atualizar_porcentagens():
    porcentagem_ficcao = calcular_porcentagem_genero('Ficção')
    porcentagem_romance = calcular_porcentagem_genero('Romance')
    porcentagem_biografia = calcular_porcentagem_genero('Biografia')
    porcentagem_misterio = calcular_porcentagem_genero('Mistério')

    label_porcentagem_ficcao.configure(text=f"Porcentagem de Ficção: {porcentagem_ficcao:.2f}%")
    label_porcentagem_romance.configure(text=f"Porcentagem de Romance: {porcentagem_romance:.2f}%")
    label_porcentagem_biografia.configure(text=f"Porcentagem de Biografia: {porcentagem_biografia:.2f}%")
    label_porcentagem_misterio.configure(text=f"Porcentagem de Mistério: {porcentagem_misterio:.2f}%")

# Função para atualizar a exibição do estoque na interface gráfica
def atualizar_estoque_display():
    for widget in frame_estoque.winfo_children():
        widget.destroy()
    for livro in estoque:
        ctk.CTkLabel(frame_estoque, text=f"Título: {livro['titulo']}, Gênero: {livro['genero']}, Quantidade: {livro['quantidade']}", font=fonte_padrao).pack(pady=2)

# Função chamada ao clicar no botão "Adicionar Livro"
def on_adicionar_livro():
    titulo = entry_titulo.get()
    genero = combo_genero.get()
    try:
        quantidade = int(entry_quantidade.get())
        if quantidade <= 0:
            raise ValueError
    except ValueError:
        label_status.configure(text="Quantidade inválida! Insira um número inteiro positivo.", text_color='red')
        return
    mensagem_erro = adicionar_livro(titulo, genero, quantidade)
    if mensagem_erro:
        label_status.configure(text=mensagem_erro, text_color='red')
    else:
        atualizar_estoque_display()
        label_status.configure(text="Livro adicionado com sucesso!", text_color='green')

#Função para remover livro do estoque
def remover_livro(titulo):
    global estoque
    estoque = [livro for livro in estoque if livro['titulo'].lower() != titulo.lower()]
    atualizar_estoque_display()
    atualizar_porcentagens()
    
def on_remover_livro():
    titulo = entry_remover_titulo.get()
    if titulo:
        remover_livro(titulo)
        label_status.configure(text="Livro removido com sucesso!", text_color='green')
    else:
        label_status.configure(text="Por favor, insira o título do livro a ser removido.", text_color='red')
        
#configurações da interface gráfica
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

# Definindo a fonte padrão
fonte_padrao = ("Poppins", 12)

# Janela principal
app = ctk.CTk()
app.title('Sistema de Gerenciamento de Estoque Livraria')
app.geometry('600x400')

# Subtítulo
subtitulo = ctk.CTkLabel(app, text='Sistema de Livraria - Algoritmos e Programação', font=('Poppins', 14))
subtitulo.pack(pady=10)

# Frame para entrada de dados
frame_entrada = ctk.CTkFrame(app)
frame_entrada.pack(pady=20, padx=20, fill='x', expand=True)

# Rótulo e campo de entrada para o título
label_titulo = ctk.CTkLabel(frame_entrada, text='Título do Livro:', font=fonte_padrao)
label_titulo.grid(row=0, column=0, padx=10, pady=10, sticky='e')
entry_titulo = ctk.CTkEntry(frame_entrada, font=fonte_padrao)
entry_titulo.grid(row=0, column=1, padx=10, pady=10, sticky='w')

# Rótulo e campo de entrada para o gênero
label_genero = ctk.CTkLabel(frame_entrada, text='Gênero:', font=fonte_padrao)
label_genero.grid(row=1, column=0, padx=10, pady=10, sticky='e')
combo_genero = ctk.CTkComboBox(frame_entrada, values=['Ficção', 'Romance', 'Biografia', 'Mistério'], font=fonte_padrao)
combo_genero.grid(row=1, column=1, padx=10, pady=10, sticky='w')

# Rótulo e campo de entrada para a quantidade
label_quantidade = ctk.CTkLabel(frame_entrada, text='Quantidade:', font=fonte_padrao)
label_quantidade.grid(row=2, column=0, padx=10, pady=10, sticky='e')
entry_quantidade = ctk.CTkEntry(frame_entrada, font=fonte_padrao)
entry_quantidade.grid(row=2, column=1, padx=10, pady=10, sticky='w')

# Botão para adicionar livro
botao_adicionar = ctk.CTkButton(frame_entrada, text='Adicionar Livro', command=on_adicionar_livro, font=fonte_padrao)
botao_adicionar.grid(row=3, column=0, columnspan=2, pady=20)

# Rótulo para status
label_status = ctk.CTkLabel(app, text='', text_color='red', font=fonte_padrao)
label_status.pack(pady=10)

# Frame principal para organizar os frames de estoque e porcentagens
frame_principal = ctk.CTkFrame(app)
frame_principal.pack(pady=20, padx=20, fill='both', expand=True)

# Frame para exibição do estoque
frame_estoque = ctk.CTkFrame(frame_principal)
frame_estoque.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

# Frame para exibição das porcentagens
frame_porcentagens = ctk.CTkFrame(frame_principal)
frame_porcentagens.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

# Configurar o layout do frame_principal para expandir os frames filhos
frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_columnconfigure(1, weight=1)
frame_principal.grid_rowconfigure(0, weight=1)

# Rótulos para exibição das porcentagens
label_porcentagem_ficcao = ctk.CTkLabel(frame_porcentagens, text='Porcentagem de Ficção: 0.00%', font=fonte_padrao)
label_porcentagem_ficcao.pack(pady=5)
label_porcentagem_romance = ctk.CTkLabel(frame_porcentagens, text='Porcentagem de Romance: 0.00%', font=fonte_padrao)
label_porcentagem_romance.pack(pady=5)
label_porcentagem_biografia = ctk.CTkLabel(frame_porcentagens, text='Porcentagem de Biografia: 0.00%', font=fonte_padrao)
label_porcentagem_biografia.pack(pady=5)
label_porcentagem_misterio = ctk.CTkLabel(frame_porcentagens, text='Porcentagem de Mistério: 0.00%', font=fonte_padrao)
label_porcentagem_misterio.pack(pady=5)

# Frame para remoção de livro
frame_remocao = ctk.CTkFrame(app)
frame_remocao.pack(pady=20, padx=20, fill='x', expand=True)

# Rótulo e campo de entrada para o título do livro a ser removido
label_remover_titulo = ctk.CTkLabel(frame_remocao, text='Título do Livro a Remover:', font=('Poppins', 12))
label_remover_titulo.grid(row=0, column=0, padx=10, pady=10, sticky='e')
entry_remover_titulo = ctk.CTkEntry(frame_remocao, font=('Poppins', 12))
entry_remover_titulo.grid(row=0, column=1, padx=10, pady=10, sticky='w')

# Botão para remover livro
botao_remover = ctk.CTkButton(frame_remocao, text='Remover Livro', command=on_remover_livro, font=('Poppins', 12))
botao_remover.grid(row=1, column=0, columnspan=2, pady=20)

# Rótulo para status
label_status = ctk.CTkLabel(app, text='', text_color='red', font=('Poppins', 12))
label_status.pack(pady=10)


# Iniciar a aplicação
app.mainloop()