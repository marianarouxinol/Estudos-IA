import pandas as pd

arquivo = "logs_treinamento.csv"

try:
    frame = pd.read_csv(arquivo)
    if 'tempo_execucao' not in frame.columns:
        raise ValueError("A coluna 'tempo_execucao'")
    media = frame['tempo_execucao'].mean()
    desvio_padrao = frame['tempo_execucao'].std()
    print(f"Média do tempo de execução: {media:.2f}")
    print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f}")

except FileNotFoundError:
    print(f"Erro, o {arquivo} não foi encontrado")
except ValueError as e:
    print(f"Erro: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")