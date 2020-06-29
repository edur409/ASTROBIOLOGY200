# The curl of a vector field

The curl of a vector field ($\vec v$) is also known as the rotor or rotational of the field.  Mathematically, it is expressed as $\nabla \times \vec{v}$.  Where the operator $\nabla \times$ acts on the vector field $\vec v$.  It is a measured of the vorticity of a vector field.

#Python Toolboxes needed
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #For 3D plots
from matplotlib import cm
#enable Latex syntax in matplotlib
from matplotlib import rc
%matplotlib notebook 

The vectorial field (${\bf \vec P}$) has the following form:

$${\bf \hat P} = e^{-(x^2+y^2)}{\bf \hat x} + sin(xy) {\bf \hat y} $$

where $\hat x$ and $\hat y$ are the unit vectors in directions $x$ and $y$ respectively 

#Create a mesh
x = np.arange(-1,1,0.1)
y = np.arange(-1,1,0.1) 
xx,yy=np.meshgrid(x,y)#[xx,yy] = meshgrid(x,y);     

#The parametric equations of the vectorial components
px = np.exp(-(xx**2+yy**2))
py = np.sin(xx*yy)
#The output
plt.figure('Vectorial field')
plt.quiver(xx,yy,px,py,edgecolor='k', facecolor='None',linewidth=0.5)
plt.streamplot(x, y, px, py, color='m', linewidth=1, cmap=plt.cm.inferno,density=2, arrowstyle='->', arrowsize=1.5)
plt.xlabel('x'), plt.ylabel('y');
plt.title(r'Vectorial Field 2-D: ${\bf \hat P} = e^{-(x^2+y^2)}{\bf \hat x} + sin(xy) {\bf \hat y} $')
plt.show()

The curl is a new vector field which is perpendicular to the original local one and its sign is determined by the right-hand rule.

[pxy,pxx]=np.gradient(px,0.1,0.1)#[pxx,pxy]=np.gradient(px,0.1,0.1)
[pyy,pyx]=np.gradient(py,0.1,0.1)#[pyx,pyy]=np.gradient(py,0.1,0.1)
#
curl_p_z=(pyx-pxy);

m,n=curl_p_z.shape
curl_p_x=np.zeros((m,n))
curl_p_y=np.zeros((m,n))

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.quiver(xx,yy,np.zeros((m,n)),curl_p_x,curl_p_y,curl_p_z,3,'r',length=0.03,normalize=False)
ax.plot_surface(xx,yy,np.zeros((m,n)))#surf(xx,yy,zeros(m,n));shading flat;colormap pink;
#rotate3d;
ax.set_xlabel('x'),ax.set_ylabel('y'),ax.set_zlabel('z')
plt.show()

In this next plot we can see the magnitude of the vectors as a coloured image.  Notice where the curl reaches its maximum and minimum values. 

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(xx, yy,curl_p_z , cmap=cm.rainbow ,linewidth=0, antialiased=False,shade=True)
ax.view_init(azim=0, elev=90)
ax.set_xlabel('x'), ax.set_ylabel('y'), ax.set_zlabel(r'$|\nabla \times {\bf \vec P}|$');

from IPython.display import HTML

HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/rB83DpBJQsE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
