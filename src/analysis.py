# src/analysis.py

import matplotlib.pyplot as plt
import pandas as pd

def descriptive_stats(df, columns):
    """Returnerar medelvärde, median, min och max för valda kolumner."""
    return df[columns].agg(["mean", "median", "min", "max"])

def plot_histogram(df, column, title, xlabel):
    """Ritar ett histogram för en vald kolumn."""
    plt.figure(figsize=(8,5))
    plt.hist(df[column], bins=20, color="skyblue", edgecolor="black")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Antal personer")
    plt.grid(axis="y")
    plt.show()

def plot_boxplot_by_sex(df, column, title="Boxplot per kön"):
    """Ritar boxplot uppdelat på män och kvinnor."""
    male = df[df["sex"]=="M"][column]
    female = df[df["sex"]=="F"][column]
    plt.figure(figsize=(8,5))
    plt.boxplot([male, female], labels=["Män", "Kvinnor"])
    plt.title(title)
    plt.ylabel(column)
    plt.show()

def plot_disease_by_sex(df):
    """Ritar stapeldiagram över andel med sjukdom per kön."""
    disease_by_sex = df.groupby("sex")["disease"].mean()
    disease_by_sex.plot(kind="bar", color=["skyblue", "pink"])
    plt.title("Andel med sjukdom per kön")
    plt.ylabel("Andel")
    plt.show()
