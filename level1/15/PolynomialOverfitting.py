import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
x=np.linspace(0,2*np.pi,30)
y=np.sin(x)+0.2*np.random.randn(len(x))
#fit polynomials
degrees=range(1,11)
plt.figure(figsize=(15,10))
plt.scatter(x,y,color='black',label='data')
x_plot=np.linspace(0,2*np.pi,1000)
for deg in degrees:
    coeffs=np.polyfit(x,y,deg)
    y_fit=np.polyval(coeffs,x_plot)
    plt.plot(x_plot,y_fit,label=f'degree {deg}')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynomial Fits of Various Degrees')
plt.show()
