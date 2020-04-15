from datetime import datetime, date, time, timedelta
"""if c == fecha[0]:
		ahora = datetime.now()
		y = ahora.day
		h = ahora.month
		 = ahora.year
		f = ahora.hour"""

"""ahora = datetime.now()  
ahorita = datetime.today()      
print(ahora)
print(ahorita)
new_date = datetime(2019, 2, 28)
print(new_date)
y = ahora.day
h = ahora.month
 = ahora.year
f = ahora.hour
g = ahora.minute
print(y)
print(h)
print()
print(f)
print(g)"""
"""h=int(input("ingrese day: "))
i=int(input("ingrese month: "))
j=int(input("ingrese year: "))
k=int(input("ingrese hour: "))
l=int(input("ingrese minute: "))
m=int(input("ingrese : "))"""

class Tiempo:

    def now(self):
        self.ahora = datetime.now()
        print (self.ahora)
        return self.ahora

    def desarmar_fecha_y_hora(self,):
        d=self.ahora.day
        m=self.ahora.month
        y=self.ahora.year
        h=self.ahora.hour
        mi=self.ahora.minute
        self.lista_hora = [d,m,y,h,mi]
        return self.lista_hora

    def armar_hora(self):
        lista_hora2=[]
        for i in range (5):
            if i==0:
                print("ingrese dia: ")
                d=int(input())
                lista_hora2.append(d)


time=Tiempo()
time.now()
time.desarmar_fecha_y_hora()
time.armar_hora()