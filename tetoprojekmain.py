import math

print("(Bartha-Nyiri Adrienn, Subicz Adrian, Szeifert Nora, Szikszai Akos)\n")

a = 9.6  #tető a oldal hossza
b = 3.2   #tető b oldal hossza
c = 23    #tető magassága


d = math.sqrt( (a/2)**2 + b**2 )  #a tető d oldalának hossza

et = c * d * 2   #a tető területe 

print("A tető területe:", '% .2f' % et , 'négyzetméter')

cs = 0.25 * 0.12 #cserép területe

print('Egy darab cserép területe:',cs,'\n')

darab = math.ceil( (et * 1.1) / cs)

print(darab, "db cserép kell a tető befedéséhez +10%-kal")
