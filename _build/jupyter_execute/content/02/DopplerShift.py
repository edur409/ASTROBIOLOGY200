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

# Doppler Shift Interactive

This interactive allows you to see how the spectrum of a star is affected by the presense of another object orbiting it, causing the star to move, and therefore for its lines to shift in wavelength.

## Interactive Figure 1: Doppler Shift versus Radial Velocity

This first figure show the spectrum of a hydrogen cloud in space versus the labratory spectrum of hydrogen gas.  The slider on the right hand side lets you adjust the hydrogen cloud's radial veleocity, that is, its speed directly towards, or away from, us.

# Author: Samuel Holen

# Date Created: 11Jun2018
# Last Modified: 14Oct2018 by Juan Cabanela
#
# Hacked on by Andrew Louwagie Gordon to get absorbtion spectrum plotted.

from IPython.display import display
import numpy as np
import bqplot as bq
import ipywidgets as widgets
import tempNcolor as tc
import number_formatting as e2l
import starlib as star
import traitlets

## Set up all the function to use in this interactive

# Tracking where the center of each of the lines is in the spectra_arrays, UPDATE if you redefine the 
# spectra arrays. - jec 10.13.2018
d_idx = 1
g_idx = 4
b_idx = 7
a_idx = 10

def New_Lambda(lamda, vel):
    # Updates the wavelength of the observed spectra using non-relativistic Doppler Shift Equation
    c = 299792458
    # Removed the relativistic and replaced with non-relativistic formula. - jec 10.13.2018
    #return np.sqrt((1+vel/c)/(1-vel/c))*lamda
    return (1+vel/c)*lamda

def simple_update(change=None):
    # updates the display of the observed spectral lines and
    # changes their color accordingly. Also changes the 
    # displayed value of the observed wavelength.
    vel = fig1_vel_slider.value
    new_H_spectra = New_Lambda(H_spectra_array, vel)
    hydrogen_line_moving_simple.x = new_H_spectra
    
     # Update the shift in wavelength for the source
    fig1_dval.value = '{:.3f}'.format(new_H_spectra[d_idx,0] - H_spectra_array[d_idx,0])
    fig1_gval.value = '{:.3f}'.format(new_H_spectra[g_idx,0] - H_spectra_array[g_idx,0])
    fig1_bval.value = '{:.3f}'.format(new_H_spectra[b_idx,0] - H_spectra_array[b_idx,0])
    fig1_aval.value = '{:.3f}'.format(new_H_spectra[a_idx,0] - H_spectra_array[a_idx,0])
    
    # Indicate the direction the source is moving relative to earth
    Vel = e2l.exp2LaTeX(abs(vel/1000),3)[2]
    if vel >= 0:
        vel_label.value = Vel
        direction.value = ' (<b>moving away</b> from us)'
    else:
        vel_label.value = Vel
        direction.value = ' (<b>moving toward</b> us)'

def simple_reset(b):
    # Resets the velocity slider to 0 when the reset button is clicked 
    # Updated to also reset the labels appropriately. - jec 14oct2018
    fig1_vel_slider.value = 0
    direction.value = ''
    
    
def update(change=None):
    # updates the display of the observed spectral lines and
    # changes their color accordingly. Also changes the 
    # displayed value of the observed wavelength.
    t = 6.84
    
    # Update position of stars
    phi = theta_slider.value*3.6  # Assume theta_slider in % fraction of orbit
    phi_step = int(phi)
    bsm.phi = phi

    global r,r2
    # Velocities to determine shifted wavelengths
    if planet_star.value == 'Star':
        bsm.mass1 = mass1a
        bsm.mass2 = mass2a 
        r = 1
        V1 = vel1[phi_step]
        V2 = vel2[phi_step]
        # update the display for the velocity of each star
        vel1_label.value = '{:.0f}'.format(V1)
        vunits1.value = 'km/s'
        ax_x.num_ticks = 12
        ax_x.tick_format = '.1f'
        vel2_label.value = '{:.0f}'.format(V2)
        shift = 0.005
        # Update the star spectral lines
        new_H_spectra = New_Lambda(H_spectra_array,V1*1000)
        new_H_spectra2 = New_Lambda(H_spectra_array,V2*1000)
        star2.default_size = 60
    else:
        bsm.mass1 = mass1b
        bsm.mass2 = mass2b
        r = 0.1
        V1 = vel1[phi_step]
        V2 = vel2[phi_step]
        vel1_label.value = '{:.0f}'.format(V1)
        vunits1.value = 'm/s'
        ax_x.num_ticks = 4
        ax_x.tick_format = '.5f'
        vel2_label.value = '{:.0f}'.format(V2)
        shift = 5e-7
        # Update the star spectral lines
        new_H_spectra = New_Lambda(H_spectra_array,V1)
        new_H_spectra2 = New_Lambda(H_spectra_array,V2*1000)
        star2.default_size = 20
    
    d1 = r*np.cos(np.pi/180 * phi)
    k1 = r*np.sin(np.pi/180 * phi)
    star1.x,star1.y = [d1],[k1]
    d2 = -r2*np.cos(np.pi/180 * phi)
    k2 = -r2*np.sin(np.pi/180 * phi)
    star2.x,star2.y = [d2],[k2]
        
    if picker.value == 'entire spectrum':
        hydrogen_line2.x = new_H_spectra
        hydrogen_line3.x = new_H_spectra2
    elif picker.value == 'violet':
        hydrogen_line2.x = [new_H_spectra[1]-shift,new_H_spectra[d_idx],new_H_spectra[d_idx]+shift]
        hydrogen_line3.x = [new_H_spectra2[1]-shift,new_H_spectra2[d_idx],new_H_spectra2[d_idx]+shift]
    elif picker.value == 'blue':
        hydrogen_line2.x = [new_H_spectra[4]-shift,new_H_spectra[g_idx],new_H_spectra[g_idx]+shift]
        hydrogen_line3.x = [new_H_spectra2[4]-shift,new_H_spectra2[g_idx],new_H_spectra2[g_idx]+shift]
    elif picker.value == 'cyan':
        hydrogen_line2.x = [new_H_spectra[7]-shift,new_H_spectra[b_idx],new_H_spectra[b_idx]+shift]
        hydrogen_line3.x = [new_H_spectra2[7]-shift,new_H_spectra2[b_idx],new_H_spectra2[b_idx]+shift]
    else:
        hydrogen_line2.x = [new_H_spectra[10]-shift,new_H_spectra[a_idx],new_H_spectra[a_idx]+shift]
        hydrogen_line3.x = [new_H_spectra2[10]-shift,new_H_spectra2[a_idx],new_H_spectra2[a_idx]+shift]

    # Update the shift in wavelength for the large (blue) star
    if planet_star.value == 'Star':
        dval1.value = '{:.3f}'.format(new_H_spectra[d_idx,0] - H_spectra_array[d_idx,0])
        gval1.value = '{:.3f}'.format(new_H_spectra[g_idx,0] - H_spectra_array[g_idx,0])
        bval1.value = '{:.3f}'.format(new_H_spectra[b_idx,0] - H_spectra_array[b_idx,0])
        aval1.value = '{:.3f}'.format(new_H_spectra[a_idx,0] - H_spectra_array[a_idx,0])
    else:
        dval1.value = '{:.7f}'.format(new_H_spectra[d_idx,0] - H_spectra_array[d_idx,0])
        gval1.value = '{:.7f}'.format(new_H_spectra[g_idx,0] - H_spectra_array[g_idx,0])
        bval1.value = '{:.7f}'.format(new_H_spectra[b_idx,0] - H_spectra_array[b_idx,0])
        aval1.value = '{:.7f}'.format(new_H_spectra[a_idx,0] - H_spectra_array[a_idx,0])

    # Update the shift in wavelength for the small (red) star
    dval2.value = '{:.3f}'.format(new_H_spectra2[d_idx,0] - H_spectra_array[d_idx,0])
    gval2.value = '{:.3f}'.format(new_H_spectra2[g_idx,0] - H_spectra_array[g_idx,0])
    bval2.value = '{:.3f}'.format(new_H_spectra2[b_idx,0] - H_spectra_array[b_idx,0])
    aval2.value = '{:.3f}'.format(new_H_spectra2[a_idx,0] - H_spectra_array[a_idx,0])

    # Indicate the direction each star is moving relative to earth
    if V1 >= 0:
        direction1.value = 'moving away'
        direction2.value = 'moving toward'
    else:
        direction1.value = 'moving toward'
        direction2.value = 'moving away'

def update_lumen(change=None):
    # Update the luminosity of the small orbiting star. This is for the 
    # simulation going to the limit where the orbiting star is actually a planet.
    if planet_star.value == 'Star':
        if Lumen.value >= 0.5:
            hydrogen_line3.opacities = [Lumen.value-0.5,Lumen.value,Lumen.value-0.5,
                                        Lumen.value-0.5,Lumen.value,Lumen.value-0.5,
                                        Lumen.value-0.5,Lumen.value,Lumen.value-0.5,
                                        Lumen.value-0.5,Lumen.value,Lumen.value-0.5]
        else:
            hydrogen_line3.opacities = [0.01,Lumen.value,0.01,0.01,Lumen.value,0.01,
                                        0.01,Lumen.value,0.01,0.01,Lumen.value,0.01]
    else:
        Lumen.value = 0
        hydrogen_line3.opacities = [0]*12

def update_view(change=None):
    global y_sc,ax_y
    wave = wavelengths.tolist()
    lines_arr = np.array([[410.2,410.2],[410.2,410.2],[410.2,410.2],[434.0,434.0],[434.0,434.0],[434.0,434.0],[486.1,486.1],[486.1,486.1],[486.1,486.1],[656.3,656.3],[656.3,656.3],[656.3,656.3]])
    if planet_star.value == 'Star':
        adjust = np.array([[-0.005,-0.005],[0,0],[0.005,0.005]])
        shift = 0.5
    else:
        adjust = np.array([[-5e-7,-5e-7],[0,0],[5e-7,5e-7]])
        shift = 5e-5
        
    if picker.value == 'entire spectrum':
        x_sc.min = float(min(wavelengths))
        x_sc.max = float(max(wavelengths))
        ax_x.scale = x_sc
        
        # Adjust spectra scales
        hydrogen_line1.scales = {'x': x_sc, 'y': y_sc}
        hydrogen_line2.scales = {'x': x_sc, 'y': y_sc}
        hydrogen_line3.scales = {'x': x_sc, 'y': y_sc}
        wide_line.scales = {'x': x_sc, 'y': y_sc}
        fig.axes = [ax_x,ax_y]
        
        hydrogen_line1.x = H_spectra_array
        hydrogen_line2.x = H_spectra_array
        hydrogen_line3.x = H_spectra_array
        
        wide_line.opacities = [100]*len(wavelengths)

        Lab_label.x=[580,580]
        Lab_label.scales={'x': x_sc, 'y': y_sc}

        fig.background_style = {'fill' : 'white'}
    elif picker.value == 'violet':
        x_sc.min = lines_arr[0,0] - shift
        x_sc.max = lines_arr[0,0] + shift
        ax_x.scale = x_sc
        # Adjust spectra scales
        hydrogen_line1.scales = {'x': x_sc, 'y': y_sc}
        hydrogen_line2.scales = {'x': x_sc, 'y': y_sc}
        hydrogen_line3.scales = {'x': x_sc, 'y': y_sc}
        wide_line.scales = {'x': x_sc, 'y': y_sc}
        
        fig.axes = [ax_x, ax_y]
        fig.background_style = {'fill' : colors_array[wave.index(410)]}
        
        hydrogen_line1.x = lines_arr[0:3] + adjust
        hydrogen_line2.x = lines_arr[0:3] + adjust
        hydrogen_line3.x = lines_arr[0:3] + adjust
        
        wide_line.opacities = [0]*len(wavelengths)
        
        Lab_label.x = [lines_arr[0,0] - shift/2,lines_arr[0,0] - shift/2]
        Lab_label.scales={'x': x_sc, 'y': y_sc}
    elif picker.value == 'blue':
        x_sc.min = lines_arr[3,0] - shift
        x_sc.max = lines_arr[3,0] + shift
        ax_x.scale = x_sc
        # Adjust spectra scales
        hydrogen_line1.scales = {'x': x_sc, 'y': y_sc}
        hydrogen_line2.scales = {'x': x_sc, 'y': y_sc}
        hydrogen_line3.scales = {'x': x_sc, 'y': y_sc}
        wide_line.scales = {'x': x_sc, 'y': y_sc}
        
        fig.axes = [ax_x,ax_y]
        fig.background_style = {'fill' : colors_array[wave.index(432)]}
        
        hydrogen_line1.x = lines_arr[3:6] + adjust
        hydrogen_line2.x = lines_arr[3:6] + adjust
        hydrogen_line3.x = lines_arr[3:6] + adjust
        
        wide_line.opacities = [0]*len(wavelengths)
        
        Lab_label.x = [lines_arr[3,0] - shift/2,lines_arr[3,0] - shift/2]
        Lab_label.scales={'x': x_sc, 'y': y_sc}
    elif picker.value == 'cyan':
        x_sc.min = lines_arr[6,0] - shift
        x_sc.max = lines_arr[6,0] + shift
        ax_x.scale = x_sc
        # Adjust spectra scales
        hydrogen_line1.scales = {'x': x_sc, 'y': y_sc}
        hydrogen_line2.scales = {'x': x_sc, 'y': y_sc}
        hydrogen_line3.scales = {'x': x_sc, 'y': y_sc}
        wide_line.scales = {'x': x_sc, 'y': y_sc}
        
        fig.axes = [ax_x,ax_y]
        fig.background_style = {'fill' : colors_array[wave.index(485)]}
        
        hydrogen_line1.x = lines_arr[6:9] + adjust
        hydrogen_line2.x = lines_arr[6:9] + adjust
        hydrogen_line3.x = lines_arr[6:9] + adjust
        
        wide_line.opacities = [0]*len(wavelengths)
        
        Lab_label.x = [lines_arr[6,0] - shift/2,lines_arr[6,0] - shift/2]
        Lab_label.scales={'x': x_sc, 'y': y_sc}

    else:
        x_sc.min = lines_arr[9,0] - shift
        x_sc.max = lines_arr[9,0] + shift
        ax_x.scale = x_sc
        
        # Adjust spectra scales
        hydrogen_line1.scales = {'x': x_sc, 'y': y_sc}
        hydrogen_line2.scales = {'x': x_sc, 'y': y_sc}
        hydrogen_line3.scales = {'x': x_sc, 'y': y_sc}
        wide_line.scales = {'x': x_sc, 'y': y_sc}
        
        fig.axes = [ax_x,ax_y]
        fig.background_style = {'fill' : colors_array[wave.index(656)]}
        
        hydrogen_line1.x = lines_arr[9:12] + adjust
        hydrogen_line2.x = lines_arr[9:12] + adjust
        hydrogen_line3.x = lines_arr[9:12] + adjust
        
        wide_line.opacities = [0]*len(wavelengths)
        
        Lab_label.x = [lines_arr[9,0] - shift/2,lines_arr[9,0] - shift/2]
        Lab_label.scales={'x': x_sc, 'y': y_sc}
        

# Creates an array of the visible light wavelengths
wavelengths = np.arange(400,700,1)

# Makes an array to plot vertical lines for each of the spectral lines
H_spectra_list = [[409.2,409.2],[410.2,410.2],[411.2,411.2],[433.0,433.0],[434.0,434.0],[435.0,435.0],[485.1,485.1],[486.1,486.1],[487.1,487.1],[655.3,655.3],[656.3,656.3],[657.3,657.3]]

#H_spec_list2
H_spectra_array = np.array(H_spectra_list)

##
## Set up some material for both figures
##

## Set up some widths here
speed_label_width = '300px'
longspeed_label_width = '400px'
vel_value_width = '60px'
longvel_value_width = '150px'
label_width = '240px'
direction_width = '170px'
longdirection_width = '300px'
line_height='35px'
box_width = '450px'
value_width = '100px'

# Creates label widgets to display the observed wavelengths of each
# of the 'shifted' spectral lines. (Both Figures 1 and 2)
shift_label1 = widgets.HTML(value='<b>H&delta; (410.2 nm):</b>')
shift_label2 = widgets.HTML(value='<b>H&gamma; (434.0 nm):</b>')
shift_label3 = widgets.HTML(value='<b>H&beta; (486.1 nm):</b>')
shift_label4 = widgets.HTML(value='<b>H&alpha; (656.3 nm):</b>')
shift_label1.layout.width = label_width
shift_label2.layout.width = label_width
shift_label3.layout.width = label_width
shift_label4.layout.width = label_width

shift_label = widgets.HTML(value='Shift:&nbsp;')
shift_text_width = '50px'
shift_label.layout.width = shift_text_width

units = widgets.Label(value='nm')
unit_text_width = '30px'
units.layout.width = unit_text_width

## Create spectral lines display for both figures
# Axes for spectra
# Set the scales
x_sc_fig1 = bq.LinearScale(min=float(min(wavelengths)), max=float(max(wavelengths)))
y_sc_fig1 = bq.LinearScale()
x_sc = bq.LinearScale(min=float(min(wavelengths)), max=float(max(wavelengths)))
y_sc = bq.LinearScale()

# Define the axes
ax_x_fig1 = bq.Axis(label='Wavelength (nm)', scale=x_sc_fig1, grid_lines='none', num_ticks=12)
ax_y_fig1 = bq.Axis(scale=y_sc_fig1, orientation='vertical', grid_lines='none', num_ticks=0)
ax_x = bq.Axis(label='Wavelength (nm)', scale=x_sc, grid_lines='none', num_ticks=12)
ax_y = bq.Axis(scale=y_sc, orientation='vertical', grid_lines='none', num_ticks=0)

# Arrays for the spectral lines. one for the stars (0.5 to 1) and one for 
# laboratory measurements (0 to 0.5).
height1 = np.array([[0.0,0.5],[0.0,0.5],[0.0,0.5],[0.0,0.5],[0.0,0.5],[0.0,0.5],
                    [0.0,0.5],[0.0,0.5],[0.0,0.5],[0.0,0.5],[0.0,0.5],[0.0,0.5],[0.0,0.5],[0.0,0.5]])
height2 = np.array([[0.5,1.0],[0.5,1.0],[0.5,1.0],[0.5,1.0],[0.5,1.0],[0.5,1.0],
                    [0.5,1.0],[0.5,1.0],[0.5,1.0],[0.5,1.0],[0.5,1.0],[0.5,1.0],[0.5,1.0],[0.5,1.0]])

# This code define the colors to be plotted and 
# which wavelengths they are plotted at, uses hexidecimal designation
colors_array = tc.wav2hex(wavelengths)
colors_list = colors_array.tolist()

# The curve for this figure is created by drawing a bunch of vertical lines that 
# go from zero to the blackbody curve, these 
#     arrays provide the proper pairs of points that define each individual line
x_array = np.array([wavelengths, wavelengths])
fin_x_array = x_array.transpose() # Arrays must be transposed to get pairs of numbers
y_zeros = np.zeros_like(wavelengths)
y_ones = np.ones_like(wavelengths)
y_array = np.array([y_zeros, y_ones])
fin_y_array = y_array.transpose() # Arrays must be transposed to get pairs of numbers

# Create the spectral lines
# Lab Spectra for Figure 1
hydrogen_line_lab_simple = bq.Lines(x=H_spectra_array, y=height1, scales={'x': x_sc_fig1, 'y': y_sc_fig1}, 
                          colors=['black'] ,opacities=[.3,.8,.3,.3,.8,.3,.3,.8,.3,.3,.8,.3])
# Star for Figure 1
hydrogen_line_moving_simple = bq.Lines(x=H_spectra_array, y=height2, scales={'x': x_sc_fig1, 'y': y_sc_fig1}, 
                          colors=['black'] ,opacities=[.3,.8,.3,.3,.8,.3,.3,.8,.3,.3,.8,.3])

# Lab Spectra for Figure 2
hydrogen_line1 = bq.Lines(x=H_spectra_array, y=height1, scales={'x': x_sc, 'y': y_sc}, 
                          colors=['black'] ,opacities=[.3,.8,.3,.3,.8,.3,.3,.8,.3,.3,.8,.3])
# Large star (blue) for Figure 2
hydrogen_line2 = bq.Lines(x=H_spectra_array, y=height2, scales={'x': x_sc, 'y': y_sc}, 
                          colors=['black'] ,opacities=[.3,.8,.3,.3,.8,.3,.3,.8,.3,.3,.8,.3])
# Small star (red) for Figure 2
hydrogen_line3 = bq.Lines(x=H_spectra_array, y=height2, scales={'x': x_sc, 'y': y_sc}, 
                          colors=['#303030'] ,opacities=[.3,.8,.3,.3,.8,.3,.3,.8,.3,.3,.8,.3])

# This is the line command that draws all the lines
fig1_wide_line = bq.Lines(x = fin_x_array, y = fin_y_array, scales={'x': x_sc_fig1, 'y': y_sc_fig1}, colors=colors_list)
wide_line = bq.Lines(x = fin_x_array, y = fin_y_array, scales={'x': x_sc, 'y': y_sc}, colors=colors_list)

# Labels the lab and source spectra on the figure
fig1_Lab_label = bq.Label(x=[580,580], y=[0.1,0.8], scales={'x': x_sc_fig1, 'y': y_sc_fig1},
                   text=['Laboratory Spectrum','Source Spectrum'], default_size=15, font_weight='bolder',
                   colors=['black'], update_on_move=False, align='middle')
Lab_label = bq.Label(x=[580,580], y=[0.1,0.8], scales={'x': x_sc, 'y': y_sc},
                   text=['Laboratory Spectrum','Source Spectrum'], default_size=15, font_weight='bolder',
                   colors=['black'], update_on_move=False, align='middle')


##
## Setup Figure 1
##

# Slider to adjust velocity (away or towards Earth) of the star in question
fig1_vel_slider = widgets.IntSlider(
    value=0,
    min=-5e6,
    max=5e6,
    step=10000,
    disabled=False,
    continuous_update=True,
    orientation='horizontal',
    readout=False,
    layout=widgets.Layout(width='340px')
)
# Reset button
fig1_reset = widgets.Button(description='Reset')

# Figure 1 shifts
fig1_dval = widgets.Text(value=str(0.0))
fig1_gval = widgets.Text(value=str(0.0))
fig1_bval = widgets.Text(value=str(0.0))
fig1_aval = widgets.Text(value=str(0.0))
fig1_dval.layout.width = value_width
fig1_gval.layout.width = value_width
fig1_bval.layout.width = value_width
fig1_aval.layout.width = value_width

# Labels for the velocity slider in Figure 1
speed_label = widgets.HTML(value='<b>Radial Velocity of Source</b>: ')
speed_label.layout.width = longspeed_label_width

vel_label = widgets.HTML(value='0', positioning='right')
vel_label.layout.width = vel_value_width 
vel_label.layout.align_content = 'center'

vunits = widgets.HTML(value='km/s')
vunits.width = unit_text_width

direction = widgets.HTML(value='')
direction.layout.width = longdirection_width

# these boxes contain display commands for the velocity of each star
fig1controls_box = widgets.HBox([speed_label, vel_label, vunits, direction])
fig1controls_box.layout.width = '400px'

# Define Figure 1
figure1 = bq.Figure(title = 'Hydrogen Cloud Absorbtion Spectrum', axes=[ax_x_fig1, ax_y_fig1], animation = 100,
                    marks = [fig1_wide_line, hydrogen_line_lab_simple, hydrogen_line_moving_simple, fig1_Lab_label], 
                    padding_y=0, min_aspect_ratio=2.5, max_aspect_ratio=2.5)
figure1.layout.width = '500px'

# Update the widgets
fig1_vel_slider.observe(simple_update, names=['value'])
fig1_dval.observe(simple_update, names=['value'])
fig1_gval.observe(simple_update, names=['value'])
fig1_bval.observe(simple_update, names=['value'])
fig1_aval.observe(simple_update, names=['value'])
fig1_reset.on_click(simple_reset)

# These boxes contain the labels for the wavelengths and the shift in wavelength
# text boxes.
fig1_shift_label1_box = widgets.HBox([shift_label1, shift_label, fig1_dval, units])
fig1_shift_label2_box = widgets.HBox([shift_label2, shift_label, fig1_gval, units])
fig1_shift_label3_box = widgets.HBox([shift_label3, shift_label, fig1_bval, units])
fig1_shift_label4_box = widgets.HBox([shift_label4, shift_label, fig1_aval, units])
fig1_shift_label1_box.layout.height=line_height
fig1_shift_label2_box.layout.height=line_height
fig1_shift_label3_box.layout.height=line_height
fig1_shift_label4_box.layout.height=line_height
fig1_shift_label1_box.layout.overflow='visible'
fig1_shift_label2_box.layout.overflow='visible'
fig1_shift_label3_box.layout.overflow='visible'
fig1_shift_label4_box.layout.overflow='visible'

# Box to contain all of the above boxes
read_box = widgets.VBox([fig1_shift_label1_box, fig1_shift_label2_box, fig1_shift_label3_box, fig1_shift_label4_box])
fig1_right_side_box = widgets.VBox([fig1_vel_slider, fig1controls_box, fig1_reset, read_box])
#fig1_right_side_box.layout.height = '780px'

# Final box
boxy = widgets.HBox([figure1, fig1_right_side_box])
fig1_right_side_box.layout.width = '500px'
#fig1_right_side_box.layout.height = '300px'

display(boxy)

## Interactive Figure 2: Spectrum of a Moving Stellar System

The following interactive let's you simulate the expected spectrum from 
- a binary star system where both stars have visible hydrogen absorption lines and 
- an exoplanetary system where both objects have hydrogen in their spectra, but only the star's spectral lines are visible because the exoplanet's spectrum is much too faint to see.

##
## Setup Figure 2
##

# Slider to adjust velocity (away or towards Earth) of the star in question

# Each hydrogen spectral line for blue star (central star)
# Note: d-delta,g-gamma,b-beta,a-alpha
dval1 = widgets.Text(value=str(0.0))
gval1 = widgets.Text(value=str(0.0))
bval1 = widgets.Text(value=str(0.0))
aval1 = widgets.Text(value=str(0.0))
# Each hydrogen spectral line for red star (outer star)
dval2 = widgets.Text(value=str(0.0))
gval2 = widgets.Text(value=str(0.0))
bval2 = widgets.Text(value=str(0.0))
aval2 = widgets.Text(value=str(0.0))

# Label for the velocity slider
speed_label1 = widgets.HTML(value='<b>Radial velocity of Star</b>: ')
speed_label2 = widgets.HTML(value='<b>Radial velocity of Orbiting Object</b>:')
# velocity output for each star
vel1_label = widgets.Text(value='0', positioning='right')
vel2_label = widgets.Text(value='0', positioning='right')
vunits1 = widgets.HTML(value='km/s')
vunits2 = widgets.HTML(value='km/s')
# labels direction each star is moving
direction1 = widgets.HTML(value='')
direction2 = widgets.HTML(value='')

# Creates a slider to animate the motion of the stars.
theta_slider = widgets.IntSlider(
    value=0,
    min=0,
    max=99,
    step=1,
    disabled=False,
    continuous_update=True,
    orientation='horizontal',
    readout=True,
    readout_format='.0f',
    layout=widgets.Layout(width='200px')
)

# Animate the stars
theta_play = widgets.Play(value = 0, min=theta_slider.min, max=theta_slider.max, 
                          step=1, description="Press play", 
                          disabled=False, _repeat=True, show_repeat=False)
widgets.jslink((theta_play, 'value'), (theta_slider, 'value'))

# Slider to adjust the 'brightness' (opacity) of the small outer star.
Lumen = widgets.FloatSlider(
    value=0,
    min=0,
    max=1,
    step=.01,
    disabled=False,
    continuous_update=True,
    orientation='horizontal',
    readout=False,
    layout=widgets.Layout(width='340px')
)
lumen_label = widgets.HTML(value='<b>Brightness of Orbiting Object</b>')
star1_label = widgets.HTML(value='<b>Central Star</b>')
star2_label = widgets.HTML(value='<b>Orbiting Object</b>')
line_label = widgets.HTML(value='<b>Line Name (Lab Wavelength)</b>')

picker = widgets.RadioButtons(value='entire spectrum', options=[('entire spectrum' , 'entire spectrum'),('near 410.2nm' , 'violet'),('near 434.0nm' , 'blue'),('near 486.1nm' , 'cyan'),('near 656.3nm' , 'red')])
picker_label = widgets.HTML(value='<b>Display Range</b>')

planet_star = widgets.RadioButtons(value='Star', options=['Star','Planet'])
planet_star_label = widgets.HTML(value='<b>Orbiting Object</b>')


### STAR VELOCITY INFO ###

mass1a = 5 # solar masses
mass2a = 1 # solar masses
a = 1 # semimajor axis in AU
e = 0.0 # eccentricity
incl = 88 # inclination angle of 88 degrees

mass1b = 1
mass2b = 1/1000

# Create a binary star model and radial velocity data in it
bsm = star.BinaryStarModel(mass1a, mass2a, a, e, rv_init=True,incl=incl, N=360)
bsm_b = star.BinaryStarModel(mass1a, mass2a, a, e, incl=0, rv_init=True)
#This created two pandas Dataframes
#bsm.orbit_info
#bsm.radvel_info

phase = bsm.radvel_info['phase']
vel1 = bsm.radvel_info['v1r']
vel2 = bsm.radvel_info['v2r']

#binary_view = star.BinaryStarViewer(bsm=bsm, t_idx0=0, view_width=400, view_height=400)
#binary_renderer = binary_view.renderer

# The BinaryStarModel will automatically update if you change sthe masses or semi-major axis
# but to get the BinaryStarViewer to change automatically for these changes, you need to link
# it using a traitlet link.
#orbit_change_link = traitlets.directional_link((bsm, 'mdl_counter'), (binary_view, 'mdl_counter'))


# Define Figure
fig = bq.Figure(title = 'Hydrogen Absorbtion Spectra', axes=[ax_x, ax_y], animation = 100, 
                marks = [wide_line, hydrogen_line1, hydrogen_line2,hydrogen_line3,Lab_label], 
                padding_y=0, min_aspect_ratio=2.5, max_aspect_ratio=2.5)
# Size figure
fig.layout.width = '500px'
fig.layout.height = '200px'
fig.layout.overflow = 'hidden'


## Create star animation 
# Setup intial conditions for the orbiting stars.
# d1,d2 are x positions and k1,k2 are y positions
phi = theta_slider.value*3.60
r = 1
d1 = r*np.cos(np.pi/180 * phi)
k1 = r*np.sin(np.pi/180 * phi)
r2 = 10
d2 = -r2*np.cos(np.pi/180 * phi)
k2 = -r2*np.sin(np.pi/180 * phi)

# Axes for stars
# Sets axis scale for x and y to 
sc_x = bq.LinearScale(min=-10,max=10)
sc_y = bq.LinearScale(min=-10,max=10)

# Sets up the axes, grid-lines are set to black so that they blend in with the background.
x_ax = bq.Axis(scale=sc_x, grid_color='white', num_ticks=0)
y_ax = bq.Axis(scale=sc_y, orientation='vertical', grid_color='white', num_ticks=0)

# Create the stars and the figure to contain them
star1 = bq.Scatter(x=[d1], y=[k1], scales={'x': sc_x, 'y': sc_y}, colors=['blue'],default_size=500)
star2 = bq.Scatter(x=[d2], y=[k2], scales={'x': sc_x, 'y': sc_y}, colors=['red'])
# Gives reference to Earth
to_earth = bq.Lines(x = [[5,10],[10,9],[10,9]], y = [[6,6],[6,7],[6,5]], scales={'x': sc_x, 'y': sc_y}, colors=['yellow'])
earth_label = bq.Label(text=["To Earth"], x=[5], y=[4], colors=['yellow'], scales={'x': sc_x, 'y': sc_y})
fig_star = bq.Figure(title='Stellar System Top-Down View', marks=[star1,star2,to_earth,earth_label], axes=[x_ax, y_ax], 
                padding_y=0, animation=100, background_style={'fill' : 'black'},
               min_aspect_ratio=1, max_aspect_ratio=1)

fig_star.layout.height = fig.layout.width
fig_star.layout.width = fig.layout.width

## Update the widgets
dval1.observe(update, names=['value'])
gval1.observe(update, names=['value'])
bval1.observe(update, names=['value'])
aval1.observe(update, names=['value'])

vel1_label.observe(update, names=['value'])
vunits1.observe(update, names=['value'])
direction1.observe(update, names=['value'])

dval2.observe(update, names=['value'])
gval2.observe(update, names=['value'])
bval2.observe(update, names=['value'])
aval2.observe(update, names=['value'])

vel2_label.observe(update, names=['value'])
direction2.observe(update, names=['value'])

theta_slider.observe(update, names=['value'])
Lumen.observe(update_lumen, names=['value'])

picker.observe(update_view, names=['value'])
picker.observe(update, names=['value'])
planet_star.observe(update, names=['value'])
planet_star.observe(update_view, names=['value'])

## Display to the screen

# these boxes contain display commands for the velocity of each star
speed1_label_box = widgets.HBox([speed_label1 ,vel1_label, vunits1, direction1])
speed2_label_box = widgets.HBox([speed_label2, vel2_label, vunits2, direction2])

# Commands to properly size the velocity boxes
speed_label1.layout.width = speed_label_width 
speed_label2.layout.width = speed_label_width 
vel1_label.layout.width = vel_value_width 
vel2_label.layout.width = vel_value_width 
vunits1.layout.width = unit_text_width
vunits2.layout.width = unit_text_width
direction1.layout.width = direction_width
direction2.layout.width = direction_width
speed1_label_box.layout.height=line_height
speed2_label_box.layout.height=line_height
speed1_label_box.layout.overflow='visible'
speed2_label_box.layout.overflow='visible'

# Set display elements for spectral line Doppler shift data
dval1.layout.width = value_width
gval1.layout.width = value_width
bval1.layout.width = value_width
aval1.layout.width = value_width
dval2.layout.width = value_width
gval2.layout.width = value_width
bval2.layout.width = value_width
aval2.layout.width = value_width

# These boxes contain the labels for the wavelengths and the shift in wavelength
# text boxes.
shift_label1_box = widgets.HBox([shift_label1, shift_label, dval1, units, dval2, units])
shift_label2_box = widgets.HBox([shift_label2, shift_label, gval1, units, gval2, units])
shift_label3_box = widgets.HBox([shift_label3, shift_label, bval1, units, bval2, units])
shift_label4_box = widgets.HBox([shift_label4, shift_label, aval1, units, aval2, units])
shift_label1_box.layout.height=line_height
shift_label2_box.layout.height=line_height
shift_label3_box.layout.height=line_height
shift_label4_box.layout.height=line_height
shift_label1_box.layout.overflow='visible'
shift_label2_box.layout.overflow='visible'
shift_label3_box.layout.overflow='visible'
shift_label4_box.layout.overflow='visible'

star_labels = widgets.HBox([line_label, star1_label, star2_label])
line_label_width = '240px'  # About labelwidth + shift_text_width
col_label_width = '130px'  # About value_width + unit_text_width
line_label.layout.width = line_label_width
star1_label.layout.width = col_label_width
star2_label.layout.width = col_label_width

# Box to contain all of the above boxes
read_box = widgets.VBox([speed1_label_box, speed2_label_box, star_labels,
                         shift_label1_box, shift_label2_box, shift_label3_box, shift_label4_box])
read_box.layout.width = box_width

# box for the star animation control
theta_label = widgets.HTML('<b>Percent of Orbit Done:</b>')
theta_label.layout.width = speed_label_width
phase_angle_box = widgets.HBox([theta_label, theta_slider, theta_play])
phase_angle_box.layout.width = box_width

# selectors
col_width = '150px'
line_select = widgets.VBox([picker_label, picker])
obj_select = widgets.VBox([planet_star_label, planet_star])
planet_star_label.layout.width = col_width
planet_star.layout.width = col_width
picker_label.layout.width = col_width
picker.layout.width = col_width
select = widgets.HBox([line_select, obj_select])

# combines the above boxes and brightness controls into one box
right_side_box = widgets.VBox([read_box, phase_angle_box, lumen_label, Lumen, select])
right_side_box.layout.width = box_width

# box for the figures
fig_box = widgets.VBox([fig, fig_star])

# Bring it all together
boxy = widgets.HBox([fig_box, right_side_box])

# Make sure lumen slider value is reflected in opacities
update_lumen()

display(boxy)

