#Importação de bibliotecas
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import os
import BancoDados

#Criação da variável para o caminho dinâmico
pastaApp=os.path.dirname(__file__)

############################################################Função Novo Paciente#################################################################
def novoPaciente():
    # Função gravar dados
    def gravarDados():
        if tb_nome.get() != "":
            vnome = tb_nome.get()
            vidade = tb_idade.get()
            vtelefone = tb_telefone.get()
            vdiagnostico = tb_diagnostico.get()
            vobs = tb_obs.get("1.0", END)
            vquery = "INSERT INTO tb_pacientes (T_NomePaciente,N_Idade,N_Telefone,T_Diagnostico,T_Observacao) VALUES('" + vnome + "','" + vidade + "','" + vtelefone + "','" + vdiagnostico + "','" + vobs + "')"
            BancoDados.dml(vquery)
            tb_nome.delete(0, END)
            tb_idade.delete(0, END)
            tb_telefone.delete(0, END)
            tb_diagnostico.delete(0, END)
            tb_obs.delete("1.0", END)
            print("Dados gravados")
        else:
            print("Erro")

    # Criação da janela
    app = Tk()

    # Título da janela
    app.title("Adicionar Paciente")
    app.wm_iconbitmap("icone.ico")

    # Dimensionamento da janela
    app.geometry("600x430")
    app.configure(background="#dde")

    # Construção e organização dos elementos na janela
    Label(app, text="Nome", background="#dde", foreground="#009", anchor=W).place(x=10, y=10, width=100, height=20)
    tb_nome = Entry(app)
    tb_nome.place(x=10, y=30, width=300, height=20)

    Label(app, text="Idade", background="#dde", foreground="#009", anchor=W).place(x=10, y=60, width=100, height=20)
    tb_idade = Entry(app)
    tb_idade.place(x=10, y=80, width=40, height=20)
    Label(app, text="anos", background="#dde", foreground="#009", anchor=W).place(x=52, y=80, width=100, height=20)

    Label(app, text="Telefone", background="#dde", foreground="#009", anchor=W).place(x=10, y=110, width=100, height=20)
    tb_telefone = Entry(app)
    tb_telefone.place(x=10, y=130, width=300, height=20)

    Label(app, text="Likert Ativo", background="#dde", foreground="#009", anchor=W).place(x=10, y=160, width=100, height=20)
    tb_idade = Entry(app)
    tb_idade.place(x=10, y=180, width=40, height=20)

    Label(app, text="Likert Positivo", background="#dde", foreground="#009", anchor=W).place(x=230, y=160, width=100, height=20)
    tb_idade = Entry(app)
    tb_idade.place(x=230, y=180, width=40, height=20)

    Label(app, text="Diagnostico", background="#dde", foreground="#009", anchor=W).place(x=10, y=210, width=100,
                                                                                         height=20)
    tb_diagnostico = Entry(app)
    tb_diagnostico.place(x=10, y=230, width=300, height=20)

    Label(app, text="Observacoes", background="#dde", foreground="#009", anchor=W).place(x=10, y=260, width=100,
                                                                                         height=20)
    tb_obs = Text(app)  # Texto multilinhas
    tb_obs.place(x=10, y=280, width=580, height=80)

    # Adicionar Botões
    Button(app, text="Gravar", command=gravarDados).place(x=10, y=380, width=100, height=20)

    app.mainloop()

################################################################Função Pesquisar Paciente################################################################
def pesquisarPaciente():
    # Criação da variável para o caminho dinâmico
    pastaApp = os.path.dirname(__file__)

    # Função Voluntarios
    def voluntario1():
        # Criação da janela
        app = Toplevel()

        # Título da janela
        app.title("Voluntario 1")
        app.wm_iconbitmap("icone.ico")

        # Dimensionamento da janela
        app.geometry("690x660")
        app.configure(background="#fff")

        # Criação do grid
        quadroAtivo = LabelFrame(app, text="Exercício Ativo", foreground="#009")
        quadroAtivo.pack(fill="both", expand="yes", padx=10, pady=10)

        # Inserindo imagem na janela
        imagem = tk.PhotoImage(file="AtivoV1.png")
        w = tk.Label(quadroAtivo, image=imagem)
        w.imagem = imagem
        w.pack()

        # Criação do grid
        quadroPassivo = LabelFrame(app, text="Exercício Passivo", foreground="#009")
        quadroPassivo.pack(fill="both", expand="yes", padx=10, pady=10)

        # Inserindo imagem na janela
        imagem = tk.PhotoImage(file="PassivoV1.png")
        w = tk.Label(quadroPassivo, image=imagem)
        w.imagem = imagem
        w.pack()

    def voluntario2():
        # Criação da janela
        app = Toplevel()

        # Título da janela
        app.title("Voluntario 2")
        app.wm_iconbitmap("icone.ico")

        # Dimensionamento da janela
        app.geometry("690x660")
        app.configure(background="#fff")

        # Criação do grid
        quadroAtivo = LabelFrame(app, text="Exercício Ativo", foreground="#009")
        quadroAtivo.pack(fill="both", expand="yes", padx=10, pady=10)

        # Inserindo imagem na janela
        imagem = tk.PhotoImage(file="AtivoV2.png")
        w = tk.Label(quadroAtivo, image=imagem)
        w.imagem = imagem
        w.pack()

        # Criação do grid
        quadroPassivo = LabelFrame(app, text="Exercício Passivo", foreground="#009")
        quadroPassivo.pack(fill="both", expand="yes", padx=10, pady=10)

        # Inserindo imagem na janela
        imagem = tk.PhotoImage(file="PassivoV2.png")
        w = tk.Label(quadroPassivo, image=imagem)
        w.imagem = imagem
        w.pack()

    def voluntario3():
        # Criação da janela
        app = Toplevel()

        # Título da janela
        app.title("Voluntario 3")
        app.wm_iconbitmap("icone.ico")

        # Dimensionamento da janela
        app.geometry("690x660")
        app.configure(background="#fff")

        # Criação do grid
        quadroAtivo = LabelFrame(app, text="Exercício Ativo", foreground="#009")
        quadroAtivo.pack(fill="both", expand="yes", padx=10, pady=10)

        # Inserindo imagem na janela
        imagem = tk.PhotoImage(file="AtivoV3.png")
        w = tk.Label(quadroAtivo, image=imagem)
        w.imagem = imagem
        w.pack()

        # Criação do grid
        quadroPassivo = LabelFrame(app, text="Exercício Passivo", foreground="#009")
        quadroPassivo.pack(fill="both", expand="yes", padx=10, pady=10)

        # Inserindo imagem na janela
        imagem = tk.PhotoImage(file="PassivoV3.png")
        w = tk.Label(quadroPassivo, image=imagem)
        w.imagem = imagem
        w.pack()

    def voluntario4():
        # Criação da janela
        app = Toplevel()

        # Título da janela
        app.title("Voluntario 4")
        app.wm_iconbitmap("icone.ico")

        # Dimensionamento da janela
        app.geometry("690x660")
        app.configure(background="#fff")

        # Criação do grid
        quadroAtivo = LabelFrame(app, text="Exercício Ativo", foreground="#009")
        quadroAtivo.pack(fill="both", expand="yes", padx=10, pady=10)

        # Inserindo imagem na janela
        imagem = tk.PhotoImage(file="AtivoV4.png")
        w = tk.Label(quadroAtivo, image=imagem)
        w.imagem = imagem
        w.pack()

        # Criação do grid
        quadroPassivo = LabelFrame(app, text="Exercício Passivo", foreground="#009")
        quadroPassivo.pack(fill="both", expand="yes", padx=10, pady=10)

        # Inserindo imagem na janela
        imagem = tk.PhotoImage(file="PassivoV4.png")
        w = tk.Label(quadroPassivo, image=imagem)
        w.imagem = imagem
        w.pack()

    def voluntario5():
        # Criação da janela
        app = Toplevel()

        # Título da janela
        app.title("Voluntario 5")
        app.wm_iconbitmap("icone.ico")

        # Dimensionamento da janela
        app.geometry("690x660")
        app.configure(background="#fff")

        # Criação do grid
        quadroAtivo = LabelFrame(app, text="Exercício Ativo", foreground="#009")
        quadroAtivo.pack(fill="both", expand="yes", padx=10, pady=10)

        # Inserindo imagem na janela
        imagem = tk.PhotoImage(file="AtivoV5.png")
        w = tk.Label(quadroAtivo, image=imagem)
        w.imagem = imagem
        w.pack()

        # Criação do grid
        quadroPassivo = LabelFrame(app, text="Exercício Passivo", foreground="#009")
        quadroPassivo.pack(fill="both", expand="yes", padx=10, pady=10)

        # Inserindo imagem na janela
        imagem = tk.PhotoImage(file="PassivoV5.png")
        w = tk.Label(quadroPassivo, image=imagem)
        w.imagem = imagem
        w.pack()

    def voluntario6():
        # Criação da janela
        app = Toplevel()

        # Título da janela
        app.title("Voluntario 6")
        app.wm_iconbitmap("icone.ico")

        # Dimensionamento da janela
        app.geometry("690x660")
        app.configure(background="#fff")

        # Criação do grid
        quadroAtivo = LabelFrame(app, text="Exercício Ativo", foreground="#009")
        quadroAtivo.pack(fill="both", expand="yes", padx=10, pady=10)

        # Inserindo imagem na janela
        imagem = tk.PhotoImage(file="AtivoV6.png")
        w = tk.Label(quadroAtivo, image=imagem)
        w.imagem = imagem
        w.pack()

        # Criação do grid
        quadroPassivo = LabelFrame(app, text="Exercício Passivo", foreground="#009")
        quadroPassivo.pack(fill="both", expand="yes", padx=10, pady=10)

        # Inserindo imagem na janela
        imagem = tk.PhotoImage(file="PassivoV6.png")
        w = tk.Label(quadroPassivo, image=imagem)
        w.imagem = imagem
        w.pack()

    # Função para determinar o voluntário selecionado
    def voluntarioSelecionado():
        voluntario_selecionado = cb_voluntarios.get()
        if voluntario_selecionado == "Voluntário 1":
            command = voluntario1()
        elif voluntario_selecionado == "Voluntário 2":
            command = voluntario2()
        elif voluntario_selecionado == "Voluntário 3":
            command = voluntario3()
        elif voluntario_selecionado == "Voluntário 4":
            command = voluntario4()
        elif voluntario_selecionado == "Voluntário 5":
            command = voluntario5()
        elif voluntario_selecionado == "Voluntário 6":
            command = voluntario6()
        else:
            messagebox.showerror(title="ERRO", message="Selecione um voluntário válido")

    # Criação da janela
    app = Tk()

    # Título da janela
    app.title("Procurar paciente")
    app.wm_iconbitmap("icone.ico")

    # Dimensionamento da janela
    app.geometry("600x370")
    app.configure(background="#dde")

    # Lista de voluntários
    listaVoluntarios = ["Voluntário 1", "Voluntário 2", "Voluntário 3", "Voluntário 4", "Voluntário 5", "Voluntário 6"]

    # Criação da Label
    lb_voluntarios = Label(app, text="Voluntário", background="#dde", foreground="#009")
    lb_voluntarios.place(x=260, y=100)

    # Criação da ComboBox
    cb_voluntarios = ttk.Combobox(app, values=listaVoluntarios)
    cb_voluntarios.place(x=220, y=120)

    # Textos
    texto = Label(app, text="Escolha o paciente a ser consultado, na caixa abaixo", background="#dde", font="Arial 12",
                  foreground="#009")
    texto.pack()
    # informativo=tk.Label(app, text="Pressione o botão procurar",background="#dde",foreground="#009").place(x=260,y=200)

    # Criação do botão
    bt_voluntario = Button(app, text="Procurar", command=voluntarioSelecionado)
    bt_voluntario.place(x=260, y=150)

    app.mainloop()

#######################################################Função Dados Voluntários#####################################################################
def dadosVoluntarios():
    # Função preenchimento dos registros
    def popular():
        tv.delete(*tv.get_children())
        query = "SELECT * FROM tb_pacientes order by N_IdPaciente"
        linhas = BancoDados.dql(query)
        for i in linhas:
            tv.insert("", "end", values=i)

    # Função deletar
    def deletar():
        vid = -1
        itemSelecionado = tv.selection()[0]
        valores = tv.item(itemSelecionado, "values")
        vid = valores[0]
        try:
            query = "DELETE FROM tb_pacientes WHERE N_IdPaciente= " + vid
            BancoDados.dml(query)
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um paciente a ser deletado")
            return
        tv.delete(itemSelecionado)

    # Função Pequisar
    def pesquisar():
        tv.delete(*tv.get_children())
        query = "SELECT * FROM tb_pacientes WHERE T_NomePaciente LIKE '%" + vnomepesquisar.get() + "%' order by N_IdPaciente"
        linhas = BancoDados.dql(query)
        for i in linhas:
            tv.insert("", "end", values=i)

    # Criação da janela
    app = Tk()

    # Título da janela
    app.title("Pesquisar")
    app.wm_iconbitmap("icone.ico")

    # Dimensionamento da janela
    app.geometry("1100x600")
    app.configure(background="#dde")

    # Criação do grid
    quadroGrid = LabelFrame(app, text="Pacientes", foreground="#009")
    quadroGrid.pack(fill="both", expand="yes", padx=10, pady=10)

    # Criação da TreeView
    tv = ttk.Treeview(quadroGrid, columns=('id', 'nome', 'idade', 'telefone', 'likertAtivo', 'likertPassivo', 'diagnostico', 'observacoes'),
                      show='headings')

    # Dimensão das colunas
    tv.column('id', minwidth=0, width=80)
    tv.column('nome', minwidth=0, width=250)
    tv.column('idade', minwidth=0, width=50)
    tv.column('telefone', minwidth=0, width=100)
    tv.column('likertAtivo', minwidth=0, width=100)
    tv.column('likertPassivo', minwidth=0, width=100)
    tv.column('diagnostico', minwidth=0, width=100)
    tv.column('observacoes', minwidth=0, width=300)

    # Definição dos textos dos cabeçalhos
    tv.heading('id', text="Voluntário")
    tv.heading('nome', text="NOME")
    tv.heading('idade', text="IDADE")
    tv.heading('telefone', text="TELEFONE")
    tv.heading('likertAtivo', text="LIKERT ATIVO")
    tv.heading('likertPassivo', text="LIKERT PASSIVO")
    tv.heading('diagnostico', text="DIAGNÓSTICO")
    tv.heading('observacoes', text="OBSERVAÇÕES")

    tv.pack()
    popular()

    # Criação do Pesquisar
    quadroPesquisar = LabelFrame(app, text="Pesquisar Pacientes", foreground="#009")
    quadroPesquisar.pack(fill="both", expand="yes", padx=10, pady=10)

    lbid = Label(quadroPesquisar, text="Nome", foreground="#009")
    lbid.pack(side="left")
    vnomepesquisar = Entry(quadroPesquisar)
    vnomepesquisar.pack(side="left", padx=10)

    # Criação do botão
    bt_pesquisar = Button(quadroPesquisar, text="Pesquisar", command=pesquisar)
    bt_pesquisar.pack(side="left", padx=10)
    bt_todos = Button(quadroPesquisar, text="Mostrar Todos", command=popular)
    bt_todos.pack(side="left", padx=10)

    # Criação do campo deletar
    quadroPesquisar = LabelFrame(app, text="Deletar Pacientes", foreground="#009")
    quadroPesquisar.pack(fill="both", expand="yes", padx=10, pady=10)

    lbid = Label(quadroPesquisar, text="Selecione um paciente e depois pressione o botão deletar")
    lbid.pack(side="left")

    # Criação do botão deletar
    bt_deletar = Button(quadroPesquisar, text="Deletar", command=deletar)
    bt_deletar.pack(side="left", padx=10)

    app.mainloop()

#######################################################Função Senha#################################################################################
def voluntarioProtegido():
    # Criando acesso
    def login():
        usuario = usuarioEntry.get()
        senha = senhaEntry.get()
        if(usuario == "acesso" and senha == "123"):
            command=dadosVoluntarios()
        else:
            messagebox.showerror(title="Informação do login",message="Digite a senha correta")
    # Criação da janela
    app = Tk()
    # Título da janela
    app.title("Senha")
    app.wm_iconbitmap("icone.ico")

    # Dimensionamento da janela
    app.geometry("300x200")
    app.configure(background="#dde")
    app.resizable(width=False, height=False)
    app.attributes("-alpha", 0.9)

    # Label
    TituloLabel = Label(app, text="Usuário e senha", background="#dde", foreground="#009", anchor=W).place(x=110, y=10)
    UsuarioLabel = Label(app, text="Usuário:", background="#dde", foreground="#009", anchor=W).place(x=40, y=60)
    SenhaLabel = Label(app, text="Senha:", background="#dde", foreground="#009", anchor=W).place(x=40, y=100)

    # Campo da senha
    usuarioEntry = Entry(app, width=27)
    usuarioEntry.place(x=90, y=60)

    # Campo da senha
    senhaEntry = Entry(app, show="•", width=27)
    senhaEntry.place(x=90, y=100)

    # Botões da janela
    bt_Acesso = ttk.Button(app, text="Acesso", width=10, command=login)
    bt_Acesso.place(x=120, y=150)

    app.mainloop()
######################################################Função LABORE##################################################################
def labore():
    # Criação da janela
    app = Toplevel()

    # Título da janela
    app.title("LABORE")
    app.wm_iconbitmap("icone.ico")

    # Dimensionamento da janela
    app.geometry("690x660")
    app.configure(background="#fff")

    # Inserindo imagem na janela
    imagem = tk.PhotoImage(file="LaboreTexto.png")
    w = tk.Label(app, image=imagem)
    w.imagem = imagem
    w.pack()

######################################################Função Emotiv EPOC##################################################################
def emotivEpoc():
    # Criação da janela
    app = Toplevel()

    # Título da janela
    app.title("Emotiv Epoc")
    app.wm_iconbitmap("icone.ico")

    # Dimensionamento da janela
    app.geometry("600x640")
    app.configure(background="#fff")

    # Inserindo imagem na janela
    imagem = tk.PhotoImage(file="EmotivEpocTexto.png")
    w = tk.Label(app, image=imagem)
    w.imagem = imagem
    w.pack()

# Criação da janela
app = Tk()

# Título da janela
app.title("Anamnese - Tela principal")
app.wm_iconbitmap("icone.ico")

# Dimensionamento da janela
app.geometry("1000x600")
app.configure(background="#fff")

#Textos
texto=Label(app,text="Seja bem vindo a este Banco de Dados!",background="#fff",font="impact 20",foreground="#009")
texto.pack()

informativo=tk.Label(app, text="Selecione uma ação desejada na barra de menu",bg="#fff",fg="#6B8E23",font="arial 14 bold").place(x=280,y=520)

#Inserindo imagem na janela
imagem = tk.PhotoImage(file="ImagemFundo.png")
w = tk.Label(app, image=imagem)
w.imagem = imagem
w.pack()

#Variável Barra de menu
barraDeMenu=Menu(app)

#Elementos do menu - Paciente
menuPaciente=Menu(barraDeMenu,tearoff=0)
menuPaciente.add_command(label="Novo",command=novoPaciente)
menuPaciente.add_command(label="Pesquisar",command=pesquisarPaciente)
menuPaciente.add_separator()
menuPaciente.add_command(label="Fechar",command=app.destroy)
barraDeMenu.add_cascade(label="Paciente",menu=menuPaciente)

#Elementos do menu - Voluntários
menuVoluntarios=Menu(barraDeMenu,tearoff=0)
menuVoluntarios.add_command(label="Voluntários",command=voluntarioProtegido)
barraDeMenu.add_cascade(label="Dados",menu=menuVoluntarios)

#Elementos do menu - Sobre
menuSobre=Menu(barraDeMenu,tearoff=0)
menuSobre.add_command(label="LABORE",command=labore)
menuSobre.add_command(label="EMOTIV EPOC",command=emotivEpoc)
barraDeMenu.add_cascade(label="Sobre",menu=menuSobre)

app.configure(menu=barraDeMenu)

app.mainloop()
