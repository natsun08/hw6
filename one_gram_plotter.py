import matplotlib as mpl
import matplotlib.pyplot as plt
import csv
import one_gram_reader

def normalize_counts(years, counts, total):
    norm = []
    for i in range(len(years)):
        norm.append(counts[i]/total[years[i]])
    return norm
def plot_words(words, year_range, wfile, tfile):
    total = one_gram_reader.read_total_counts(tfile)
    for word in words:
        years, counts = one_gram_reader.read_wfile(word, year_range, wfile)
        normalized_counts = normalize_counts(years, counts, total)
        plt.plot(normalized_counts.keys(), normalized_counts.values())
    plt.legend(words)
    plt.xlabel("Year")
    plt.ylabel("Usage")
    plt.grid(True)
    plt.show()
