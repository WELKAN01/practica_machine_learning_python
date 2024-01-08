
import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
class IrisModel:
    def __init__(self):
        names=['Sepal length','Sepal width','Petal length', 'Petal width','class']
        dataframe=pd.read_csv("iris.data.csv",names=names)
        ##se obtiene datos independientes, a excepcion de class que es el tipo de dato que es
        X=dataframe.drop('class',axis=1)

        ##se obtiene el dato eliminado anterior para obtener la clase, se va utilizar como etiqueta
        y=dataframe['class']

        """
        X: Las características del conjunto de datos.

        y: Las etiquetas (o valores objetivo) asociadas a cada muestra en el conjunto de datos.

        test_size: Especifica la proporción del conjunto de datos que se utilizará como conjunto de prueba. Por ejemplo, test_size=0.2 significa que el 20% de los datos se utilizarán como conjunto de prueba, y el 80% restante se utilizará como conjunto de entrenamiento.

        random_state: Controla la aleatoriedad de la división. Si proporcionas un número fijo a random_state, obtendrás la misma división cada vez que ejecutes tu código. Esto es útil para reproducibilidad.

        X_train, X_test: Conjuntos de características para entrenamiento y prueba, respectivamente.

        y_train, y_test: Conjuntos de etiquetas para entrenamiento y prueba, respectivamente.
        """
        X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

        self.rf=RandomForestClassifier(random_state=42,n_jobs=12)

        self.rf.fit(X_train,y_train)

        y_test_pred=self.rf.predict(X_test)

        accuracy= accuracy_score(y_test,y_test_pred)

        print(f"Accuracy on the tests set : {accuracy:,.2f}")

    
    def predict(self,predict_model):
        prediction=self.rf.predict(predict_model)
        return prediction

irisModel = IrisModel()
## es una sola fila 2-->[1-->1 filas[]]
new_data_test=np.array([[5.1, 1.2, 7.6, 2.5]])
predict_class= irisModel.predict(new_data_test)
print(f"prediccion de clase es :{predict_class}")