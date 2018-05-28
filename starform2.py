import numpy as np
import pylab as plt

def y(t, ms, tgas,c,mgas) :
    return ( c * mgas/tgas*t**2)


def rk4(t,ms,h,tgas,c,mgas):
    k1 = h*y(t, ms, tgas,c,mgas)
    k2 = h*y(t+h/2,ms+k1/2., tgas,c,mgas)
    k3 = h*y(t+h,ms+k2/2., tgas,c,mgas)
    k4 = h*y(t+h, ms+k3, tgas,c,mgas)    
    return ms + k1/6. + k2/3. + k3/3. + k4/6.

NINT=10
mg=1.e6
tgas = 2. 
c = 0.1
ms=0.

tfin=10.
tn = 0.
h = tfin/NINT


t=np.empty(0)
Ms=np.empty(0)
Mg=np.empty(0)
while tn<tfin:
    if mg >0.:
        msp1 = rk4(tn,ms,h,tgas,c,mg)
        Ms=np.append(Ms,msp1)
        
        tn += h
        t=np.append(t,tn)

        mg -= (msp1-ms)
        ms=msp1
        Mg=np.append(Mg,mg)

    else:
        tn += h
        t=np.append(t,tn)
        Mg=np.append(Mg,0.0)
        Ms=np.append(Ms,Ms[-1])
        
    

#plt.loglog()
plt.plot(t,Ms,label='Mstar',color='red')
plt.plot(t,Mg,label='Mgas',color='blue')

plt.legend(loc='best')
plt.show()
