lista=[]
lista2=[]
import datetime

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

"""    conexion=sqlite3.connect("bd1.db")

def sql_insert(conexion, cifras):

    cursorObj = conexion.cursor()
    
    cursorObj.execute('INSERT INTO corona(codigo, Pais, Confirmados, Casos_por_millon_de_personas, Recuperados,Muertes) VALUES(?, ?, ?, ?, ?, ?)', cifras)
    
    conexion.commit()

cifras = (2,'Ana', 2.2,43 , 365, 95)

sql_insert(conexion, cifras)"""




