from dataclasses import dataclass
from turtle import clear
import numpy as nump #linear algebra
import pandas as panda #datapreprocessing, CSV file I/O
import seaborn as sns #for plotting graphs
import matplotlib.pyplot as plotter

datos = panda.read_csv("homes.csv")


#print(datos.head(5))\

#print(datos.shape)

#print(datos.isnull().sum())


print(sns.countplot(data=datos,x=datos['bedrooms']))