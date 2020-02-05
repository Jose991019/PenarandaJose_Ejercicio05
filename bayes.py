import numpy as np
import matplotlib.pyplot as plt

cadena = "scccc"
Nc = cadena.count("c")
Ns = cadena.count("s")
def prob(H):
    return((H**Nc)*((1-H)**Ns))
H = np.linspace(0.000001,1-1e-5,100)
y = prob(H)
normalizacion = np.trapz(y, x = H)
nuevoY = y/normalizacion
L = np.log(nuevoY)

maximo = np.max(nuevoY)
H0 = int(np.where(nuevoY == maximo)[0])

deriv2 = (L[H0+1] - 2*L[H0] + L[H0-1])/(H[H0]-H[H0-1])**2

sigma = (-deriv2)**(-1/2)

def aprox(H): 
    A = 1.0/(np.sqrt(2*np.pi)*sigma)
    return(A*np.exp(-0.5*(H-H[H0])**2/sigma**2))

yaprox = aprox(H)

plt.plot(H,nuevoY)
plt.plot(H,yaprox,"--")
plt.title("H = {} {} {:.3f}".format(H0,"$\pm$",sigma))
plt.xlabel("H")
plt.ylabel("P(H|{prob})")
plt.savefig("coins.png")