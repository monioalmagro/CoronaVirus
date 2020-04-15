import datetime
import sqlite3

def crear_base_de_datos():
    conexion=sqlite3.connect("basededatos2.db")
    
    conexion.execute("""create table tiempo (
                        codigo integer primary key AUTOINCREMENT,
                        data TIMESTAMP                         
                        )""")
    print("se creo la tabla tiempo")                        
        #except sqlite3.OperationalError:
         #   print("La tabla tiempo ya existe")                    
    conexion.close()
        
        



#today = datetime.date.today()
#print('Today    :', today)

#$one_day = datetime.timedelta(days=1)
#print('One day  :', one_day)

#yesterday = today - one_day
#print('Yesterday:', yesterday)

#tomorrow = today + one_day
#print('Tomorrow :', tomorrow)

#print()
#print('tomorrow - yesterday:', tomorrow - yesterday)
#print('yesterday - tomorrow:', yesterday - tomorrow)
crear_base_de_datos()
aohorita=datetime.datetime.now()
d = datetime.date.today()
lista=[]
#aohorita



print(d)
str(d)
print(d)
print(aohorita)
conexion=sqlite3.connect("basededatos2.db")
cursorObj = conexion.cursor()
cursorObj.execute('INSERT INTO tiempo(data) VALUES(?)', str(d))
conexion.commit()


cifras = (2,'Ana', 2.2,43 , 365, 95)















"""
today = datetime.date.today()
print(today)

for x in range (100):
    lista.append(x)
while len(lista)>4:    
    print(lista)
    for x in range(5):
        q=lista[x]
        lista2.append(q)
    print(lista2)
    print("esto es el primer dato:",lista2[0])
    perro=lista2[3]
    print("perro",perro)
    for x in range(5):
        lista.pop(0)
        lista2.pop(0)     
    print(lista)
"""
"""    conexion=sqlite3.connect("bd1.db")

def sql_insert(conexion, cifras):

    cursorObj = conexion.cursor()
    
    cursorObj.execute('INSERT INTO tiempo( Pais, Confirmados, Casos_por_millon_de_personas, Recuperados,Muertes) VALUES(?, ?, ?, ?, ?, ?)', cifras)
    
    conexion.commit()

cifras = (2,'Ana', 2.2,43 , 365, 95)

sql_insert(conexion, cifras)"""




