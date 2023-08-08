# -*- coding: utf-8 -*-
import re
from unicodedata import digit
from Table import Table
from tkinter import*
import tkinter as tk 
from tkinter import ttk 


class AL:
    def __init__(self) -> None:
        pass

    def analizador(self,Exp):
        self.digits = r'[0-9]+'
        self.operators = r'[+]|[\-]|[*]|[\/]|[\(\|[\)]|[[]|[]]|[\^]'
        self.t_operators= []
        self.t_operators=[]
        self.t_digits= []
        self.function= []
        self.resume_table = []

        'Recorremos la expresion caracter a caracter para identificar numeros y operadores'
        for i in Exp:
            'Si se encuentra un operador se agrega al arreglo de operadores'
            if re.match(self.operators,i):
                self.t_operators.append(i)
            'Si se encuentra un digito se agrega al arreglo de digitos'
            if re.match(self.digits,i):
                self.t_digits.append(i)

        print('Se identificaron {} digitos: {}'.format(len(self.t_digits), self.t_digits))
        print('Se identificaron {} operadores: {}'.format(len(self.t_operators), self.t_operators))

        'Definimos expresiones regulares para identificar operaciones'
        expSum = re.findall(r'\d+\+\d+\*\(|\d+\+\d+',Exp) #\d+\+\d+|\*\(
        expRest = re.findall(r'\d+\-\d+\*\(|\d+\-\d+',Exp)
        expMult = re.findall(r'\d+\*\d+|\d+\*\(',Exp) #\d+\*\d+          \d+\*\((\d+\W\d+)+\)$            \d+\*\((\d+[\*+-/]\d+)+\)$
        expDiv = re.findall(r'\d+\/\d+|\d+\/\(',Exp)
        expExp = re.findall(r'\d+\^\d+|\d+\^\(', Exp)


        self.function.append("Funciones: ")
        self.t_operators.insert(0, "Operadores: ")
        self.t_digits.insert(0, "Números Enteros: ")


        if expSum != None:
            #c = 0
            for i in expSum:
                self.function.append("OperaciónSuma: {}".format(self.evaluateExpr(i)))
                #if c == 0:
                    #self.function.append("OperaciónSuma: {}".format(self.evaluateExpr(i)))
                    #c = c+1
                #else:
                    #self.function.append(", {} ".format(self.evaluateExpr(i)))

        if expRest != None:
            for i in expRest:
                self.function.append("OperaciónResta: {}".format(self.evaluateExpr(i)))

        if expMult != None:
            for i in expMult:
                self.function.append("OperaciónMultiplicación: {}".format(self.evaluateExpr(i)))

        if expDiv != None:
            for i in expDiv:
                self.function.append("OperaciónDivisión: {}".format(self.evaluateExpr(i)))

        if expExp != None:
            for i in expExp:
                self.function.append("OperaciónExponencial: {}".format(self.evaluateExpr(i)))


        #print('Antes de el print self.function')
        #print(self.function)

        self.resume_table.append(self.function)
        self.resume_table.append(self.t_operators)
        self.resume_table.append(self.t_digits)

        table = Tk()
        table.title("Resumen de Ejecución")

        t = Table(table,self.resume_table)

        """parser.expr(): analiza la expresion  y si el análisis sintáctico tiene éxito, se crea un objeto ST 
        para contener la representación del árbol de análisis sintáctico interno

        compile(): invoca un objeto ST para producir objetos de código que se pueden usar como 
        parte de una llamada a las function incorporadas exec() o eval().
        """
        #analisis sintactico
        self.expresion = Exp  # parser.expr(Exp).compile()
        #print(self.expresion)
        self.result = eval(self.expresion)
        #print(self.result)
        return self.result


    def evaluateExpr(self,i):
        for j in i:
            if j == "(" :
                return "{}Exp)".format(i)
        return i
