"""
Homework 6
Author: Dan Nguyen and Ha Chi
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import csv
import one_gram_reader

def normalize_counts(years, counts, total):
    """ This function normalize the count into relative frequencies
     Parameters:
         years: list. a list of years in which the word is being mentioned 
         counts: list. a list of the number of times the word mentioned in each respective years
         total: dict. the total of every word mentioned in each respective years
     return
         norm: list. a list of normalize the count into relative frequencies in each year """
    norm = []
    for i in range(len(years)):
        norm.append(counts[i]/total[years[i]])
    return norm


def plot_words(words, year_range, wfile, tfile):
    """ This function plot the frequency of each word throughout a year range
     Parameters:
         words: list. a list of words
         year_range: list. the first and last year of the year range.
         wfile: string. The name of the file that contain data of the word and the times it's repeat in the year range
         tfile: string. The name of the file that contain data the total times a word is mentioned in the year range"""
    total = one_gram_reader.read_total_counts(tfile)
    for word in words:
        years, counts = one_gram_reader.read_wfile(word, year_range, wfile)
        normalized_counts = normalize_counts(years, counts, total)
        plt.plot(years, normalized_counts)
    plt.legend(words)
    plt.xlabel("Year")
    plt.ylabel("Relative frequency")
    plt.grid(True)
    plt.show()

    

def  plot_relative_popularity(word1, word2,year_range, wfile, tfile):
    """This function plot the frequency of each word throughout a year range
    Parameters:
         word1: string. the fisrt word
         word2: string. the second word
         year_range: list. the first and last year of the year range.
         wfile: string. The name of the file that contain data of the word and the times it's repeat in the year range
         tfile: string. The name of the file that contain data the total times a word is mentioned in the year range
    """
    plt.figure()
    words = [word1, word2]
    ratio = []
    fig2_data = []
    plt.subplot(2, 1, 1)
    total = one_gram_reader.read_total_counts(tfile)
    for word in words:
        years, counts = one_gram_reader.read_wfile(word, year_range, wfile)
        normalized_counts = normalize_counts(years, counts, total)
        ratio.append(normalized_counts)
        plt.plot(years, normalized_counts)
    plt.legend(words)
    plt.xlabel("Year")
    plt.ylabel("Relative frequency")
    plt.subplot(2, 1, 2)
    for i in range(len(ratio[0])):
        fig2_data.append(ratio[0][i]/ratio[1][i])
    plt.plot(years, fig2_data)
    max_and_min = [max(fig2_data), min(fig2_data)]
    for data in max_and_min:
        pos = fig2_data.index(data)
        anno_year = years[pos]
        plt.annotate(str(anno_year), (anno_year, data))
    plt.legend([word1 + "\\" + word2])
    plt.ylabel("Frequency ratio")
    plt.xlabel("Year")
    plt.grid(True)
    plt.show()