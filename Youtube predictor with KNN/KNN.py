import tkinter as tk
from Logic import Proy3

class Run:
    def __init__(self):
        self.names_var = ""
        self.numbers_var = 0
        self.UI()

    def Boton(self):
        selected_name = self.names_var.get()
        selected_number = int(self.numbers_var.get())
        Proy3(selected_number,selected_name)

    def UI(self):
        root = tk.Tk()
        root.title("Proyecto 3er parcial")
        root.geometry("500x600")

        # Crea opciones
        names = ["INvideos","MXvideos", "CAvideos", "DEvideos", "FRvideos","GBvideos","JPvideos","KRvideos","RUvideos"]
        numbers = [1, 2, 3, 4,5,6,7,8,9,10,50,100,250,500]
        self.names_var = tk.StringVar(root)
        self.numbers_var = tk.StringVar(root)
        self.names_var.set(names[0])
        self.numbers_var.set(numbers[0])

        # Creacion de listas
        names_list = tk.OptionMenu(root, self.names_var, *names)
        numbers_list = tk.OptionMenu(root, self.numbers_var, *numbers)

        # crea Boton
        run_button = tk.Button(root, text="Run", command=self.Boton,background="red",width="6",height="3")

        # Agrega a UI
        names_list.place(relx = 0.5, rely = 0.25, anchor = 'center')
        numbers_list.place(relx = 0.5, rely = 0.50, anchor = 'center')
        run_button.place(relx = 0.5, rely = 0.75, anchor = 'center')

        root.mainloop()



if __name__ == "__main__":
    run = Run()
