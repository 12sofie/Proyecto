from tkinter import *

class Table:

    def __init__(self,root,t_resumen):
        
        totalRows = len(t_resumen)
        t_resumen.sort(reverse = True)
        totalcolumns = len(t_resumen[0])      
        
        for i in range(totalRows): 
                for j in range(totalcolumns):     
                    resp = Entry(root, width=27, font=("Arial",10))
                    #resp.place(x=25, y=255, height="200", width="450")
                    resp.grid(row=i, column=j) 
                    try :
                        resp.insert(END, t_resumen[i][j]) 
                    except IndexError:
                        resp.insert(END, " ") 