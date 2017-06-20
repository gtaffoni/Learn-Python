#
# importo i moduli che mi servono
#
import pyfits
import numpy as np
import matplotlib.pyplot as plot
plot.ion()

#
# carico le immagini 
#

biases = np.array([pyfits.getdata("./DATA/BIAS/ima00%d.fits" % n) for n in range(10,17)])
biases.shape

flats = np.array([pyfits.getdata("./DATA/FLAT/ima00%02d.fits" % n) for n in range(8,16)])
flats.shape

scidata = np.array([pyfits.getdata("./DATA/OBJ/ima0%03d.fits" % n) for n in range(1,211)])
scidata.shape

#
# notate che sono degli array a 3 dimensioni la dimensione 0 quella che indica l'immagine
#

#
# calcolo la mediana dei bias (voi non li avete per cui questo passo non potete farlo)
#
# notate che adesso ho un array 2D...ossia una immagine solo risultato della operazione di mediana dei bias
#

bias = np.median(biases, axis=0)
bias.shape

#
# calcolo la mediana dei flat
#

flat = np.median(flats, axis=0)

flat.shape

#
# leggo i dati da ridurre carico 210 immagini
#

rawdata = np.array([pyfits.getdata("./DATA/OBJ/ima0%03d.fits" % n) for n in range(1,211)])

rawdata.shape 


#
# faccio la riduzione nota che e' una operazione che faccio comtemporaneamente su tutti i dati 
#
# in teoria il conto da fare sarebbe:
#
# final = ((rawdata-dark)/(flat-bias))*mean(flat-bias)
#
# dove il dark e' la mediana dei dark.
# ma voi non avete ne' bias ne' dark per cui al posto del valor medio dei bias mettete 1834
#

reduced = (rawdata / flat ) * (np.mean(flat)-1834)
reduced.shape

#
# facciamo delle operazioni su una immagine 
#
data=reduced[0].copy()

#
# per visualizzarla bene posso calcolare un istogramma che mi permette di visualizzare la distribuzione del valore dei pixel
# 
plot.hist(data.ravel(), 256, range=(0.0, 10000.0))

plot.show()
#
# dato che il magior numero di pixel si trova tra 1500 e 2200 provo a visualizzare l'immagine impostando la scala dei grigi tra questi volori
#
# nota che serve solo per visulizzare meglio 
# 

plot.imshow(rawdata[0], cmap='Greys', vmax=2200,vmin=1500)
plot.show()
plot.imshow(data, cmap='Greys', vmax=2200,vmin=1500)
plot.show()
plot.imshow(reduced[0], cmap='Greys', vmax=2200,vmin=1500)
plot.show()
#
# usando il pulsantino che mi fa fare lo zoom cerco di trovare un intorno della stella che mi interessa 
#
# giocando un po' trovo che la stella e' centrata nel punto (644,518)
#
# ricavo un intorno
#
plot.imshow(reduced[0][510:526,635:654], cmap='Greys', vmax=2200,vmin=1500)
plot.show()
plot.imshow(reduced[0][510:527,636:654], cmap='Greys', vmax=2200,vmin=1500)
plot.show()
plot.imshow(reduced[0][510:527,637:654], cmap='Greys', vmax=2200,vmin=1500)
plot.show()
#
# faccio qualche tentativo per trovare il giusto riquadro che contiene la stella
# 
plot.imshow(reduced[0][510:527,637:653], cmap='Greys', vmax=2200,vmin=1500)
plot.show()


fluxes = np.array([np.sum(reduced[n,510:526,635:654]) for n in range(0,210)])
#
# o anche 
#
stars=reduced[:,510:527,637:653]
stars.shape

fluxes=np.array([np.sum(stars[n]) for n in range(0,210)])
fluxes.shape

time=np.arange(0,210)

plot.plot(time,fluxes)
plot.show()

#
# come plotto in funzione della data giuliana?
# 

rawdataheader = np.array([pyfits.getheader("./OBJ/ima0%03d.fits" % n) for n in range(1,211)])
rawdataheader.shape
rawdataheader[0]['JD-HELIO']
Jdate = np.array([rawdataheader[n]['JD-HELIO'] for n in range(0,rawdataheader.size)])
plot.plot(Jdate,fluxes)
plot.show()


#
# come seleziono un cerchio invece che un quadrato?
# 
# uso la funzione ogrid con xint,yint come coordinate del centro della stella (individuato visivamente)
#
xint=644
yint=518
r=9.2
y,x = np.ogrid[-xint:834-xint, -yint:1108-yint]

#
# creo una maschera che ha come indici zero se le coordinate distano piu' di r dal centro altrimenti 1
#
mask=x*x+y*y > r*r

#
# la apllico alla matrice
#
data[mask]=0
#
# cosa plottero'?
#
plot.imshow(data, cmap='Greys',clim=(1500,2000))
plot.show()

#
# calcolo il flusso (nota che la matrice e' tutti zeri tranne la stella)
#
flux = np.sum(data)
star_data=data.copy()

#
#
data=reduced[0].copy()
r=18
mask=x*x+y*y > r*r
data[mask]=0
plot.imshow(data, cmap='Greys',clim=(1500,2000))
plot.show()

bg_data=data-star_data

plot.imshow(bg_data, cmap='Greys',clim=(1500,2000)); plot.show()
plot.show()

#
# come lo applico a tutte le immagini contemporaneamente?
#

