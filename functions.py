import string
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

alphabet = string.ascii_lowercase
alpha_dict = {alphabet[i]:i for i in range(len(alphabet))}
alpha_cnt = [0 for i in range(len(alphabet))]
NO_LETTERS = len(alphabet)

def letters_dist(words):
    all_words = ''.join(words)
    alpha_cnt = [all_words.count(alphabet[i])/NO_LETTERS * 100 for i in range(NO_LETTERS)]
    plt.bar([l for l in alphabet], alpha_cnt, color='magenta')
    plt.ylabel('%')
    plt.title("Frequency of letters")
    plt.show()
    return alpha_cnt


def transition_matrix(words):
    matrix = [[0 for _ in range(NO_LETTERS) + 1)] for _ in range(NO_LETTERS)]
    for word in words:
        for i in range(1, len(word)):
            if i == len(word) - 1:
                matrix[alpha_dict[word[i]]][-1] += 1
            else:
                matrix[alpha_dict[word[i - 1]]][alpha_dict[word[i]]] += 1

    df = pd.DataFrame(matrix)
    alpha = [alphabet[i] for i in range(NO_LETTERS)]
    alpha.append('\n')
    df.columns = alpha
    df.index = alpha[:-1]
    df = df.div(df.sum(axis=1), axis=0)
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(df)

    return df.values
