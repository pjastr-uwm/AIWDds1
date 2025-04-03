import pandas as pd

dane = pd.read_csv("gastro21.csv", header=None).T
dane.columns = ["Rodzaj", "Rok", "Wartość"]
dane["Rok"] = dane["Rok"].astype(int)
dane["Wartość"] = dane["Wartość"].astype(int)