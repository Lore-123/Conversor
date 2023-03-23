#Maria Jennifer Carbajal Martinez 41s
#Lorenzo Hernandez Hernandez 41s
#Conversor de monedas
from tkinter import*
from tkinter import ttk
from PIL import ImageTk,Image
root = Tk()

ventanaPrincipal = Frame(root)
ventanaPrincipal.grid()
imge = Image.open("C:\\Users\\nisha\\OneDrive\\Escritorio\\TECNOLOGICO\\4to Semestre\\PROGRA VIS\\moneda.jpg")
imagens = imge.resize((70,70))
imagenA = ImageTk.PhotoImage(imagens)
Ponerimagen = Label(ventanaPrincipal, image=imagenA, bg="#0099FF").grid(row=5,column=2,columnspan=1,rowspan=6)

root.title("Conversor")

def Conversor():

    if monedaS.get()!=Conversormoneda.get():

        
        if Conversormoneda.get()=="USD":

            if monedaS.get()=="EUR":
                resultado = moneda.get()*1.07
                numText2.config(text=f'{resultado} USD')
                
            if monedaS.get()=="MXN":
                resultado = moneda.get()*0.030
                numText2.config(text=f'{resultado} USD')    
        
                
        if Conversormoneda.get()=="MXN":
    
            if monedaS.get()=="USD":
                resultado = moneda.get()*18.59
                numText2.config(text=f'{resultado} MXN')

            if monedaS.get()=="EUR":
                resultado = moneda.get()*20.21
                numText2.config(text=f'{resultado} MXN')

        if Conversormoneda.get()=="EUR":

            if monedaS.get()=="USD":
                resultado = moneda.get()*0.92
                numText2.config(text=f'{resultado} EUR')
            
            if monedaS.get()=="MXN":
                    resultado = moneda.get()*0.049
                    numText2.config(text=f'{resultado} EUR')

    else:
        numText2.config(text=f'Select different option')

moneda = IntVar()
Conversormoneda = StringVar()
monedaS = StringVar()

ventanaPrincipal = Frame(root, bg="#0099FF")
ventanaPrincipal.grid()

tiituuloon = Label(ventanaPrincipal, text="Convert Money", font=("Aurora",20,"bold"), bg="#0099FF", fg="black")
tiituuloon.grid(row=1, column=1, padx=10, columnspan=2)

tiituuloon = Label(ventanaPrincipal, text="Quantity", font=("Vanilla Caramel",15,"bold"), bg="#0099FF", fg="black")
tiituuloon.grid(row=2, column=1, padx=10, pady=10)

numText1 = Entry(ventanaPrincipal, font=("Vanilla Caramel",15), textvariable=moneda).grid(row=2, column=2, padx=10, pady=10)

tiituuloon = Label(ventanaPrincipal, text="Value to convert", font=("Vanilla Caramel",15,"bold"), bg="#0099FF", fg="black")
tiituuloon.grid(row=3, column=1, padx=10, pady=10)

Lista = ttk.Combobox(ventanaPrincipal,values=["USD", "MXN", "EUR"], state="readonly", textvariable=monedaS).grid(row=4, column=1, padx=10, pady=10)

tiituuloon = Label(ventanaPrincipal, text="Converted", font=("Vanilla Caramel",15,"bold"), bg="#0099FF", fg="black")
tiituuloon.grid(row=3, column=2, padx=10, pady=10)

Lista = ttk.Combobox(ventanaPrincipal,values=["USD", "MXN", "EUR"], state="readonly", textvariable = Conversormoneda).grid(row=4, column=2, padx=10, pady=10)

tiituuloon = Label(ventanaPrincipal, text="Resultado", font=("Vanilla Caramel",15,"bold"), bg="#0099FF", fg="black")
tiituuloon.grid(row=5, column=1, padx=10, pady=10)

numText2 = Label(ventanaPrincipal, text="", font=("Vanilla Caramel",15), bg="#0099FF")
numText2.grid(row=5, column=2, padx=10, pady=10)

botonConvertir = Button(ventanaPrincipal, text="Convertir", font=("Vanilla Caramel",15), command=Conversor).grid(row=6, column=1, padx=10, pady=10, columnspan=2)

root.mainloop()