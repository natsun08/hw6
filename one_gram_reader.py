"""
Homework 6
Author: Dan Nguyen and Ha Chi
"""
import csv

def read_wfile(word,year_range,wfile):      
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


def read_total_counts(wfile):
    total_counts ={}
    with open(wfile,"r" , newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter = ",", fieldnames =["year","total words","pages", "source count"])
        for row in reader:
            total_counts[int(row["year"])] = int(row["total words"])
        return total_counts
    