"""
Homework 6
Author: Dan Nguyen and Ha Chi
"""
import csv

def read_wfile(word,year_range,wfile):
    """ This function return the number of time a word is repeated in the given year range
        Parameter:
            word: string. The word being repeated
            year_range: list. The year range that we want to see the number of times the word being repeated
            wfile: string. The file name contain the data.
        Return:
            years: list. A list of years the word being repeated
            counts: list. A list of the number of time the word being repeated in the respective year
    """
    years = []
    counts = []
    with open(wfile,"r" , newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter = "\t", fieldnames= ["word", "year", "word count", "source count"])
        for row in reader:
            row["year"] = int(row["year"])
            row["word count"] = int(row["word count"])
            if row["word"] == word and row["year"] in range(year_range[0], year_range[1]+1):
                years.append(row["year"])
                counts.append(row["word count"])
        return years, counts


def read_total_counts(tfile):
    """ This function return a dictionary of the total word count within their respective year
        Parameter:
            tfile: string. The file name of the data
        return:
            total_counts: Dictionary. A dictionary of the total word count within each year.
    """
    total_counts ={}
    with open(tfile,"r" , newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter = ",", fieldnames =["year","total words","pages", "source count"])
        for row in reader:
            total_counts[int(row["year"])] = int(row["total words"])
        return total_counts
    