import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

def Proy3(K_Vecinos,DataSet):
    # Cargar dataset
    data = pd.read_csv(f"./Main/Youtube predictor with KNN/Datasets/{DataSet}.csv",encoding="latin1")
    #data = data.dropna()
    # Separa para entrenamiento y prueba
    X = data[["views"]]
    y = data[["likes"]]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=1, shuffle=True)
    # crea el modelo con K vecinos
    knn = KNeighborsRegressor(n_neighbors=K_Vecinos)

    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    #calcula el error
    mse = mean_squared_error(y_test, y_pred)
    #acc =accuracy_score(y_test , y_pred)
    print(f"Mean Squared Error: {mse}\tKvecinos: {K_Vecinos}\tRegion:{DataSet}")
    # imprime
    plt.scatter(X_test, y_test, color="red")
    plt.scatter(X_test, y_pred, color="blue")
    plt.xlabel("Vistas")
    plt.ylabel("Likes")
    plt.show()


    