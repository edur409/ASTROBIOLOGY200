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

# Life in the Universe
<a id="top-title"></a>

[Jupyter notebook](https://jupyter4edu.github.io/jupyter-edu-book/) based on the exercises of the book *Life in the Universe (2011)* by Jeffrey Bennett and Seth Shostak.  The book is a candidate for the syllabus considered for the **ASTRO200** course at The University of Auckland. The following problems or guided exercises belong to the quantitative part of the book they called *Cosmic Calculations*.  These exercises cover in my opinion four main subjects related to astrophysics and astrobiology:

-  Gravity and Newton's laws of motion (Planetary orbits, tidal forces, rocket launching, etc).
-  Light (EM radiation to be precise) and how we use it to find information about the universe (distances, chemical composition, masses of distant objects, interstellar communication with intelligent life, etc).
- Radioactive decay (for explaining heat in planetary bodies and the passage of geological time).
- Exponential growth (bacterial growth).

The exercises below can definitely be inscribed within any of those four broad categories.  The objective of showing the calculations is understanding the scientific motivations behind them while providing the mathematical and physical principles we use to improve our knowledge of the known universe and more importantly: what we still don't know.

## The Main Goal:

Inspire students through astrobiology by showing the relevance of the content in a practical way that introduces them to the usefulness and fun of scientific inquiry.


## Te Ao Mārama (Centre for Fundamental Inquiry)

If you want to know more about all the branches of science comitted to life in the universe at The University of Auckland, please visit: [Te Ao Mārama](https://www.teaomarama.auckland.ac.nz/).  A [Kiwi approach](https://www.youtube.com/channel/UCZb4b5bo6e8aA1aPLZ6kOvA) to the collaboration between science and philosophy. It includes the Maori worldview (Weltanschauung) and its interesting cultural ramifications into what is possible and impossible from the point of view of its ancestral heritage. 

### Core values of Te Ao Mārama:
-  Cross-disciplinary collaboration.
-  Clarity in our communication.
-  Respectful and open dialogue.

## About ASTRO200

24 lectures to introduce Astrobiology and its key concepts.  The course requires a minimum of high school level to be taken and past satisfactorily.  Please never be afraid to ask questions.  Whenever possible we will try to give you an answer, and more importantly, its scientific historical development so you don't feel lonely in that sense of discovery that triggered your question in the first place. We are here to teach you what's known to the present and inspire you to look for the unanswered questions or, if posible, to ask those questions nobody has yet dare to ask. 

## The Quest(ion) of Science

The quest to know more is intrinsically human.  In today's world there are so many things humanity already knows that catching up to current knowledge is a huge task, sometimes overwhelming.  But catching up to that knowledge is like climbing a ladder to see farther into the unknown, and, although strenuous at times, it can be fun and incredibly rewarding.  Here we will teach you, within our capabilities, how we know what we know.

## General Advice

Remember that you should always try to answer questions qualitatively before you begin plugging numbers into a calculator. For example, make an order of magnitude estimate of what your answer should be so that you’ll know your calculation is on the right track, and be sure that your answer makes sense and has the appropriate units.

The contents are:

1. [Cosmic Calculations 2.1: Kepler’s Third Law](#CC-2.1)  

2. [Cosmic Calculations 3.1: How Far Is a Light-Year?](#CC-3.1) 

3. [Cosmic Calculations 4.1: Radiometric Dating](#CC-4.1)

4. [Cosmic Calculations 5.1: The Dominant Form of Life on Earth ](#CC-5.1)

5. [Cosmic Calculations 6.1: Bacteria in a Bottle I: Lessons for Early Life](#CC-6.1)

6. [Cosmic Calculations 6.2: Bacteria in a Bottle II: Lessons for the Human Race](#CC-6.2) 

7. [Cosmic Calculations 7.1: Newton’s Version of Kepler’s Third Law](#CC-7.1) 

8. [Cosmic Calculations 8.1: The Surface Area–to–Volume Ratio](#CC-8.1) 

9. [Cosmic Calculations 9.1: The Strength of the Tidal Force](#CC-9.1) 

10. [Cosmic Calculations 10.1: Chances of Being in the Zone](#CC-10.1)

11. [Cosmic Calculations 11.1: Finding orbital Distances for Extrasolar Planets](#CC-11.1)

12. [Cosmic Calculations 11.2: Finding Masses of Extrasolar Planets](#CC-11.2)

13. [Cosmic Calculations 11.3: Finding Sizes of Extrasolar Planets](#CC-11.3)

14. [Cosmic Calculations 12.1: The Distance Between Signaling Societies](#CC-12.1)

15. [Cosmic Calculations 12.2: Sensitivity of SETI Searches](#CC-12.2) 

16. [Cosmic Calculations 13.1: The Rocket Equation ](#CC-13.1)

17. [Cosmic Calculations 13.2: Time Dilation ](#CC-13.2) 


<a id="CC-2.1"></a>
## Cosmic Calculations 2.1: Kepler’s Third Law

First, let's review the three laws discovered by Kepler from the careful measurements of [Tycho Brache](https://physicsworld.com/a/kepler-and-tycho-brahe-the-odd-couple/).  This is one of the most ineteresting stories of scientific collaboration that transformed years of observations into laws about the universe.  I recommend to read/watch [***The Character of Physical Law***](https://www.youtube.com/watch?v=j3mhkYbznBk) by Richard Feynman if you want to indulge in the details.

<p><a href="https://commons.wikimedia.org/wiki/File:Tycho-Kepler-Statue-Prague.jpg#/media/File:Tycho-Kepler-Statue-Prague.jpg"><img src="https://upload.wikimedia.org/wikipedia/commons/7/73/Tycho-Kepler-Statue-Prague.jpg" alt="Tycho-Kepler-Statue-Prague.jpg" width="360" height="480"></a><br>By <a href="https://en.wikipedia.org/wiki/hu:User:Both_El%C5%91d" class="extiw" title="w:hu:User:Both Előd">Both Előd</a> at <a href="https://en.wikipedia.org/wiki/hu:" class="extiw" title="w:hu:">Hungarian Wikipedia</a>, <a href="https://creativecommons.org/licenses/by-sa/2.5" title="Creative Commons Attribution-Share Alike 2.5">CC BY-SA 2.5</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=47229075">Link</a></p>

### Kepler's laws:

***1. The orbit of every planet is an ellipse with the Sun at one of the two foci.***

In the figure below, you can imagine the yellow dot as the sun, and a planet would be moving on the blue curve a certain distance away from it.  The elliptical orbit can be described by the semi-major and semi-minor axes, which define the eccentricity of the orbit.  


Look for the *perihelion* and *aphelion* of Earth's orbit. From those values, what's the flattening of Earth's orbit and its eccentricity?

import numpy as np
import matplotlib.pyplot as plt
#from __future__ import print_function
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

[Go back to the top of the page](#top-title)

<a id="CC-3.1"></a>
## Cosmic Calculations 3.1: How Far Is a Light-Year? 

One light-year $(ly)$ is deﬁned to be the distance that light can travel in 1 year. This distance is ﬁxed because light always travels through space at the speed of light, which is 300,000 kilometers per second (186,000 miles per second). It’s easy to calculate the distance represented by a lightyear if you recall that $distance = speed * time$.  For example, if you travel at a speed of 50 kilometers per hour for 2 hours, you will travel 100 kilometers. To ﬁnd the distance represented by 1 light-year, we need to multiply the speed of light by 1 year: 

$$1~ly = speed~of~light*1~yr$$

Because we are given the speed of light in units of kilometers per second but the time as 1 year, we must carry out the multiplication while converting 1 year into seconds.

$$1~ly = 300,000~\frac{km}{s}*1~y*365~\frac{d}{y}*24~\frac{h}{d}*60~\frac{min}{h}*60~\frac{s}{min}= 9,460,000,000,000~km$$

That is, 1 light-year is equivalent to 9.46 trillion kilometers, or almost 10 trillion kilometers. Be sure to note that a lightyear is a unit of distance, not time.

### How do we know how far are distant objects? 

An interesting video on light-years and the distance from stars from [Yuan-Sen Ting](https://www.youtube.com/watch?v=Op3AYaJc0Xw)

[Go back to the top of the page](#top-title)

from IPython.display import HTML

HTML('<center><iframe width="560" height="315" src="https://www.youtube.com/embed/Op3AYaJc0Xw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><center>')


<a id="CC-4.1"></a>
## Cosmic Calculations 4.1: Radiometric Dating 

The amount of a radioactive substance decays by half with each half-life, so we can express the decay process with a simple formula relating the current amount of a radioactive substance in a rock to the original amount: 

$$\frac{current~amount}{original~amount} = \bigg(\frac{1}{2}\bigg)^{t/t_{half}}$$ 

where $t$ is the time since the rock formed and $t_{half}$ is the half-life of the radioactive material. We can solve this equation for $t$ by taking the logarithm of both sides and rearranging the terms: 

$$ t = t_{half}*\frac{log_{10}\big(\frac{current~amount}{original~amount}\big)}{log_{10}\big(\frac{1}{2}\big)}$$

**Example:** You chemically analyze a small sample of a meteorite. Potassium-40 and argon-40 are present in a ratio of approximately 0.85 unit of potassium-40 atoms to 9.15 units of gaseous argon-40 atoms. (The units are unimportant, because only the relative amounts of the parent and daughter materials matter.) How old is the meteorite? 

**Solution:** Because no argon gas could have been present in the meteorite when it formed (see discussion in text), the 9.15 units of argon-40 must originally have been potassium-40 that has decayed with its half-life of 1.25 billion years. The sample must therefore have started with 0.85 + 9.15 = 10 units of potassium-40 (the original amount), of which 0.85 unit remains (the current amount). The formula now reads log 10 a t = 1.25 billion yr *

$$ t = 1.25~billion~yr*\frac{log_{10}\big(\frac{0.85}{10}\big)}{log_{10}\big(\frac{1}{2}\big)} \\
     = 1.25~billion~yr*\bigg(\frac{-1.07}{-0.301}\bigg) \\
     = 4.45~billion~yr$$

This meteorite solidiﬁed about 4.45 billion years ago.

The plot below illustrates the change in number of Parents and Daughters as time changes in multiples of the half-life. 

[Go back to the top of the page](#top-title)

import numpy as np
import matplotlib.pyplot as plt
#from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

def radio_decay(No,t):
    n=10
    th=1.25 #Billions of years
    #No=100
    time=np.linspace(0,n*th,10*n)
    N=No*(0.5)**(time/th)
    #Figure
    fig, ax1 = plt.subplots(figsize=(8,5))
    color = 'tab:blue'
    P=No*(0.5)**(t/th)
    ax1.set_xlabel('Time (billions of years)')
    ax1.set_ylabel('Number of Parents', color=color)
    ax1.plot(time, N,'-', color=color,label='$^{40} K = '+np.str(P)+'$')
    ax1.scatter(t, P,s=100,c=color)
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.legend(loc='best',bbox_to_anchor=(0.5, 0., 0.5, 0.7))
    
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:red'
    D=No-No*(0.5)**(t/th)
    ax2.set_ylabel('Number of Daughters', color=color)  # we already handled the x-label with ax1
    ax2.plot(time, No-N, color=color,label='$^{40} Ar = '+np.str(D)+'$')
    ax2.scatter(t,D,s=100,c=color)
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.legend(loc='best',bbox_to_anchor=(0.5, 0., 0.5, 0.5))
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.grid(True)
    plt.show()
    return

interactive(radio_decay, No = (100,1000,100),t = (0,10*1.25,1.25),continuous_update=False)

<a id="CC-5.1"></a>
## Cosmic Calculations 5.1 The Dominant Form of Life on Earth 

We can use estimation to show that microbes far outweigh human beings on Earth. We ﬁrst estimate the total mass of the approximately 6 billion human beings on Earth. If an average person is 50 kilograms (110 pounds), the total human mass is about

$$ 6~kg * 10^9~persons * 50~\frac{kg}{person} = 3 * 10^{11}~kg$$
 
We next estimate the mass of microbes in the oceans. The density of microbes varies signiﬁcantly with location and depth, but a rough average is *1 billion* ($10^9$) microbes per liter of water. Multiplying this value by the total volume of ocean water (a Web search reveals this to be about $1.4*10^9~km3$) gives us an estimate of the total number of microbes in the ocean: 

$$ Total~microbes \approx 10^9~\frac{microbes}{liter}*(1.4*10^9~km^3)*(10^3\frac{m}{km})^3*(10^3~\frac{liter}{m^3})$$

$$ \approx 10^9~\frac{microbes}{liter}*(1.4*10^9~km^3)*(10^9\frac{m^3}{km^3})*(10^3~\frac{liter}{m^3})$$

$$ \approx 1.4 * 10^{30}~microbes$$


To ﬁnd the total mass of microbes, we next need to know the typical microbe mass. A typical bacterium measures about 1 micrometer on a side, which means it has a volume of about 1 cubic micrometer.

There are 1 million (10^6) micrometers per meter, so the volume of a bacterium is 

$$1~\mu m^3*(10^{-6}~\frac{m}{\mu m})^3 = 10^{-18}~m^3$$

Because life is made mostly of water, we can use the density of water ($1000~kg/m^3$) as the density of a microbe. Multiplying the microbe volume by the density, we estimate that the typical microbe mass is 

$$10^{-18}~m^3 * 10^3~\frac{kg}{m} = 10^{-15}~kg$$


We combine our results to ﬁnd the total mass of microbes in the oceans:

$$total~mass~of~microbes \approx (number~of~microbes) * (mass~per~microbe)$$

$$\approx 1.4 * 10^{30}~microbes * 10{-15}\frac{kg}{microbe}$$
$$\approx 1.4 * 10^{15}~kg$$

We can compare to the mass of human beings by dividing:

$$\frac{total~mass~of~microbes}{total~mass~of~humans}\approx \frac{1.4 * 10^{15}~kg}{3 * 10^{11}~kg}$$

The total mass of microbes in the oceans is roughly 5000 times that of all humans combined.

[Go back to the top of the page](#top-title)

<a id="CC-6.1"></a>
## Cosmic Calculations 6.1 Bacteria in a Bottle I: Lessons for Early Life 

Once the ﬁrst organisms took hold, how quickly could they have spread and evolved? A thought experiment* offers insight into this question. Suppose that you place a single bacterium in a nutrient-ﬁlled bottle at noon, and that this species is capable of replicating by cell division every minute. The original bacterium grows until it divides into two bacteria at 12:01. These two bacteria divide into 4 bacteria at 12:02, which divide into 8 bacteria at 12:03, and so on. Then the number of bacteria in the bottle at any time t minutes after noon is 


$$number~of~bacteria~at~t~minutes~after~12:00 = 2^t$$ 

We’ll explore general characteristics of this **exponential growth** (t is in the exponent) in *Cosmic Calculations 6.2*. Here, to understand how rapidly early life could have spread, let’s consider the volume of a bacterial colony. A typical bacterium is $10^{-7}~m$ (0.1 micrometer) across, which means it has a volume of about $(10^{-7}m)^3 = 10^{-21}~m^3$. So the volume of bacteria at any time $t$ minutes after noon is 

$$bacterial~volume = 2^t * 10^{-21}~m^3$$

Our two formulas tell us that after 60 minutes the number of bacteria is $2^{60} \approx 1 * 10^{18}$, or a *million trillion*; their volume is about $2^{60} * 10^{-21}~m^3 \approx 0.001~m^3$, or 1 liter (the volume of a typical bottle). But let’s imagine they could somehow continue to multiply. By the end of the second hour, they would number an astonishing $2^{120} \approx 1.3 * 10^{36}$, and their volume would be $2^{120} * 10^{-21}~m^3 \approx 1.3 * 10^{15}~m^3$  —large enough to cover the surface of the Earth to a depth of about 2 meters (*see Problem 53 at the end of the chapter*). Continuing the calculations, you’d ﬁnd that the bacteria would exceed the total volume of the world’s oceans (about $1.3*10^{18}~m3$) at $t = 130~minutes$. Note that changing the doubling time from one minute to a year hardly matters; a time of $t = 130~years$ rather than $130~minutes$ is still geologically insigniﬁcant. Although the bacteria could not really continue this hypothetical growth, the implication should be clear: The ﬁrst self-replicating organisms would have spread rapidly as far as conditions allowed, leaving the door wide open for biological evolution through natural selection.

*This thought experiment is adapted from one created by Professor of Physics Albert A. Bartlett of the University of Colorado.

[Go back to the top of the page](#top-title)

<a id="CC-6.2"></a>
## Cosmic Calculations 6.2 Bacteria in a Bottle II: Lessons for the Human Race 

Recall the thought experiment of the bacteria in a bottle in Cosmic Calculations 6.1, in which we start with a single bacterium at 12:00 that replicates each minute. Suppose that bacterial growth completely ﬁlls the bottle at 1:00, exhausting all nutrients so all the bacteria die. Let’s explore this issue with a series of simple questions. 

*Question 1:* The tragedy occurs when the bottle is full at 1:00, just 60 minutes after the ﬁrst bacterium started the colony at 12:00. When was the bottle half-full? 

*Answer:* Most people guess 12:30, halfway through the hour of growth. But this is incorrect: The bacterial population doubled every minute, so the bottle went from half-full at 12:59 to full at 1:00. 

*Question 2:* You are a mathematically sophisticated bacterium, and at 12:56 you recognize the impending disaster. You warn your fellow bacteria that the end is just four minutes away unless they slow their growth dramatically. Will anyone believe you? 

*Answer:* Because the bottle was full at 1:00, it was $\frac{1}{2}$-full at 12:59, $\frac{1}{4}$-full at 12:58, $\frac{1}{8}$-full at 12:57, and $\frac{1}{16}$-full at 12:56—which means there’s still 15 times as much unused bottle as used bottle when you give your warning. Your warning may go unheeded. 

*Question 3:* Just before the disaster strikes, a bacterial space program discovers 3 more bottles in the lab. With an immediate and massive population redistribution program among the original and 3 new bottles, how much more time will the bacteria buy?

*Answer:* You may be tempted to think that 3 more bottles should give the colony 3 more hours, but in fact it gives them only 2 more minutes: Because the growth occurs through doubling, the colony will ﬁll 2 bottles at 1:01 and 4 bottles at 1:02. In fact, nothing could allow the growth to continue much longer, because the doublings would soon lead the bacteria to impossible volumes (see Problem 54 at the end of the chapter).

We can draw several general conclusions. First, because populations of living organisms tend to grow exponentially, numbers can rise very rapidly. This explains the inevitable population pressure that helped Darwin realize the role of natural selection (see Fact 1 on p. 157). Second, exponential growth must always be a short-term, temporary phenomenon; for living organisms, the growth typically stops because of predation or a lack of sufﬁcient nutrients or energy. Third, these laws about growth apply to all species—our intelligence cannot make us immune to simple mathematical laws. This is a critical lesson, because human population has been growing exponentially for the past few centuries (see Figure 13.14). Of course, our intelligence gives us one option not available to bacteria. Exponential growth can stop only through some combination of an increase in the death rate and a decrease in the birth rate. Unlike bacteria, we can choose to stop our exponential growth with changes to our birth rate before we “ﬁll” our planet.

[Go back to the top of the page](#top-title)

<a id="CC-7.1"></a>
## Cosmic Calculations 7.1: Newton’s Version of Kepler’s Third Law 

How do we know the masses of distant objects? In many cases, we can use a modiﬁed version of Kepler’s third law $p^2 = a^3$. Recall that this law applies only to objects orbiting the Sun (see [Cosmic Calculations 2.1](#CC-2.1)). However, Newton found that Kepler’s original law was just a speciﬁc case of a more general law, usually called Newton’s version of Kepler’s third law: 

$$p^2 = \frac{4\pi^2}{G~(M_1 + M_2)}a^3  $$

where $M_1$ and $M_2$ are the masses of the two objects, $p$ is their orbital period, and $a$ is the distance between their centers. The term $4\pi^2$ is simply a number ($4\pi^2 \approx 4~X~3.14^2 \approx 39.44$), and $G = 6.67 * 10-11 \frac{m^3}{kg * s^2}$ is the gravitational constant. This law gives us the power to measure the masses of distant objects. Any time we measure an orbiting object’s period ($p$) and orbital distance ($a$), Newton’s equation allows us to calculate the sum $M_1 + M_2$ of the two objects involved in the orbit. If one object is much more massive than the other, we essentially learn the mass of the massive object, as the following example shows. 

**Example:** Use the fact that Earth orbits the Sun in 1 year at an average distance of 150 million kilometers (1 AU) to calculate the mass of the Sun. 

**Solution:** Newton’s version of Kepler’s third law becomes

$$p_{Earth}^2 = \frac{4\pi^2}{G~(M_{Sun} + M_{Earth})}a_{Earth}^3  $$

Because the Sun is much more massive than Earth, the sum of their masses is nearly the mass of the Sun alone: $M_{Sun} + M_{Earth} \approx M_{Sun}$. Using this approximation, we ﬁnd $p_{Earth}^2$:

$$p_{Earth}^2 \approx \frac{4\pi^2 a_{Earth}^3}{G~M_{Sun}}  $$

To ﬁnd an expression for the mass of the Sun, we multiply both sides by $M_{Sun}$ and divide both sides by $p_{Earth}^2$:

$$ M_{Sun} \approx  \frac{4\pi^2 a_{Earth}^3}{G~p_{Earth}^2} $$

Because $G$ is given above with units of seconds and meters, we must use the same units for Earth’s orbital period ($p_{Earth} = 1~year \approx 3.15 * 10^7~s^2$) and average orbital distance ($a_{Earth} = 1 AU \approx 1.5 * 10^11~m^2$). We ﬁnd 

$$ M_{Sun} \approx  \frac{4\pi^2 (1.5~x~10^{11}~m)^3}{(6.67~\frac{m^3}{kg * s^2})~(3.15~x~10^7~s)^2} = 2.0~x~10^{30}~kg $$


Simply by substituting in Earth’s orbital period and distance from the Sun and the gravitational constant $G$, we have used Newton’s version of Kepler’s third law to ﬁnd that the Sun’s mass is about $2 * 10^{30}$ kilograms.

[Go back to the top of the page](#top-title)

<a id="CC-8.1"></a>
## Cosmic Calculations 8.1 The Surface Area–to–Volume Ratio 

The total amount of heat contained in Mars or any other planet depends on the planet’s volume, but this heat can escape to space only from the planet’s surface. As heat escapes, more heat ﬂows upward from the interior to replace it, until the interior is no hotter than the surface. Thus, the time it takes for a planet to lose its internal heat is related to the ratio of the surface area through which it loses heat to the volume that contains heat: surface area volume

$$surface~area–to–volume~ratio = \frac{surface~area}{volume}$$


A spherical planet (radius $r$) has surface area $4\pi r^2$ and volume $\frac{4}{3} \pi r^3$, so the ratio becomes

$$surface~area–to–volume~ratio = \frac{4\pi r^2}{\frac{4}{3} \pi r^3} = \frac{3}{r}$$ 

Because $r$ appears in the denominator, we conclude that larger objects have smaller surface area–to–volume ratios. (Although we’ve considered a sphere, this idea holds for objects of any shape.) 

**Example:** Compare the surface area–to–volume ratios of the Moon and Earth. 

**Solution:** Dividing the surface area–to–volume ratios for the Moon and Earth, we ﬁnd 

$$\frac{surface~area–to–volume~ratio~(Moon)}{surface~area–to–volume~ratio~(Earth)} =\frac{\frac{3}{r_{Moon}}}{\frac{3}{r_{Earth}}} = \frac{r_{Earth}}{r_{Moon}}$$ 

The radii of the Moon and Earth are $r_{Moon} = 1738~km$ and $r_{Earth} = 6378~km$: 

$$\frac{surface~area–to–volume~ratio~(Moon)}{surface~area–to–volume~ratio~(Earth)} = \frac{6378~km}{1738~km} = 3.7$$

The Moon’s surface area–to–volume ratio is nearly four times as large as Earth’s, which means the Moon would cool four times faster if all else were equal. In fact, Earth has retained heat much longer, because its larger size gave it more heat to begin with and because Earth has a higher proportion of radioactive elements. (**See Problem 53 for a similar analysis of Mars.**)

### Something must be added here about the heat flow from the InSight Mars Mission (The Mole)

[Go back to the top of the page](#top-title)

<a id="CC-9.1"></a>
## Cosmic Calculations 9.1 The Strength of the Tidal Force 

Recall that the force of gravity acting between two objects is 

$$F_g = G\frac{M_1 M_2}{ d^2}$$

The tidal force that a planet exerts on a satellite is the difference between the gravitational force on the near and far sides of that satellite. One way to get a sense of this difference is to consider a “test mass”—say, a 1-kg rock—on the satellite’s surface. If $d$ is the distance between the center of the planet and the center of a satellite of radius $r_{sat}$, then on the near side of the satellite the distance from the planet’s center to the 1-kg rock is $d - r_{sat}$ and on the far side it is $d + r_{sat}$. We then calculate the gravitational force in both positions and subtract to get the tidal force acting on the satellite per kilogram of mass.

**Example:** Calculate the tidal force that Earth exerts on the Moon (per kilogram) and compare to the effect of the Moon’s own gravity. Useful data: $M_{Earth} = 5.97 * 10^{24}~kg$, $r_{Moon} = 1.74 * 10^6~m$, the Earth–Moon distance is $d = 3.84 * 10^8~m$, and $M_{Moon} = 7.35 * 10^{22}~kg$. As long as you use $G$ in standard units and the masses and distances in kilograms and meters, your answer will come out in newtons ($1~N \approx  1 kg * m/s^2 \approx 0.225~lb$).

**Solution:** We ﬁnd the tidal force $F_{tidal}$ that Earth exerts on the rock by subtracting the gravitational force $F_g$ when the rock is on the far side of the Moon (where the rock’s gravitational attraction to Earth is weaker) from the gravitational force when it is on the near side (where the gravitational attraction is stronger): 

$$F_{tidal} = F_g(on~near~side) - F_g(on~far~side)$$

Let’s ﬁrst consider the near-side term: 

$$F_g(near~side) = G \frac{M_{Earth} M_{rock}}{(d_{Earth-Moon} - r_{Moon})^2} $$

$$= ( 6.67 * 10^{-11}~\frac{m^3}{kg * s^2})*(\frac{(5.97 * 10^{24}~kg)*(1~kg)}{(3.84 * 10^8~m - 1.74 * 10^6~m)^2}) $$

$$ = 0.00273~N$$

For the far-side term, we find

$$F_g(far~side) = G \frac{M_{Earth} M_{rock}}{(d_{Earth-Moon} + r_{Moon})^2} $$

$$= ( 6.67 * 10^{-11}~\frac{m^3}{kg * s^2})*(\frac{(5.97 * 10^{24}~kg)*(1~kg)}{(3.84 * 10^8~m + 1.74 * 10^6~m)^2}) $$

$$ = 0.00267~N$$

The difference gives us the tidal force (per kilogram): 

$$F_{tidal} = F_g(on~near~side) - F_g(on~far~side) = 0.00273~N - 0.00267~N = 0.00006~N$$ 

For comparison, the Moon’s gravitational force acting on the rock is 

$$F_g = G \frac{M_{Moon} M_{rock}}{r_{Moon}^2}$$

$$ = (6.67 * 10^{-11}~\frac{m^3}{kg * s^2})*(\frac{(7.35 * 10^{22}~kg)*(1~kg)}{(1.74 * 10^6~m)^2}) $$

$$= 1.6 N$$

Note that this $1.6~N$ gravitational force (which is the weight of the rock on the Moon and is equivalent to $1.6~N * 0.225~lb/N = 0.36~pound$) is more than 15,000 times greater than the $0.00006~N$ tidal force that Earth exerts on the rock. Clearly, the tidal force is quite small in comparison to the gravitational force, though over time it has been large enough to bring the Moon into synchronous rotation. (The tidal force was stronger when the Moon was closer to Earth.)

### Write something here about how Jupiter gravitationally squeezes its moons 

[Go back to the top of the page](#top-title)

<a id="CC-10.1"></a>
## Cosmic Calculations 10.1 Chances of Being in the Zone 

If all other factors are equal, the likelihood of ﬁnding planets in a star’s habitable zone depends on the width of the zone. 

**Example:** The Sun’s habitable zone is (optimistically) calculated to extend from about $0.84$ to $1.7~AU$. Consider a smaller star (of spectral type M [Section 11.1]), in which the habitable zone extends only from $0.05$ to $0.1~AU$. How does the probability of ﬁnding a habitable planet in this star’s habitable zone compare to the probability around a Sun-like star? Given that these types of small stars outnumber Sun-like stars by approximately eight to one in our galaxy, for which class of stars should we expect more worlds in habitable zones? 

**Solution:** The width (range of radii) of a habitable zone, $R_{HZ}$, is,

$$R_{HZ} = R_{outer} - R_{inner}$$

For a Sun-like star,

$$R_{HZ} = 1.7 - 0.84 = 0.86~AU$$

For the smaller star,

$$R_{HZ} = 0.1 - 0.05 = 0.05~AU$$

For the smaller star, the probability of being in the habitable zone is only $0.05/0.86 = 0.058$ times that for a Sun-like star. However, because these stars are eight times as common, the total number of worlds in habitable zones around these small stars would be about $8 * 0.058 = 0.46$, or $46\%$, as great as for worlds around Sun-like stars. (Of course, we have not considered factors besides the size of the habitable zone that may also be important.)

[Go back to the top of the page](#top-title)

<a id="CC-11.1"></a>
## Cosmic Calculations 11.1 Finding orbital Distances for Extrasolar Planets 

Recall that Newton's version of Kepler's third law reads

$$p^2 = \frac{4\pi^2}{G~(M_1 + M_2)}a^3  $$

In the case of a planet orbiting a star, $p$ is the planet's orbital period, $a$ is its average orbital distance (semimajor axis), $M_1$ and $M_2$ are the masses of the star and planet, respectively, and $G = 6.67 *10^{-11}~\frac{m^3}{Kg*s^2}$ is the gravitational constant.  Because a star is so much more massive than a planet, we can approximate $M_{star}+M_{planet} \approx M_{star}$ (see [Cosmic Calculations 7.1](#CC-7.1)). Using this approximation, we can apply simple algebra to solve for the average orbital distance $a$:

$$a \approx \sqrt[3]{\frac{G M_{star}}{4\pi ^2}p_{planet}^2}$$

**Example:** The star 51 Pegasi has a mass 1.06 times that of our Sun, and Doppler measurements (shown in Figure 11.11b) indicate it has a planet with an orbital period of $4.23~days$.  What is the planet's average orbital distance?

**Solution:** We can use Newton's version of Kepler's third law, but to make the units consistent, we first convert the given stellar mass to kilograms (using the fact that the Sun's mass is $2*10^{30}~kg$) and the orbital period to seconds:

$$M_{star}= 1.06*M_{Sun} = 1.06*(2*10^{30}~kg) = 2.12*10^{30}kg$$

$$p = 4.23~day* \frac{24~hr}{1~day}* \frac{3600~s}{1~hr} = 3.65*10^5~s$$

We now plug these values into our equation from above to find the average distance $a$:

$$a \approx \sqrt[3]{\frac{G M_{star}}{4\pi ^2}p_{planet}^2}$$

$$\approx \sqrt[3]{\frac{6.67*10^{-11}\frac{m^3}{kg*s^2}*2.12*10^{30}~kg}{4\pi^2}*(3.65*10^5~s)^2}$$

$$\approx 7.81*10^9~m$$

The planet orbits 51 Pegasi ata an average distance of 7.8 billion meters, 7.8 million kilometers.  It's easier to interpret this number if we convert it to astronomical units ($1~AU \approx 1.50*10^{11}~m$):

$$a = 7.81*10^9~m*\frac{1~AU}{1.50*10^{11}~m} = 0.052~AU$$

The planet's average orbital distance is 0.052 AU --small even compared to that of Mercury, which orbits our Sun at 0.39 AU.  In fact, comparing the planet's 7.8-million-kilometer distance to the size of the star itself (presumably close to the 700,000-kilometer radius of our Sun), we estimate that the planet orbits its star at a distance only a little more than 10 times the star's radius.

[Go back to the top of the page](#top-title)

<a id="CC-11.2"></a>
## Cosmic Calculations 11.2 Finding Masses of Extrasolar Planets 

An object’s momentum is deﬁned as its mass $m$ times its velocity $v$; like angular momentum [Section 3.4], momentum must be conserved. Consider a star with a single planet. Because the center of mass remains stationary between them (see Figure 11.7), the system has no momentum relative to this center of mass. The star’s momentum ($m_{star} * v_{star}$) must therefore be equal in magnitude (but opposite in direction) to the planet’s momentum ($m_{planet} * v_{planet}$): 

$$m_{star}*v_{star} = m_{planet}*v_{planet}$$

Solving, the planet’s mass is 

$$m_{planet} = \frac{m_{star}*v_{star}}{v_{planet}}$$

We generally know the star’s mass from its spectral type. The Doppler technique can tell us the star’s velocity ($v_{star}$) and the planet’s orbital period $p$; we can use the latter to ﬁnd the planet’s velocity ($v_{planet}$) if we already know its average orbital distance $a_{planet}$ (calculated with the method in [Cosmic Calculations 11.1](#CC-11.1)).  If we assume a circular orbit, the planet travels a distance $2\pi a$ during each orbit that takes time $p$, so its orbital velocity is $2\pi a_{planet}/p_{planet}$.  Substituting this expression for the planet's velocity into the above equation for mass gives:

$$m_{planet} = \frac{m_{star}*v_{star}*p_{planet}}{2\pi*a_{planet}}$$

Remember that with velocity data from the Doppler method, this formula gives us the *minimum* mass of the planet.

**Example:** Estimate the mass of the planet orbiting 51 Pegasi.

**Solution:** From [Cosmic Calculations 11.1](#CC-11.1)), we know the planet's orbital period ($p = 3.65*10^5~s$)and orbital distance ($a = 7.81*10^9~m$) and the star's mass ($M_{star} = 2.12*10^{30}~kg$). The graph in Figure 11.11b shows that the star's velocity is about $v_{star} = 57~m/s$.  We now plug these values into the above formula to find the planet's mass:

$$m_{planet} = \frac{(2.12*10^{30}~kg)*(57~m/s)*(3.65*10^5~s)}{2\pi*(7.81*10^9~m)}$$

$$\approx 9*10^{26}~kg$$

The minimum mass of the planet is about $9*10^{26}$ kilograms, which is about of half of Jupiter's mass and about 150 times the mass of Earth.  The fact that the planet has a Jupiter-like mass but orbits very close to its star (as found in [Cosmic Calculations 11.1](#CC-11.1)), where we expect it to have a very hot surface, makes this planet an example of what astronomers refer to as a *hot Jupiter*.


[Go back to the top of the page](#top-title)

<a id="CC-11.3"></a>
## Cosmic Calculations 11.3 Finding Sizes of Extrasolar Planets 

We determine planet radii from the fraction of a star's light blocked during a transit.  Viewed against the sky, both the star and the planetappear as tiny circular disks.  These disks are far too smallfor our telescopes to resolve, but the fraction of the star's light that is blocked must be equal to the area of the planet's disk ($\pi r_{planet}^2$) divided by the area of the star's disk ($\pi r_{star}^2$).  We generally know the approximate radius of the star (from its spectral type), so the fractional drop in the star's light during a transit is

$$fraction~of~light~blocked = \frac{area~of~planet's~disk}{area~of~star's~disk} = \frac{\pi r_{planet}^2}{\pi r_{star}^2} = \frac{r_{planet}^2}{r_{star}^2}$$

Solving for the planet's radius, we find

$$r_{planet} = r_{star} \sqrt{fraction~of~light~blocked}$$

**Example:** Figure 11.13 shows a transit of the star HD 189733. The star's radius is about 800,000 kilometers ($1.15R_{Sun}$), and the planet blocks $1.7\%$ of the star's light during a transit.  What is the planet's radius? 

**Solution:** We simply plug the star's radius (800,000 km) and the fraction of its light blocked during a transit ($1.7\% = 0.017$) into the above equation:

$$r_{planet} = r_{star} \sqrt{fraction~of~light~blocked}$$
$$r_{planet} = 800,000~km \sqrt{0.017}$$
$$\approx 100,000~km$$

The planet's radius is about 100,000 kilometers, which is about 1.4 times Jupiter's radius of 71,500 kilometers.  That is, the planet is about $40\%$ larger than Jupiter in radius.


[Go back to the top of the page](#top-title)

<a id="CC-12.1"></a>
## Cosmic Calculations 12.1 The Distance Between Signaling Societies 

How far is it to the nearest other world with technologically advanced beings? We don’t know, of course, but if we use the Drake equation to estimate the number of civilizations, we can then compute their average separation. 

We start by estimating the volume $V$ of space available for civilizations in the Milky Way Galaxy, assuming that civilizations are conﬁned to the galaxy’s disk: 

$$V = \pi R^2 * T $$

where $R$ is the disk radius and $T$ is the disk thickness. 

Suppose the Drake equation tells us that there are $N$ technological civilizations in our galaxy. If we assume that these civilizations are spread randomly, then the average volume of space that contains just one civilization must be the total volume of the galaxy divided by the number of civilizations, $V/N$. If we consider this volume per civilization to be a cube in which each side measures $d$ light-years, then $d$ is also the distance from the center of one cube to the center of the next, which means it is the average distance between civilizations.

The volume of a cube with side length $d$ is $d^3$, so $d^3 = V/N$. Solving for $d$, we ﬁnd

$$d = \Big(\frac{V}{N}\Big)^\frac{1}{3} =  \Big(\frac{\pi R^2 * T}{N}\Big)^\frac{1}{3}$$

**Example:** Suppose that N = 10,000. What is the average distance between civilizations? 

**Solution:** The disk of the galaxy has radius R = 50,000 light-years and thickness T = 1000 light-years, so its volume is 

$$V = \pi R^2 * T = \pi * (50,000~ly)^2 * (1000~ly) \approx 8*10^{12}~ly^3 $$

We use this volume to calculate $d$: 

$$d = \Big(\frac{V}{N}\Big)^\frac{1}{3} =  \Big(\frac{8*10^{12}~ly^3}{10,000}\Big)^\frac{1}{3} \approx 900~ly$$

If there are 10,000 civilizations in the disk of our galaxy, the average distance between these civilizations is nearly 1000 light-years.


[Go back to the top of the page](#top-title)

<a id="CC-12.2"></a>
## Cosmic Calculations 12.2 Sensitivity of SETI Searches 

The distance from which a SETI experiment could detect an alien transmission depends on the sensitivity of the receiver and on the strength of the signal. The inverse square law for light [Section 7.1] tells us that if aliens broadcast a signal with power $P$, it will have weakened by a factor $d^2$ by the time it reaches Earth, where $d$ is the distance of the broadcasting civilization. Therefore, the strength $S$ of the signal we receive at Earth is this diminished power $P/d^2$ multiplied by the area of the receiving radio dish, $A_r$, and a constant of proportionality, $k$:

$$S = k * A_r * \frac{P}{d^2} $$

**Example:** A SETI search using the 300-meter-diameter Arecibo radio telescope can pick up a 10-million-watt signal from 1000 light-years away (if the transmitting antenna is also 300 m in diameter). If we were to detect a similar signal coming from 25,000 light-years away, how powerful would the alien transmitter have to be? 

**Solution:** Since all else is held constant in this problem, the only change is that in the second case the transmitter is 25 times farther away than in the ﬁrst case. Thus, for a given transmitted power $P$, the signal strength $S$ will be reduced by a factor of $(\frac{1}{25})^2 = \frac{1}{625} $. To get the same $S$, the transmission power from this star would have to be 625 times stronger, or 625 * 10 million = 6 billion watts.


[Go back to the top of the page](#top-title)

<a id="CC-13.1"></a>
## Cosmic Calculations 13.1 The Rocket Equation 

The rocket equation tells us how a spacecraft’s ﬁnal velocity, $v$, depends on the velocity of the exhaust gas expelled out the back, $v_e$, and the rocket’s *mass ratio*. The mass ratio is $M_i/M_f$, where $M_i$ is the mass of the rocket (including any payload—such as a spacecraft—it is carrying) with all its fuel and $M_f$ is the mass of the rocket after the fuel has been burned (that is, the spacecraft and any still-attached but empty fuel tanks). We can write the rocket equation in the following two equivalent forms: 

$$v = v_e ln(\frac{M_i}{M_f}) \quad \Longleftrightarrow \quad  \frac{M_i}{M_f} = e^{\frac{v}{v_e}}$$


In the equation at left, “ln” is the natural logarithm; your calculator should have a key for computing this. In the equation at right, $e$ represents a special number with value $e \approx 2.718$; your calculator should also have a key for computing $e$ to any power. If you are familiar with the algebra of logarithms, you can conﬁrm that the two equations are equivalent. 

**Example:** Suppose you want a rocket to achieve escape velocity from Earth ($11~km/s$) and its engines produce an exhaust velocity of $3~km/s$. What mass ratio is required? 

**Solution:** We set the rocket’s ﬁnal velocity to $v = 11~km/s$ and its exhaust velocity to $v_e = 3~km/s$, and use the second form of the equation to ﬁnd the mass ratio: 

$$\frac{M_i}{M_f} = e^{\frac{v}{v_e}} = e^{\frac{11~km/s}{3~km/s}} = e^{\frac{11}{3}} \approx 39 $$ 

The required mass ratio is about 39. As discussed in the text, this mass ratio cannot be achieved with a single-stage rocket but can be reached with a multistage rocket.


### What's $e$?

The best explanation of $e$ and its value is shown in the video below (just need to watch until minute 4:00 if you are in a hurry).  The inverse function of $e$, $ln$, or the natural logarithm is important on its own and it is a special case of the logarithmic function using $e$ as its base power.

[Go back to the top of the page](#top-title)

from IPython.display import HTML

HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/-dhHrg-KbJ0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')

<a id="CC-13.2"></a>
## Cosmic Calculations 13.2: Time Dilation 

The effects of time dilation on a fast spaceship can be calculated with a simple formula if we assume that the spaceship travels at constant speed:

$$t_{ship} = t_{Earth} \sqrt{1-\bigg(\frac{v}{c}\bigg)^2}$$

where $t_{ship}$ is the amount of time that passes on the rocket, $t_{Earth}$ is the amount of time that passes on Earth, $v$ is the rocket’s velocity (speed), and $c = 3 * 10^8~m/s$ is the speed of light. 

**Example:** Consider a spaceship that travels round-trip to Vega at 90% of the speed of light. As noted in the text, the round-trip travel time measured by people on Earth is 56 years. How much time passes for passengers on the spaceship? 

**Solution:** Because we are given that the ship travels at 90% of the speed of light, or 0.9c, we know that $v/c = 0.9$. We plug in this value along with the time that passes on Earth, $t_{Earth} = 56~yr$ : 

$$t_{ship} = t_{Earth} \sqrt{1-\bigg(\frac{v}{c}\bigg)^2} \\
           = 56~yr~x~\sqrt{1-0.9^2} \\
           = 56~yr~x~\sqrt{1-0.81}  \\
           = 56~yr~x~\sqrt{0.19}  \\
           = 24.4~yr$$

This is the approximately 24-year round-trip time shown for the ship in **Table 13.1**.

### INCREDIBLE JOURNEYS

In fact, if we could somehow boost our spacecraft to speeds arbitrarily close to the speed of light, we could go anywhere in the universe within a human lifetime. Astronomer Carl Sagan considered a hypothetical rocket that accelerates at a steady 1g (or “1 gee”)—an acceleration that would feel comfortably like gravity on Earth—to the halfway point of its voyage. This constant acceleration would bring the ship closer and closer to the speed of light, though it would never exceed it. (Note that the acceleration of 1g is constant, but the speed is not!) The ship then reverses and decelerates at 1g to its destination. During most of the trip, the ship would be traveling at speeds quite close to the speed of light, so time would pass quite slowly on the ship compared to time on Earth. Longer trips would mean longer periods of acceleration, bringing the ship even closer to the speed of light for most of the journey. 

Calculations show that such a continuously accelerating ship could make a trip to a star 500 light-years away in only about 12 years according to those on board the ship. However, 500 years would pass on Earth. If a crew of 20-year-olds left Earth in the year 2100, they would be merely 32 years old when they reached their destination; but it would be the year 2600 on Earth (actually a bit later, since they would be traveling at not quite the speed of light). 

If they sent a radio message back to Earth, the message would take 500 years to arrive here across the 500-lightyear distance. More than 1000 years after the crew had left, we’d get a message from people who had aged only 12 years since they’d last been seen on Earth. 

#### There's even more: huge gravity fields can slow the ticking of time!!!

One nice scene from [*Interstellar*](https://www.youtube.com/watch?v=lznM-fygfqo).   The planet the crew wants to visit is close to a massive black hole (called *Gargantua* in the movie).  The time in that planet is significantly slower than the one on Earth. 

[Go back to the top of the page](#top-title)




```{toctree}
:hidden:
:titlesonly:


Curl Vector Field <1/Curl_vector_field>
Small angle equation <1/SmallAngleEquation>
```
