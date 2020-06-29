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

# Small Angle Approximation Interactive

This interactive can be used to explore the relationship between an object's size, its distance, and its observed angular size.  When an object is far away compared to its size, astronomers use the *small angle approximation* to simplify the relationship.

There are two control sliders: the first for the size of the object (s) and the second for the distance from Earth to the object (d). The interactive uses both the "exact" equation and small angle approximation to estimate the angular size of the object:

$$\theta_{exact} = 2\arctan\left(\frac{s}{2d}\right) \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \theta_{approx} = \frac{s}{d}$$

**Note**: The above espressions give the angle $\theta$ in radians. To get an angle in degrees, we must multiply by the conversion factor $\frac{180^{\circ}}{\pi}$ (because there are $2\pi$ radians or $360^{\circ}$ in a circle).

# Originally created on June 13, 2018 by Samuel Holen

import ipywidgets as widgets
import numpy as np
import bqplot.pyplot as bq
from IPython.display import display

def approx_theta(s,d):
    # Small angle approximation equation
    return s/d

def exact_theta(s,d):
    # Exact equation for theta
    return 2*np.arctan(s/(2*d))

def circle(r,d=0.):
    # Creates a circle given a radius r and displacement along the 
    # x-axis d 
    theta = np.linspace(0,2*np.pi,1000)
    return (r*np.cos(theta)+d,r*np.sin(theta))

def par_circ(r,theta0,theta1,d=0.,h=0.):
    theta = np.linspace(theta0,theta1,1000)
    return (r*np.cos(theta)+d,r*np.sin(theta)+h)

def ellipse(a,b,d=0.):
    # Creates an ellipse centered at (d,0) with a semimajor axis of 'a'
    # in the x direction and 'b' in the y direction
    theta = np.linspace(0,2*np.pi,1000)
    return (a*np.cos(theta)+d,b*np.sin(theta))

def update(change=None):
    # Update the display.
    D1.y = [0,h_slider.value/2]
    D2.y = [0,-h_slider.value/2]
    D1.x = [0,d_slider.value]
    D2.x = [0,d_slider.value]
    ref.x = [0,d_slider.value]
    # Note that the ellipse is used so that the display needn't be a square.
    X_new, Y_new = circle(h_slider.value/2, d_slider.value)
    Object.x = X_new
    Object.y = Y_new
    
    # Update the resulting angles
    theta_approx = 180/np.pi*approx_theta(h_slider.value,d_slider.value)
    theta_exact = 180/np.pi*exact_theta(h_slider.value,d_slider.value)
    
    approx_eqn.value='<p><b>"Small Angle"  Equation:</b> <br/> {:.5f}&deg; = (180&deg;/&pi;) * ({} / {})</p>'.format(theta_approx,h_slider.value,d_slider.value)
    exact_eqn.value ='<p><b>"Exact" Equation:</b> <br/> {:.5f}&deg; = 2 arctan( {} / 2*{} )</p>'.format(theta_exact,h_slider.value,d_slider.value)    
    difference_eqn.value='<p><b>Difference:</b> <br/> {:.5f}&deg; ({:.2f}%)</p>'.format(abs(theta_exact-theta_approx), 100*(abs(theta_exact-theta_approx)/theta_exact))
    
    arc_loc = (d_slider.value - h_slider.value/2)/3
    angle_loc = exact_theta(h_slider.value,d_slider.value)/2
    xc,yc = par_circ(r=arc_loc, theta0=2*np.pi-angle_loc, theta1=2*np.pi+angle_loc)

    angle_ex.x = xc
    angle_ex.y = yc

h_slider = widgets.FloatSlider(
    value=5,
    min=0.1,
    max=30.05,
    step=0.1,
    disabled=False,
    continuous_update=True,
    orientation='horizontal',
    readout=True,
    readout_format='.2f',
)
d_slider = widgets.FloatSlider(
    value=50,
    min=20.,
    max=100,
    step=0.1,
    disabled=False,
    continuous_update=True,
    orientation='horizontal',
    readout=True
)

theta_approx = 180/np.pi*approx_theta(h_slider.value,d_slider.value)
theta_exact = 180/np.pi*exact_theta(h_slider.value,d_slider.value)

# Create labels for sliders
h_label = widgets.Label(value='Size of star (s)')
d_label = widgets.Label(value='Distance to star (d)')

# Create text display
approx_eqn = widgets.HTML(value='<p><b>"Small Angle" Equation:</b> <br/> {:.5f}&deg; = (180&deg;/&pi;) * ({} / {})</p>'.format(theta_approx,h_slider.value,d_slider.value))
exact_eqn = widgets.HTML(value='<p><b>"Exact" Equation:</b> <br/> {:.5f}&deg; = 2 arctan( {} / 2*{} )</p>'.format(theta_exact,h_slider.value,d_slider.value))
difference_eqn = widgets.HTML(value='<p><b>Difference:</b> <br/> {:.5f}&deg; ({:.2f}%)</p>'.format(abs(theta_exact-theta_approx), 100*(abs(theta_exact-theta_approx)/theta_exact)))
                             
blank = widgets.Label(value='')



## PLOT/FIGURE ##

# Sets axis scale for x and y to 
sc_x = bq.LinearScale(min=-5,max=115)
sc_y = bq.LinearScale(min=-26,max=26)

# Get the range to work with
x_range = sc_x.max - sc_x.min
y_range = sc_y.max - sc_y.min

# Initial height and distance of star
init_h = h_slider.value
init_d = d_slider.value

# Note that the ellipse is used so that the display needn't be a square.
# Creates a circular 'star'
X,Y = circle(r=init_h/2, d=init_d)

# Sets up the axes, grid-lines are set to black so that they blend in with the background.
ax_x = bq.Axis(scale=sc_x, grid_color='white', num_ticks=0)
ax_y = bq.Axis(scale=sc_y, orientation='vertical', grid_color='white', num_ticks=0)

# Draws the lines to the top and bottom of the star respectively
D1 = bq.Lines(x=[0,init_d], y=[0,init_h/2], scales={'x': sc_x, 'y': sc_y}, colors=['white'])
D2 = bq.Lines(x=[0,init_d], y=[0,-init_h/2], scales={'x': sc_x, 'y': sc_y}, colors=['white'])

# Creates the star
Object = bq.Lines(scales={'x': sc_x, 'y': sc_y}, x=X, y=Y, colors=['blue'], 
                  fill='inside', fill_colors=['blue'])

# Creates a reference line.
ref = bq.Lines(x=[0,init_d], y=[0,0], scales={'x': sc_x, 'y': sc_y}, colors=['white'], line_style='dashed')

arc_loc = (init_d - init_h/2)/3
angle_loc = exact_theta(init_h,init_d)/2
xc,yc = par_circ(r=arc_loc, theta0=2*np.pi-angle_loc, theta1=2*np.pi+angle_loc)

angle_ex = bq.Lines(x=xc, y=yc, scales={'x': sc_x, 'y': sc_y}, colors=['white'])

angle_label = bq.Label(x=[2], y=[0], scales={'x': sc_x, 'y': sc_y},
                   text=[r'$$\theta$$'], default_size=15, font_weight='bolder',
                   colors=['white'], update_on_move=False)

# Update the the plot/display
h_slider.observe(update, names=['value'])
d_slider.observe(update, names=['value'])

# Creates the figure. The background color is set to black so that it looks like 'space.' Also,
# removes the default y padding.
fig = bq.Figure(title='Small Angle Approximation', marks=[Object,D1,D2,angle_ex], axes=[ax_x, ax_y], 
                padding_x=0, padding_y=0, animation=100, background_style={'fill' : 'black'})

# Display to the screen

# Set up the figure
fig_width = 750
fig.layout.width = '{:.0f}px'.format(fig_width)
fig.layout.height = '{:.0f}px'.format(fig_width/2)

# Set up the bottom part containing the controls and display of equations
h_box = widgets.VBox([h_label, h_slider])
d_box = widgets.VBox([d_label, d_slider])
slide_box = widgets.HBox([h_box, d_box])
h_box.layout.width = '{:.0f}px'.format(fig_width/2)
d_box.layout.width = '{:.0f}px'.format(fig_width/2)

eqn_box = widgets.HBox([exact_eqn, approx_eqn, difference_eqn])
exact_eqn.layout.width = '{:.0f}px'.format(fig_width/3)
approx_eqn.layout.width = '{:.0f}px'.format(fig_width/3)
difference_eqn.layout.width = '{:.0f}px'.format(fig_width/3)

BOX = widgets.VBox([fig, slide_box, eqn_box])
display(BOX)


