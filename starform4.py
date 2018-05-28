import numpy as np
import pylab as plt
from scipy.integrate import odeint

def derivs(y, t, tgas,c) :
    dydt=np.array([0.,0.])
    if y[1]>0.:
        dydt[0]= ( c * y[1]**1.5/tgas)
        dydt[1]= -dydt[0]
        
    return dydt


mg=1.e6
tgas = 2. 
c = 0.1
ms=0.

t=np.arange(0,10.,0.001)
y0=np.array([ms,mg])

Y=odeint(derivs,y0,t,args=(tgas,c))


plt.loglog()
plt.plot(t, Y[:,0],label='Mstar',color='red')
plt.plot(t, Y[:,1],label='Mgas',color='blue')

plt.legend(loc='best')
plt.show()
