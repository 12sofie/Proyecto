#-*- coding: utf-8 -*-

from tkinter import *
from turtle import bgpic
import tkinter.messagebox
from tkinter import ttk
from tkinter import filedialog
from AL import AL


class Ventana:
    def __init__(self) -> None:
        pass

    def openFiles(self):

        filepath=filedialog.askopenfilename(initialdir="/", title="Seleccionar Archivos",filetypes=(("text files","*.txt"),("all files","*.*")))
        if filepath is not None:
            self.fileNameText.insert(INSERT,filepath)
            f= open (filepath,'r')
            self.lines=f.read()
            self.content=self.lines.split(' ')
            self.txtContentText.insert(INSERT,self.content[0])
            f.close()

    def resolveOperation(self):
        self.operationResult=[]
        self.lex=AL()
        self.operationResult = self.lex.analizador(self.content[0])
        print (self.operationResult)
        self.resultText.insert(0,self.operationResult)
      
     
    def clear(self):
        """
            Este método limpia las entradas de texto una vez que se ha terminado de encriptar, para poder repetir el proceso de encriptación
            cuantas veces se desee sin necesidad de volver a ejecutar el programa.
        """   
        self.fileNameText.delete("1.0",END)
        self.resultText.delete(0,END) 
        self.txtContentText.delete(0,END)
       
        self.content = ''

    
    def setup(self,root):
        """
            Este método contiene la interfaz principal del programa, que es una ventana que contiene todos los botones,
            etiquetas, y entradas de texto.

            @param {tk} root es la ventana donde se van a almacenar todos los widgets.
        """

        self.indicator = 0 
        self.root= root
   
        windowWidth=1000
        windowHeight=500

        screenWidth1=self.root.winfo_screenwidth()
        screenHeight1=self.root.winfo_screenheight()
        x=(screenWidth1/2)-(windowWidth/2)
        y=(screenHeight1/2)-(windowHeight/2)

        
        self.root.title("Calculadora") 
        #Centrar ventana principal en pantalla
        #Dimensiones de la ventana principal
        
        #Aqui se obtiene la información del ancho y largo de la ventana
        
        #se realizan los calculo para colocar la ventana principal al centro de la pantalla
        
        #con el metodo "geometry" se le asigna a la ventana los valores que la colocaran en el centro de la pantalla

        self.root.geometry(f'{windowWidth}x{windowHeight}+{int(x)}+{int(y)}')
        
        
        self.root.config(bg="#1E385B") # color de fondo

        #Creación de Label inicial
        self.fileName=Label(self.root, text="CALCULADORA DE OPERACIONES",bg="#1E385B",fg="#000000",  font=("Tahoma", 35, "bold"))
        self.fileName.place(x=80,y=30)
        
        self.fileNameText= Text(self.root, relief=FLAT,bg="white",font=("yu gothic ui semibold",12))
        self.fileNameText.place(x=200,y=110,width=450, height=35)

        #Creación de Label final
        self.fileName=Label(self.root, text="DISEÑO DE COMPILADORES",bg="#1E385B",fg="#000000", font=("Bremen BD BT",35,"bold"))
        self.fileName.place(x=150,y=350)
    
        self.txtContentText= Text(self.root,relief=FLAT,bg="white",font=("yu gothic ui",12, "bold"))
        self.txtContentText.place(x=200,y=200,width=450, height=35)

        
        #Boton de selecciónar
        self.btn_selection1= Button(self.root,font=("yu gothic ui",12,"bold"), relief="raised", activebackground="white", cursor="hand2",width=14,height=1, borderwidth=2, text="Seleccionar archivo", fg="white", bg="#000000",command =self.openFiles)
        self.btn_selection1.place(x=20,y=110)

        #Boton de calcular y entry para calcular 
        self.btn_execute= Button(self.root,font=("yu gothic ui",12,"bold"), relief="raised", activebackground="white", cursor="hand2",width=16,height=1, borderwidth=2, text="Calcular", fg="white", bg="#000000" ,command =self.resolveOperation)
        self.btn_execute.place(x=20,y=200)
        self.txtContentText= Entry(self.root, relief=FLAT,bg="white",font=("yu gothic ui",12,"bold"))
        self.txtContentText.place(x=200,y=200,width=450, height=35)
      

        #Creación de Label y entry para el resultado
        self.result=Label(self.root, text="Resultado: ",bg="#1E385B",fg="#000000", font=("Bremen BD BT",20,"bold"))
        self.result.place(x=20,y=290)

        self.resultText= Entry(self.root, relief=FLAT,bg="white",font=("yu gothic ui",12,"bold"))
        self.resultText.place(x=200,y=290,width=450, height=35)
        
        #Boton de Borrar
        self.btn_clear= Button(self.root,font=("yu gothic ui",12,"bold"), relief="raised", activebackground="white", cursor="hand2",width=16, height=2,borderwidth=2, text="Borrar", fg="white", bg="#000000", command = self.clear)
        self.btn_clear.place(x=700,y=150)

       

        #Boton para salir 
        self.btn_exit= Button(self.root,font=("yu gothic ui",12,"bold"), relief="raised", activebackground="white", cursor="hand2",width=16, height=2,command=self.root.quit, borderwidth=2, text="Salir", fg="white", bg="#000000")
        self.btn_exit.place(x=700,y=250)

