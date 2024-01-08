import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Creamos datos de ejemplo
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
y = np.array([0, 0, 1, 1])

# Sin especificar random_state
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
print("División de datos sin especificar random_state:")
print("Conjunto de entrenamiento:", X_train)
print("Conjunto de prueba:", X_test)

# Especificando random_state
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=5)
print("\nDivisión de datos especificando random_state=42:")
print("Conjunto de entrenamiento:", X_train)
print("Conjunto de prueba:", X_test)

# Entrenamiento de un modelo de regresión logística sin especificar random_state
model_1 = LogisticRegression()
model_1.fit(X_train, y_train)
acc_1 = model_1.score(X_test, y_test)
print("\nPrecisión del modelo 1:", acc_1)

# Entrenamiento de otro modelo de regresión logística especificando random_state=42
model_2 = LogisticRegression(random_state=42)
model_2.fit(X_train, y_train)
acc_2 = model_2.score(X_test, y_test)
print("Precisión del modelo 2:", acc_2)
