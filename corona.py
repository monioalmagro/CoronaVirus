from selenium import webdriver
import time
import sqlite3
import datetime
from datetime import datetime, date

class data_processing:
    
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path = "/home/almagro/Escritorio/Selenium/chromedriver")


    def abrir_pagina(self):
        print("Abriendo pagina")
        self.driver.get("https://google.com/covid19-map/?hl=es-419")
        time.sleep(5)
        print("Midiendo matriz")

    def medir_matriz(self):
        self.rows = len(self.driver.find_elements_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div[2]/div/div[2]/div[4]/div[1]/div[1]/div/div[2]/div/div[1]/table/tbody/tr"))
        self.col =  len(self.driver.find_elements_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div[2]/div/div[2]/div[4]/div[1]/div[1]/div/div[2]/div/div[1]/table/tbody/tr[1]/td"))
        #print(self.rows)
        #print(self.col)
        #return self.rows, self.col
        print("Obteniendo datos")

    def obtener_datos(self):
        self.lista=[]
        for n in range(2 ,self.rows+1):
            for b in range(1,self.col+1):
                self.dato = self.driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div[2]/div/div[2]/div[4]/div[1]/div[1]/div/div[2]/div/div[1]/table/tbody/tr["+str(n)+"]/td["+str(b)+"]").text
                self.lista.append(self.dato)
        #print(self.lista)
                #print(self.dato)
                #print("esto es n:",n)
                #print("esto es b:",b)
                #print()
        print("conectando con la  base de datos")        
        return self.lista        

    

    def crear_base_de_datos(self):
        self.conexion=sqlite3.connect("basededatos.db")
        try:
            self.conexion.execute("""create table corona (
                                codigo integer primary key AUTOINCREMENT,
                                Pais,
                                Confirmados,
                                Casos_por_millon_de_personas,
                                Recuperados,
                                Muertes,
                                date
                                )""")
            print("se creo la tabla corona")                        
        except sqlite3.OperationalError:
            print("La tabla corona ya existe")                    
        self.conexion.close()
        print("Cortando listas")

    


    def cortado_de_lista(self):
        print("terminando")
        self.today = datetime.now()
        self.lista2=[]
        while len(self.lista)>4:
            for x in range(5):
                q=self.lista[x]
                self.lista2.append(q)
            #print(self.lista2)
            #print("esto es el primer dato:",self.lista2[0])
            self.country=self.lista2[0]
            self.confir=self.lista2[1]
            self.casos=self.lista2[2]
            self.recu=self.lista2[3]
            self.dead=self.lista2[4]
            self.cifras=[self.country,self.confir,self.casos,self.recu,self.dead,self.today]
            self.conexion=sqlite3.connect("basededatos.db")
            self.cursorObj = self.conexion.cursor()
            self.cursorObj.execute('INSERT INTO corona( Pais, Confirmados, Casos_por_millon_de_personas, Recuperados,Muertes,date) VALUES(?, ?, ?, ?, ?,?)', self.cifras)
            self.conexion.commit()
            #self.fecha=self.lista2[5]
            for x in range(5):
                self.lista.pop(0)
                self.lista2.pop(0)
    
        """def insertar_datos(self,cifras):
            self.conexion=sqlite3.connect("basededatos.db")
            self.cursorObj = self.conexion.cursor()
            self.cursorObj.execute('INSERT INTO corona( Pais, Confirmados, Casos_por_millon_de_personas, Recuperados,Muertes) VALUES(?, ?, ?, ?, ?)', self.cifras)
            self.conexion.commit()            """

    def cerrar_chrome(self):
        self.driver.close()
        print("listo.!")



            

                


script=data_processing()
script.abrir_pagina()
script.medir_matriz()
script.obtener_datos()
script.crear_base_de_datos()
script.cortado_de_lista()
script.cerrar_chrome()

