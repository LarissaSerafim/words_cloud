import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

df = pd.read_csv("Book.csv") # Abrir texto que será analisado

all_summary = " ".join(s for s in df)
print("Quantidade de Palavras: {}".format(len(all_summary)))

arquivo_lista = 'C:\\Users\\larissa.serafim\\Documents\\Python\\Nuvem de Palavras\\stopwords.txt'
with open(arquivo_lista, 'r') as arquivo:
    conteudo = arquivo.read()
    
lista_conteudo = conteudo.split('\n')  # Dividir por nova linha
lista_conteudo = [linha.strip() for linha in lista_conteudo]  # Transformar arquivo com stopwords em uma lista

stopwords = set(STOPWORDS)
stopwords.update(lista_conteudo) # Setar stopwords

nuvem_masc= np.array(Image.open('nuvem_de_formato.png')) # Formato da nuvem

wordcloud = WordCloud(stopwords=stopwords,background_color="navy",width=3000, height=6000, mask=nuvem_masc, max_words=25,max_font_size=400).generate(all_summary) # Configurações da nuvem

fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()

cores = ["purple", "pink", "blue", "orange"] # Cores das letras nas palavras

def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return cores[hash(word) % len(cores)]

wordcloud.recolor(color_func=color_func)

plt.imshow(wordcloud);
wordcloud.to_file("nuvem_palavras.png")