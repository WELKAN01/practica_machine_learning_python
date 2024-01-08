
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from model_prediction import prediction


def message_data(list_field):
    prediction_class.set_sepal_width(float(list_field[0].get()))
    prediction_class.set_sepal_length(float(list_field[1].get()))
    prediction_class.set_petal_width(float(list_field[2].get()))
    prediction_class.set_petal_length(float(list_field[3].get()))
    if prediction_class.get_petal_length() is None or prediction_class.get_petal_width() is None or prediction_class.get_sepal_length() is None or prediction_class.get_sepal_width() is None:
        messagebox.showerror("Message","ingrese un valor de datos")
    else:    
        result= "\n".join([f"\n {atrribute} : {value} " for atrribute,value in vars(prediction_class).items()])
        messagebox.showinfo("Message",result)

def Interface(root:tk):
    #Interfaces de label y texto creados para almacenar
    label_field_sepal_width=ttk.Label(root,text="date sepal width :")
    entry_sepal_width=ttk.Entry(root)
    label_field_sepal_lenght=ttk.Label(root,text="date sepal lenght : ")
    entry_sepal_lenght=ttk.Entry(root)
    label_field_petal_width=ttk.Label(root,text="date petal width : ")
    entry_petal_width=ttk.Entry(root)
    label_field_petal_lenght=ttk.Label(root, text="date petal lenght : ")
    entry_petal_lenght=ttk.Entry(root)

    #insertar valores
    list_field=[entry_sepal_width,entry_sepal_lenght,entry_petal_width,entry_petal_lenght]
    #list_label=[label_field_sepal_width.cget("text"),label_field_petal_lenght.cget("text"),label_field_petal_width.cget("text"),label_field_petal_lenght.cget("text")]
    
    #se inserta el boton para dar efecto al mensaje
    buttonMessage=ttk.Button(root,text="click me ",command=lambda:message_data(list_field))
    
    #crear un grid que indica las posiciones que tendra 0-[1 a 4] sera de label y [1 a 4]-1
    label_field_sepal_width.grid(row=0,column=0,padx=10,pady=8)
    entry_sepal_width.grid(row=0,column=1, padx= 10,pady=8)
    label_field_sepal_lenght.grid(row=1,column=0,padx=10,pady=8)
    entry_sepal_lenght.grid(row=1,column=1,padx=10,pady=8)
    label_field_petal_width.grid(row=2,column=0,padx=10,pady=8)
    entry_petal_width.grid(row=2,column=1,padx=10,pady=8)
    label_field_petal_lenght.grid(row=3,column=0,padx=10,pady=8)
    entry_petal_lenght.grid(row=3,column=1,padx=10,pady=8)
    # se realiza una union de ambas columnas y se inserta el button
    buttonMessage.grid(row=4,columnspan=2,padx=10,pady=4)


if __name__ == "__main__":
    root=tk.Tk()
    root.title("prediccion")
    prediction_class=prediction(0.0,0.0,0.0,0.0)
    Interface(root)

root.mainloop()
