import requests
import tkinter
from bs4 import BeautifulSoup
from PIL import Image, ImageTk
global charada
def mudarCharada():
    page = requests.get('https://us-central1-kivson.cloudfunctions.net/charada-aleatoria')
    sopa = BeautifulSoup(page.text, 'html.parser')
    charada = sopa.find('h1').contents[0]
    while len(charada) > 80:
        page = requests.get('https://us-central1-kivson.cloudfunctions.net/charada-aleatoria')
        sopa = BeautifulSoup(page.text, 'html.parser')
        charada = sopa.find('h1').contents[0]
    page = requests.get('https://us-central1-kivson.cloudfunctions.net/charada-aleatoria')
    sopa = BeautifulSoup(page.text, 'html.parser')
    charada = sopa.find('h1').contents[0]
    resposta = sopa.find('p').contents[0]
    labelCharada['text'] = charada
    labelResposta['text'] = resposta
def ajustaTela():
    janela.geometry('500x500')
#Primeira Requisição
page = requests.get('https://us-central1-kivson.cloudfunctions.net/charada-aleatoria')
sopa = BeautifulSoup(page.text, 'html.parser')
charada = sopa.find('h1').contents[0]
resposta = sopa.find('p').contents[0]
#####################
janela = tkinter.Tk()
janela.geometry('500x500')
janela.title('Ulusanoia Charadas da Net')
janela['bg'] = 'black'
img1 = tkinter.PhotoImage(file='darlan.png')
img1 = img1.subsample(2, 2)
background = tkinter.Label(janela, image=img1)
background.pack()
botaoNovamente = tkinter.Button(janela, text='Mudar Charada', command=mudarCharada, bg='black', fg='green')
ajustarTela = tkinter.Button(janela, text='Ajustar Tela', command=ajustaTela, bg='black', fg='green')
ajustarTela.place(x=410)
botaoNovamente.place(x=150, y=300, height = 50, width = 200)
labelCharada = tkinter.Label(janela, text=charada, bg='black', fg='green')
labelCharada.place(x=1, y=100, width = 500)
labelResposta = tkinter.Label(janela, text=resposta, bg='black', fg='green')
labelResposta.place(x=1, y=200, width=500)
labelCreditos = tkinter.Label(janela, text='Por: <<Ulusanoia Todos Direitos não são reservados>>', bg='black', fg='pink', font=("Arial"))
labelCreditos.place(x=0, y=482)
janela.mainloop()
