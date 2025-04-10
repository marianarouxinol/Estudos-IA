import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.datasets import make_classification

# Gerando um conjunto de dados sintético
X, y = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42)

# Dividindo os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criando e treinando o modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Fazendo previsões
y_pred = model.predict(X_test)
y_pred_prob = model.predict_proba(X_test)[:, 1]  # Probabilidades para a classe positiva

# Calculando as métricas
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
auc_roc = roc_auc_score(y_test, y_pred_prob)

# Exibindo os resultados
metrics_df = pd.DataFrame({
    "Métrica": ["Acurácia", "Precisão", "Recall", "F1-Score", "AUC-ROC"],
    "Valor": [accuracy, precision, recall, f1, auc_roc]
})

print(metrics_df)
