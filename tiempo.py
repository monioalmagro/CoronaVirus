from datetime import datetime, date, time, timedelta


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
            if i==1:
                print("ingrese mes: ")
                d=int(input())
                lista_hora2.append(d)
            if i==2:
                print("ingrese ano: ")
                d=int(input())
                lista_hora2.append(d)
            if i==3:
                print("ingrese hora: ")
                d=int(input())
                lista_hora2.append(d)
            if i==4:
                print("ingrese minutos: ")
                d=int(input())
                lista_hora2.append(d)
        #print(lista_hora2)
        self.new_date=datetime(lista_hora2[2],lista_hora2[1],lista_hora2[0],lista_hora2[3],lista_hora2[4])        
        #print(self.new_date)
        self.new_date

        

"""

time=Tiempo()
time.now()
time.desarmar_fecha_y_hora()
time.armar_hora()
"""