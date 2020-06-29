from IPython.display import HTML

HTML('''<script>
code_show=true; 
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show
} 
$( document ).ready(code_toggle);
</script>
The raw code for this IPython notebook is by default hidden for easier reading.
To toggle on/off the raw code, click <a href="javascript:code_toggle()">here</a>.''')

<a id="top-title"></a>
# From Ptolemy to Kepler

Ptolemy, Copernicus, Brahe, Kepler




<a id="CC-2.1"></a>
# Cosmic Calculations 2.1: Kepler’s Third Law

First, let's review the three laws discovered by Kepler from the careful measurements of [Tycho Brache](https://physicsworld.com/a/kepler-and-tycho-brahe-the-odd-couple/).  This is one of the most ineteresting stories of scientific collaboration that transformed years of observations into laws about the universe.  I recommend to read/watch [***The Character of Physical Law***](https://www.youtube.com/watch?v=j3mhkYbznBk) by Richard Feynman if you want to indulge in the details.

<p><a href="https://commons.wikimedia.org/wiki/File:Tycho-Kepler-Statue-Prague.jpg#/media/File:Tycho-Kepler-Statue-Prague.jpg"><img src="https://upload.wikimedia.org/wikipedia/commons/7/73/Tycho-Kepler-Statue-Prague.jpg" alt="Tycho-Kepler-Statue-Prague.jpg" width="360" height="480"></a><br>By <a href="https://en.wikipedia.org/wiki/hu:User:Both_El%C5%91d" class="extiw" title="w:hu:User:Both Előd">Both Előd</a> at <a href="https://en.wikipedia.org/wiki/hu:" class="extiw" title="w:hu:">Hungarian Wikipedia</a>, <a href="https://creativecommons.org/licenses/by-sa/2.5" title="Creative Commons Attribution-Share Alike 2.5">CC BY-SA 2.5</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=47229075">Link</a></p>

## Kepler's laws:

***1. The orbit of every planet is an ellipse with the Sun at one of the two foci.***

In the figure below, you can imagine the yellow dot as the sun, and a planet would be moving on the blue curve a certain distance away from it.  The elliptical orbit can be described by the semi-major and semi-minor axes, which define the eccentricity of the orbit.  


Look for the *perihelion* and *aphelion* of Earth's orbit. From those values, what's the flattening of Earth's orbit and its eccentricity?

import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

# Set default font size for plots:
font = {'size'   : 18}
plt.rc('font',**font)

def elliptic_orbit(a,b,t):
    '''Plot an elliptical orbit and see the radial distance from one focal point
    a= semi-major axis
    b=semi-minor axis
    t=location at an angle between 0 and 360'''
    p=np.linspace(0,2*np.pi,360)
    x = a*np.cos(p)
    y = b*np.sin(p) 
    plt.figure('Ellipse2',figsize=(10,5))
    plt.plot(x,y,'-')
    plt.axis('equal')
    plt.grid(True)
    #t is the angle varying from 0 to 360 degrees
    X = a*np.cos(t*np.pi/180)
    Y = b*np.sin(t*np.pi/180)
    #Conditionals in case of changing length of largest semi-major axis
    if a>=b:
        c=np.sqrt(a**2-b**2)
        plt.scatter(c,0,s=200,c='y')
        plt.scatter(-c, 0, s=200, facecolors='none', edgecolors='y')
        plt.arrow(c, 0, X-c, Y, head_width=0.1, head_length=0.1, fc='red', ec='red')
        plt.scatter(X,Y,s=50,c='b')
        f=(a-b)/a
        e=c/a
        #print('Orbital flattening : ',f)
        print('Orbital eccentricity : ',e)
        #plt.show()
    else:
        c=np.sqrt(b**2-a**2)
        plt.scatter(0,c,s=200,c='y')
        plt.scatter(0, -c, s=200, facecolors='none', edgecolors='y')
        plt.arrow(0, c, X, Y-c, head_width=0.1, head_length=0.1, fc='red', ec='red')
        plt.scatter(X,Y,s=50,c='b')
        f=(b-a)/b
        e=c/b
        #print('Orbital flattening : ',f)
        print('Orbital eccentricity : ',e)
    plt.show()
    return

interactive(elliptic_orbit, a = (0,20,1),b=(0,20,1),t=(0,360,20),continuous_update=False)
        

The reason the orbits are ellipses, and not circles, would not be understood until the arrival of Newton's equations on Gravitation.  

***2. A line joining a planet and the Sun sweeps out equal areas during equal intervals of time.***

<p><a href="https://commons.wikimedia.org/wiki/File:Kepler-second-law.gif#/media/File:Kepler-second-law.gif"><img src="https://upload.wikimedia.org/wikipedia/commons/6/69/Kepler-second-law.gif" alt="Kepler-second-law.gif"></a><br>By <a href="https://en.wikipedia.org/wiki/User:Gonfer" class="extiw" title="en:User:Gonfer">Gonfer</a> (<a href="//commons.wikimedia.org/wiki/User_talk:Gonfer" title="User talk:Gonfer">talk</a>) - <a href="https://en.wikipedia.org/wiki/User:Gonfer" class="extiw" title="en:User:Gonfer">Gonfer</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=24871608">Link</a></p>


When Kepler discovered his third law ($p^2 = a^3$), he knew only that it applied to the orbits of planets about the Sun. In fact, it applies to any orbiting object as long as the following two conditions are met: 

1. The object orbits the Sun or another star of precisely the same mass. 
2. We use units of years for the orbital period and AU for the orbital distance. (Newton extended the law to all orbiting objects; see [Cosmic Calculations 7.1](#CC-7.1).) 

In other words, these two conditions make the relationship a perfect equality.

**Example 1:** The largest asteroid, Ceres, orbits the Sun at an average distance (semimajor axis) of 2.77 AU. What is its orbital period? 

***Solution:*** Both conditions are met, so we solve Kepler’s third law for the orbital period $p$ and substitute the given orbital distance, $a = 2.77~AU$.


$$p^2 = a^3$$

$$ p = \sqrt{a^3} = \sqrt{2.77^3} \approx 4.6~y$$

Ceres has an orbital period of 4.6 years. 

**Example 2:** A planet is discovered orbiting every three months around a star of the same mass as our Sun. What is the planet’s average orbital distance? 

***Solution:*** The ﬁrst condition is met, and we can satisfy the second by converting the orbital period from months to years: $p = 3$ months = 0.25 year. We now solve Kepler’s third law for the average distance a: 

$a = \sqrt[3]{p^2}$

$a = \sqrt[3]{0.25^2} \approx 0.40~AU$

The planet orbits its star at an average distance of $0.40~AU$, which is nearly the same as Mercury’s average distance from the Sun.

These observations offered clear proof that Earth is not the center of everything.* Although we now recognize that Galileo won the day, the story was more complex in his own time, when Catholic Church doctrine still held Earth to be the center of the universe. On June 22, 1633, Galileo was brought before a Church inquisition in Rome and ordered to recant his claim that Earth orbits the Sun. Nearly 70 years old and fearing for his life, Galileo did as ordered and his life was spared. However, legend has it that as he rose from his knees, he whispered under his breath, Eppur si muove— Italian for “And yet it moves.” (Given the likely consequences if Church ofﬁcials had heard him say this, most historians doubt the legend.) The Church did not formally vindicate Galileo until 1992, but the Church had given up the argument long before that. Today, Catholic scientists are at the forefront of much astronomical research, and ofﬁcial Church teachings are compatible not only with Earth’s planetary status but also with the theories of the Big Bang and the subsequent evolution of the cosmos and of life.


<object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" width="750" height="400"><param name="movie" value="KeplerFirstLaw.swf" /><!--[if !IE]>--><object type="application/x-shockwave-flash" data="KeplerFirstLaw.swf" width="750" height="400"><!--<![endif]--><p>flash animation</p><!--[if !IE]>--></object><!--<![endif]--></object>


[Go back to the top of the page](#top-title)

