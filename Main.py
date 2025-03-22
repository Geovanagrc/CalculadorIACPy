import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo  # ImportaÃ§Ã£o correta do showinfo
import math

#Função para carregar dados
def carregar_dados():
    global iac
    global altura
    global quadril
    global genero
    with open ('Historico'+'.txt','r') as arquivo:
        iac = arquivo.readline()
        altura = arquivo.readline()
        quadril = arquivo.readline()
        genero = arquivo.readline()
    entradaAltura.delete(0,tk.END)#Do primeiro caractere ao ultimo
    entradaQuadril.delete(0,tk.END)
    entradaAltura.insert(0,altura)
    entradaQuadril.insert(0,quadril)
    selecao.set(StringVar(genero))
    calcular()    
#Função gravar_dados
def gravar_dados():
    global iac
    global altura
    global quadril
    global genero
    with open('Historico'+'.txt','w') as historico:
        historico.write(f'{str(iac)}\n')
        historico.write(f'{str(altura)}\n')
        historico.write(f'{str(quadril)}\n')
        historico.write(f'{str(genero)}\n')

#CONFIG TELA

janela = Tk()
janela.geometry('350x350')  # Aumentei um pouco a largura para dar mais espaÃ§o

janela.title("IAC")
janela.resizable(0, 0)

#Alterando o fundo da janela e as cores do texto

janela.config(bg="#2e2e2e")  # Cor de fundo escura

#Função para calcular o IAC

def calcular():
    global iac
    global altura
    global quadril
    global genero
    try:
        # Obtem os valores das entradas
        quadril = float(entradaQuadril.get())
        altura = float(entradaAltura.get())

        # Calcula a raiz quadrada da altura
        raiz_altura = math.sqrt(altura)

        # Calcula o IAC
        iac = (quadril / (altura * raiz_altura)) - 18

        # Obtem a seleçao do Gênero
        genero = selecao.get()

        # Classificação do IAC com base no Gênero
        if genero == "Mulher":
            if iac > 30:
                classificacao = "Excesso"
                cor_classificacao = "#FF6347"  # Vermelho
            elif 26 <= iac < 30:
                classificacao = "Moderado"
                cor_classificacao = "#FFD700"  # Amarelo
            elif 20 <= iac < 26:
                classificacao = "Ideal"
                cor_classificacao = "#32CD32"  # Verde
            elif 16 <= iac < 20:
                classificacao = "Baixo"
                cor_classificacao = "#800080"  # Roxo
            elif 10 <= iac < 16:
                classificacao = "Muito baixo"
                cor_classificacao = "#9370DB"  # Roxo claro
            else:
                classificacao = "Valor fora da faixa"
                cor_classificacao = "#808080"  # Cinza

        elif genero == "Homem":
            if  iac > 25:
                classificacao = "Excesso"
                cor_classificacao = "#FF6347"  # Vermelho
            elif 19 <= iac < 25:
                classificacao = "Moderado"
                cor_classificacao = "#FFD700"  # Amarelo
            elif 15 <= iac < 19:
                classificacao = "Ideal"
                cor_classificacao = "#32CD32"  # Verde
            elif 11 <= iac < 15:
                classificacao = "Baixo"
                cor_classificacao = "#800080"  # Roxo
            elif 6 <= iac < 11:
                classificacao = "Muito baixo"
                cor_classificacao = "#9370DB"  # Roxo claro
            else:
                classificacao = "Valor fora da faixa"
                cor_classificacao = "#808080"  # Cinza
        else:
            showinfo('Erro','Por favor, selecione o gênero',icon='info')  # Exibe a janela de erro
            classificacao = "selecione o gênero"
            cor_classificacao = "#808080"  # Cinza

        # Atualiza a label de sai­da com o resultado
        saida.config(text=f"IAC: {iac:.2f} - {classificacao}")  # Mostra o resultado com 2 casas decimais

        # Atualiza o quadrado colorido ao lado da classificação
        quadrado.config(bg=cor_classificacao)
    except ValueError:
        showinfo('Erro','insira valores validos (Ex: 1.67).',icon='info')
        saida.config(text="Por favor, insira valores validos.")  # Em caso de erro na conversÃ£o dos valores

#LABEL QUADRIL

labelQuadril = Label(janela, text="Quadril(cm):", bg="#2e2e2e", fg="white", font=("Arial", 12))
labelQuadril.grid(row=0, column=0, padx=10, pady=10, sticky='e')

#ENTRADA QUADRIL

entradaQuadril = Entry(janela, bg="#4f4f4f", fg="white", font=("Arial", 12))
entradaQuadril.grid(row=0, column=1, padx=10, pady=10)

#LABEL ALTURA

labelAltura = Label(janela, text="Altura(m):", bg="#2e2e2e", fg="white", font=("Arial", 12))
labelAltura.grid(row=1, column=0, padx=10, pady=10, sticky='e')

#ENTRADA ALTURA

entradaAltura = Entry(janela, bg="#4f4f4f", fg="white", font=("Arial", 12))
entradaAltura.grid(row=1, column=1, padx=10, pady=10)

#LABEL SELEção GeNERO

labelGenero = Label(janela, text="Gênero:", bg="#2e2e2e", fg="white", font=("Arial", 12))
labelGenero.grid(row=2, column=0, padx=10, pady=10, sticky='e')

#Variavel de controle para o genero

selecao = StringVar()

#Radiobutton para 'Mulher'

mulher = Radiobutton(janela, text="Mulher", variable=selecao, value="Mulher", bg="#2e2e2e", fg="white", selectcolor="#4f4f4f", font=("Arial", 12))
mulher.grid(row=2, column=1, padx=10, pady=10, sticky='w')

#Radiobutton para 'Homem'

homem = Radiobutton(janela, text="Homem", variable=selecao, value="Homem", bg="#2e2e2e", fg="white", selectcolor="#4f4f4f", font=("Arial", 12))
homem.grid(row=3, column=1, padx=10, pady=10, sticky='w')

#BotÃ£o para calcular o IAC

botaoCalcular = Button(janela, text="Calcular IAC", command=calcular, bg="#4f4f4f", fg="white", font=("Arial", 12))
botaoCalcular.grid(row=4, column=0, columnspan=2, pady=10)

#LABEL SAiDA (Para exibir o resultado)

saida = Label(janela, text="IAC: ", bg="#2e2e2e", fg="white", font=("Arial", 14))
saida.grid(row=5, column=0, columnspan=2, pady=10)

#Label do quadrado colorido, ajustado para ficar mais perto da classificao

quadrado = Label(janela, width=4, height=2, bg="#808080")  # Cor inicial cinza
quadrado.place(x=300, y=245)

#Botão para salvar os dados
btn_salvar = Button(janela,text="Salvar", command = gravar_dados)
btn_salvar.config(width = 10,height = 1,bg="#4f4f4f", fg="white")
btn_salvar.place(x= 50,y = 300)

#Botão carregar
btn_carregar = Button (janela, text= "Carregar",command = carregar_dados)
btn_carregar.config(width = 10,height = 1,bg="#4f4f4f", fg="white")
btn_carregar.place(x = 150, y=300)

janela.mainloop()