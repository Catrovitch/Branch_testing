# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan ohjelman")

x = int(input("luku 1: "))
y = int(input("luku 2: "))
print(f"{x} + {y} = {summa(x, y)}") # muutos masterissa
print(f"{x} - {y} = {erotus(x, y)}") # muutos masterissa

logger("lopetetaan")
print("goodbye!")
