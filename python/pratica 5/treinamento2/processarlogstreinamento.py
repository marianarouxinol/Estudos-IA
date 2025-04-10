import pandas as pd
import numpy as np
df = pd.read_csv("logs_treinamento.csv")
media = df["tempo_execucao"].mean()
desvio_padrao = df["tempo_execucao"].std()
print(f"Média do tempo de execução: {media:.2f}")
print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f}")