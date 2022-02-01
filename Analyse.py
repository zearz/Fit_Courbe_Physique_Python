import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly

#Pas de mot en premiere ligne des deux colonnes sinon ça marche pas et c'est dommage

def analyse(cheminDUfichier):
    data= np.loadtxt(cheminDUfichier, delimiter=';')
    x = data[:,1] #la deuxième colonne de donnée
    y = data[:,0] #la première colonne de donnée
    model1 = np.poly1d(np.polyfit(y, x, 1))
    print(model1.c) #le fit en degrè 1
    def f(y): #fonction pour tracer le fit 
        return (model1.c[0]*y)+model1.c[1]
    plt.plot(y, f(y), color='green',label = "Courbe fit (formule : {pre:f}x + {deu:f})".format(pre = model1.c[0],deu=model1.c[1])) #Plot le fit
    plt.plot(y,x,label = "Courbe Sans fit") #plot la courbe
    plt.title(cheminDUfichier) #Nom du plot


analyse("XXX") #Chemin d'accès pour le fichier

plt.xlabel("L'axe X") #Nom de l'axe x
plt.ylabel("L'axe Y") #Nom de l'axe y
plt.legend()
plt.show()
