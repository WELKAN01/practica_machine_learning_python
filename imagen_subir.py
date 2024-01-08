import tkinter as tk


def interface_imagen(root:tk):
    label_imagen=root.Tk.Label(text="suba la direccion de la imagen")
    label_imagen.grid(column=0,row=0,padx=10,pady=10)
    return


if __name__=="__main__" :
    root=tk.Tk()
    root.title("subir imagen")
    interface_imagen(root=root)

root.mainloop()
    