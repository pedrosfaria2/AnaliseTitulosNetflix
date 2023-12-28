import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def grafico_histograma(df, coluna, b, s, titulo, x_label):
    plt.figure(figsize=(10,5))
    plt.hist(df[coluna], bins=b, alpha=0.5, color='b')
    plt.title(titulo)
    plt.xlabel(x_label)
    plt.ylabel('Frequência')
    x_ticks = np.arange(min(df[coluna]), max(df[coluna]), step=s)
    plt.xticks(x_ticks)
    plt.grid(True)
    plt.show()

def calcula_indice_de_popularidade(df, m, C):
    v = df['imdb_votes']
    R = df['imdb_score']
    return (v/(v+m) * R) + (m/(m+v) * C)

def cria_grafico_dispersao(df, s, x, y, titulo, x_label, y_label):
    plt.figure(figsize=(10,5))
    plt.scatter(df[x], df[y], alpha=0.5)
    plt.title(titulo)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    x_ticks = np.arange(min(df[x]), max(df[x]), step=s)
    plt.xticks(x_ticks)
    plt.grid(True)
    plt.show()