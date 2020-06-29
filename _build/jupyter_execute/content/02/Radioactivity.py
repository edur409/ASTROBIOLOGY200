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

# Radioactive Decay Interactives

The following interactive figures were borrowed from [Astro Interactives](https://juancab.github.io/AstroInteractives/) and adapted for easy access into this Jupyter Book. The first one shows the random yet predictable nature of radioactive decay and its use as a time clock.  The second one illustrates Geochron plots. 

## Interactive Figure 1: Model of Radioactive Decay

This first figure takes a population of 900 atoms and models their radioactive decay.

This first interactive is designed to allow you to explore what happens during radioactive decay of some isotope. An *isotope* refers to a particular version of an element.  For example, the non-radioactive Carbon-12 isotope has 6 protons and 6 neutrons in its nucleus but the radioactive Carbon-14 isotope has 6 protons and 8 neutrons in its nucleus.  Different isotopes of the same element behave identically in terms of chemistry and bonding to other atoms, but their nuclear properties can differ.

During radioactive decay, a *parent isotope* is said to decay into a *daughter isotope*.  So, for example, the parent isotope of Carbon-14 decays into Nitrogen-14.  There is no way to predict when any one nucleus of a *parent isotope* will decay into a *daughter isotope*.   That said, if you look at a large number of nuclei of a parent isotope, they exhibit a very simple property:

> **The same *fraction* of a radioactive parent isotope will decay over the same amount of time.**
    
The time it takes for one-half of a population of parent isotopes to decay (on average) into daughter isotopes is called the *half-life* of that isotope.  Different parent isotopes can have very different half-lifes.   **NOTE:** This interactive shows a simulation of the decay of only 900 atoms.  The radioactive decay is still modelled as occurring randomly for any one atom, so the simulation will show slightly different results on different runs!!

Some questions to consider 
1. After 1 half-life, about 50% of a parent isotope should have decayed and become daughter isotope.  Use the interactive graphic below and adjust the elapsed time to figure out how long one half-life is for each isotope.  Explain your approach.
2. How much of a parent isotope is left after 2 half-lifes? 3 half-lifes? 4 half-lifes? 5 half-lifes?  Explain how you figured this out.
3. You should have found about 25% of the original amount of parent isotope is left after 2 half-lifes.  This may seem surprising since in the first half-life 50% of the original amount of parent isotope decayed.  Explain why 'less' of it decayed during the second half-life.  **HINT** Consider the very simple property of radioactive decay we highlighted above.

from IPython.display import display
import numpy as np
import bqplot as bq
import ipywidgets as widgets
import random as random
import pandas as pd
import number_formatting as nf
from math import ceil, floor, log10

## Originally developed June 2018 by Samuel Holen
##
## Edits by Juan Cabanela October 2018 to allow changes in the GUI.
## - Made the display of the precise number/faction of parent/daught atoms instructor
##   configurable.
## - Fixed a problem with the display of data, forced data to only be displayed for first
##   10 half-lifes regardless of actual generated decay times (this allows hard-coding of)
##   num_ticks and tick values.

## Pre-construct model of radioactive decay of a population
## of parent and daughter atoms.
## 

# GUI Configuration Parameters
show_counts = True
max_half_lifes = 10   # maximum half-lives to graph
time_ticks = 6  # number of ticks for the time axis
# half-lives to place ticks on horizontal axis
half_life_ticks = np.linspace(0, max_half_lifes, time_ticks)

# Constants Related to decay of the parent species to the daughter species
N_parent = 900          # initial number of parent atoms (should be a perfect square)
N_daughter = 0          # initial number of daughter atoms
tau = 1                 # placeholder for the half-life of the parent species 
h = 0.025               # time step (in half lives)
mu = np.log(2.) / tau   # constant for decay time distribution 
Plot_all_times = True   # Plot all times (otherwise, selects only before time slider value)

# Initialize tracking of number of atoms
Parent_counts = []          # list of number of parent atoms 
Dauther_counts = []          # list of number of daughter atoms

# Generate a uniform random distribution of N_parent numbers from 0 to 1
z = np.random.rand(N_parent)

# Function to convert uniform distribution of random numbers to
# a distribution weighted to model radiactive decay. The times are in number of 
# half-lives. 
#
# The unsorted data representing the number of half-lifes until the individual
# decay of each atom.
decay_times = -np.log(1 - z) / mu
decay_times_sorted = np.sort( decay_times )

# Genereate array of numbers of atoms left
# Adjusted so that each count contains 0 and N_parent
Parent_counts = np.arange(N_parent,-1, -1, dtype='int') # Number of parent atoms
Daughter_counts = np.ones_like(Parent_counts)
Daughter_counts = N_parent - Parent_counts   # Number of daughter atoms

#
# Construct Pandas data frames
#

# Time column adjusted to include t=0
decay_data = pd.DataFrame()
decay_data['time'] = np.concatenate((np.zeros(1), decay_times_sorted))
decay_data['Parent'] = Parent_counts
decay_data['Daughter'] = Daughter_counts

# Data array for species
species = pd.DataFrame()
species['parent_long'] = ['Generic', 'Carbon', 'Thallium','Uranium','Rubidium']
species['daughter_long'] = ['Generic', 'Nitrogen','Lead','Thorium','Strontium']
species['parent_short'] = ['Parent', 'C-14','Tl-208','U-235','Rb-87']
species['daughter_short'] = ['Daughter', 'N-14','Pb-208','Th-231','Sr-87']
species['half-lives'] = [tau, 5730, 3.053 * 60, 703.8, 48.8]
species['step-size'] = [h, 125, 0.05 * 60, 15, 1]
species['timeunits'] = ['half-lives', 'years', 'seconds', 'million years', 'billion years']

##
## Define functions to respond to controls on population plots.
##

def UpdateSpecies(change=None):
    ##
    ## Deal with possible changes of species
    ##
    
    # Generate a new uniform random distribution of N_parent numbers from 0 to 1 and
    # then convert uniform distribution to one weighted to model radioactive decay.
    z = np.random.rand(N_parent)
    decay_times = -np.log(1 - z) / mu
    decay_times_sorted = np.sort( decay_times )
    decay_data['time'] = np.concatenate((np.zeros(1), decay_times_sorted))
    
    # Reset the time to zero
    Time_slide.value = 0
    
    # Adjust half-life data and limits on plots appropriately 
    new_index = species.loc[species.parent_long == pick_Species.value].index[0]
    
    # Set the half-life based the selected species
    hf = species['half-lives'][new_index]
    
    # Set the limit on the time sider to be 10 half-lifes
    Time_slide.max = max_half_lifes*hf
    
    # Set the time step on slider
    Time_slide.step = species['step-size'][new_index]

    # Updates the time slider label/units
    unit_label.value = species['timeunits'][new_index]
    
    # Updates the time axes on the plot
    x_time.max = Time_slide.max
    ax_x_time.scale = x_time
    ax_x_time.label = unit_label.value
    
    # Update tick values
    ax_x_time.tick_values = list(half_life_ticks*hf)

    # Update the legend
    parent_label_new = species['parent_short'][new_index]
    daughter_label_new = species['daughter_short'][new_index]
    line_parent.labels = [parent_label_new]
    line_daughter.labels = [daughter_label_new]
    
    # Update the species in the box that shows how many are present    
    parent_label.value = parent_label_new + ' produced'
    daughter_label.value = daughter_label_new + ' remaining'

    # Now call the function for updating the plot in the event of a time change
    UpdateTimes()

    
def UpdateFraction(change=None):
    ##
    ## Deal with whether fraction view or number view selected to set scales for plot,
    ## y values for plot, and label values
    ##
    if frac_or_num.value == False:
        # Number count mode enabled

        # Update axes and scales
        fig_counts.axes = [ax_x_time, ax_y_number]
        line_parent.scales={'x': x_time, 'y': y_number}
        line_daughter.scales={'x': x_time, 'y': y_number}
        pts_parent.scales={'x': x_time, 'y': y_number}
        pts_daughter.scales={'x': x_time, 'y': y_number}
        line_time.scales={'x': x_time, 'y': y_number}

        # Update 'time line' limits
        line_time.y = [0, N_parent]    
    else:
        # Fraction mode enabled

        # Updated axes and scales
        fig_counts.axes = [ax_x_time, ax_y_fraction]
        line_parent.scales={'x': x_time, 'y': y_fraction}
        line_daughter.scales={'x': x_time, 'y': y_fraction}
        pts_parent.scales={'x': x_time, 'y': y_fraction}
        pts_daughter.scales={'x': x_time, 'y': y_fraction}
        line_time.scales={'x': x_time, 'y': y_fraction}

        # Update 'time line' limits
        line_time.y = [0, 1]

    UpdateTimes()

    
def UpdateTimes(change=None):
    ##
    ## Deal with changes in the time slider
    ##

    # Recall half-life of this species
    species_idx = species.loc[species.parent_long == pick_Species.value].index[0]
    hf = species['half-lives'][species_idx]

    # Update time label with 3 significant figures
    Time_label.value = str(nf.SigFig(Time_slide.value, 3))
        
    # Get the array of times
    time_arr = hf * decay_data['time']
    
    # Set the times to be x values
    line_daughter.x = time_arr
    line_parent.x = line_daughter.x
    pts_daughter.x = line_daughter.x
    pts_parent.x = line_daughter.x
    line_time.x = [Time_slide.value, Time_slide.value]
    
    # Changes the color of population to reflect the decays
    for i in range(N_parent):
        if Time_slide.value >= decay_times[i]*hf:
            Colors[i] = 'blue'
        else:
            Colors[i] = 'red'
    population_scat.colors = Colors
    
    # Identify where we are in the data set
    i = 0
    while i < N_parent + 1 and hf*decay_data['time'][i] < Time_slide.value:        
        i += 1
    if i > 0:
        i -= 1
        
    # Update selection of the parent and daughter data to be plotted
    if Plot_all_times:
        daughter_decay = decay_data['Daughter']
        parent_decay = decay_data['Parent']
    else:
        daughter_decay = decay_data['Daughter'][0:i+1]
        parent_decay = decay_data['Parent'][0:i+1] 
    
    line_parent.y = parent_decay
    line_daughter.y = daughter_decay
        
    ##
    ## Deal with whether fraction view or number view selected to set scales for plot,
    ## y values for plot, and label values
    ##
    if frac_or_num.value == False:
        # Number count mode enabled

        # Update number of parent and daughter in labels
        parent_present.value = str(decay_data['Parent'][i])
        daughter_present.value = str(decay_data['Daughter'][i])
    else:
        # Fraction mode enabled
        
        # Update the x and y arrays for the parent and daughter lines
        line_parent.y = (1/N_parent)*parent_decay
        line_daughter.y = (1/N_parent)*daughter_decay
    
        # Update number of parent and daughter in labels
        parent_present.value = '{:.3f}'.format((1/N_parent)*decay_data['Parent'][i])
        daughter_present.value = '{:.3f}'.format((1/N_parent)*decay_data['Daughter'][i])
    
    # Update parent and daughter lines
    pts_parent.y = line_parent.y
    pts_daughter.y = line_daughter.y
    
    # Update the tooltip labels and formats (Bug? Doesn't appear to be working)
    #pts_parent.tooltip.labels[1] = parent_label_new
    #pts_daughter.tooltip.labels[1] = daughter_label_new
    #if frac_or_num.value == False:
    #    pts_parent.tooltip.formats[1] = '3.0f'
    #    pts_daughter.tooltip.formats[1] = '3.0f'
    #else:
    #    pts_parent.tooltip.formats[1] = '0.3f'
    #    pts_daughter.tooltip.formats[1] = '0.3f'
        


##
## Set up counts versus time plot
##

# Set up Species to be Generic
init_species_ind = 0  

# Set up initial time
init_time = 0
init_time_idx = 0

# Set up axes
x_time = bq.LinearScale(min = 0, max=max_half_lifes)
y_number = bq.LinearScale(min = 0, max=N_parent)
y_fraction = bq.LinearScale(min = 0, max=1)

# Labels and scales for Axes
ax_x_time = bq.Axis(label=species['timeunits'][init_species_ind], scale=x_time, num_ticks = time_ticks,
                    tick_values = half_life_ticks )
ax_y_number = bq.Axis(label='Number of atoms', scale=y_number, orientation='vertical')
ax_y_fraction = bq.Axis(label='Fraction of atoms', scale=y_fraction, orientation='vertical')

# Define tooltip (Bug: doesn't allow relabeling Tooltips, also needs to apply to Scatter, not Lines)
#def_tt_parent = bq.Tooltip(fields=['x', 'y'], formats=['.2f', '3.0f'], labels=['time', species['parent_short'][init_species_ind]])
#def_tt_daughter = bq.Tooltip(fields=['x', 'y'], formats=['.2f', '3.0f'], labels=['time', species['daughter_short'][init_species_ind]])
def_tt_parent = bq.Tooltip(fields=['x', 'y'], formats=['.2f', '.3f'], labels=['time', 'amount of parent isotope'])
def_tt_daughter = bq.Tooltip(fields=['x', 'y'], formats=['.2f', '.3f'], labels=['time', 'amount of daughter isotope'])

# Define the Lines and Scatter plots
# NOTE: Scatter only necessary to allow tooltips to function.
init_x = decay_data['time']*species['half-lives'][init_species_ind]
if Plot_all_times:
    init_parent = decay_data['Parent']
    init_daughter = decay_data['Daughter']
else:
    init_parent = decay_data['Parent'][0:init_time_idx]
    init_daughter = decay_data['Daughter'][0:init_time_idx]
    
pts_parent = bq.Scatter(x=init_x, y=init_parent,
                      scales={'x': x_time, 'y': y_number}, marker='circle', default_size=2,
                      display_legend=False, colors=['red'], labels=[species['parent_short'][init_species_ind]], 
                      tooltip=def_tt_parent)
pts_daughter = bq.Scatter(x=init_x, y=init_daughter,
                        scales={'x': x_time, 'y': y_number}, marker='circle', default_size=2,
                        display_legend=False, colors=['blue'], labels=[species['daughter_short'][init_species_ind]],
                        tooltip=def_tt_daughter)
line_parent = bq.Lines(x=init_x, y=init_parent, 
                       scales={'x': x_time, 'y': y_number}, display_legend=True, colors=['red'], 
                       labels=[species['parent_short'][init_species_ind]], )
line_daughter = bq.Lines(x=init_x, y=init_daughter, 
                         scales={'x': x_time, 'y': y_number}, display_legend=True, colors=['blue'], 
                         labels=[species['daughter_short'][init_species_ind]] )

# Set up a vertical line on this plot to indicate the current time
times_x = [init_time, init_time]
times_y = [0, N_parent]
line_time = bq.Lines(x=times_x, y=times_y,
                     scales={'x': x_time, 'y': y_number}, 
                     colors=['greenyellow'])

# Creates figure for plot
fig_counts = bq.Figure(axes=[ax_x_time, ax_y_number], marks=[line_parent, line_daughter, line_time, pts_parent, pts_daughter], 
                       legend_location='right', legend_style={'fill': 'white'}, 
                       title='Counts versus Time', background_style={'fill': 'black'}, 
                       layout={'width': '500px', 'min_height': '400px'},
                      animation=1000)

# Slider widget to control the amount of time that has passed
# Set for generic half-life situation initially (0 to 10 half-lifes)
Time_slide = widgets.FloatSlider(
    value=0.,
    description='Time',
    min=0.,
    max=max_half_lifes,
    step=h,
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=False,
    readout_format='.1f',
    layout=widgets.Layout(overflow_x='visible',
                          overflow_y='visible',
                          width='400px',
                          max_width='500px',
                          min_width='250px')
)

# Widget to display the number of parent atoms present
parent_present = widgets.Text(
    value = str(N_parent),
    style = {'description_width': 'initial'},
    #description = species['parent_short'][0]+' remaining',
    disabled = True,
    layout=widgets.Layout(overflow_x='visible',
                          overflow_y='visible',
                          width='175px',
                          max_width='300px',
                          min_width='125px')
)

# Widget to display the number of daughter atoms present
daughter_present = widgets.Text(
    value = str(0),
    style = {'description_width': 'initial'},
    #description = species['daughter_short'][0]+' produced',
    disabled = True,
    layout=widgets.Layout(overflow_x='visible',
                          overflow_y='visible',
                          width='175px',
                          max_width='300px',
                          min_width='125px')
)

# Widgets to label the time slider with units
Time_label = widgets.Label(value=str(Time_slide.value))
unit_label = widgets.Label(value=str(species['timeunits'][0]))
Composite_Time_Label = widgets.HBox([Time_label, unit_label],
                                   layout=widgets.Layout(width='200px'))

# Labels for the parent/daughter present displays
parent_label = widgets.Label(value=species['parent_short'][0]+' remaining',
                             layout=widgets.Layout(width='200px', 
                                                   overflow_x='visible',
                                                   overflow_y='visible') )
daughter_label = widgets.Label(value=species['daughter_short'][0]+' produced',
                             layout=widgets.Layout(width='200px', 
                                                   overflow_x='visible',
                                                   overflow_y='visible') )

# Checkbox to choose whether to display the number of each species
# or the fraction of each
frac_or_num = widgets.Checkbox(value=False, description='Display as fraction of atoms')

# Widget to allow one to choose which species to work with
pick_Species = widgets.RadioButtons(options=species['parent_long'][:],
                                    value='Generic', description='Species:', disabled=False,
                                    layout=widgets.Layout(width='250px'))


# Scale for population figure
x_sc = bq.LinearScale(min=1, max=np.sqrt(N_parent))
y_sc = bq.LinearScale(min=1, max=np.sqrt(N_parent))

# Axes for population figure
ax_x = bq.Axis(scale=x_sc, num_ticks=0)
ax_y = bq.Axis(scale=y_sc, orientation='vertical', num_ticks=0)

# Creates an array of x values: [1,2,...,30,1,2,...30,.....,1,2,...,30]
x_ls = []
for i in range(1,int(np.sqrt(N_parent))+1):
    x_ls.append(float(i))
x_ls = x_ls * int(np.sqrt(N_parent))
x_arr = np.array(x_ls)

# Creates an array of y values: [1,1,...,1,2,2,...2,......,30,30,...,30]
y_ls = []
for i in range(1,int(np.sqrt(N_parent))+1):
    y_ls += [float(i)] * int(np.sqrt(N_parent))
y_arr = np.array(y_ls)    

# Creates a color array with the same number of entries as the number of atoms in
# the sample
Colors = ['red'] * N_parent

# Plot the population model
population_scat = bq.Scatter(x=x_arr, y=y_arr, scales={'x': x_sc, 'y': y_sc}, colors =['red'])

# Picking a new species resets everything
pick_Species.observe(UpdateSpecies, names=['value'])

# Update view from fraction to/from number
frac_or_num.observe(UpdateFraction, names=['value'])

# Update times
Time_slide.observe(UpdateTimes, names=['value'])
Time_label.observe(UpdateTimes, names=['value'])

# Figure for the population
fig_population = bq.Figure(title='Population of Atoms', marks=[population_scat], axes=[ax_x, ax_y], 
                background_style={'fill' : 'black'},padding_x = 0.025,
                min_aspect_ratio=1, max_aspect_ratio=1)

# Boxes to organize display
parent_box = widgets.HBox([parent_label, parent_present],
                          layout=widgets.Layout(overflow_x='visible', overflow_y='visible'))
daughter_box = widgets.HBox([daughter_label, daughter_present],
                            layout=widgets.Layout(overflow_x='visible', overflow_y='visible'))
# Set visibility of the exact counts/fractions
if (show_counts == False):
    parent_box.layout.visibility = 'hidden'
    daughter_box.layout.visibility = 'hidden'

value_box = widgets.VBox([parent_box, daughter_box])
species_box = widgets.HBox([value_box, pick_Species])

slide_box = widgets.HBox([Time_slide, Composite_Time_Label])
slide_check_box = widgets.VBox([slide_box, frac_or_num])

top_box = widgets.HBox([fig_counts, fig_population],
                      layout=widgets.Layout(width='900px'))
top_box.children[0].layout.width = '450px'
top_box.children[1].layout.width = '450px'

bottom_box = widgets.HBox([species_box, slide_check_box],
                      layout=widgets.Layout(width='900px'))
bottom_box.children[0].layout.width = '450px'
bottom_box.children[1].layout.width = '450px'

# Final display
Final = widgets.VBox([top_box, bottom_box])
Final.layout.overflow = 'hidden'
display(Final)

## Interactive Figure 2: Geochron Plot

Assuming a non-radiogenic isotope (that is, an isotope that is not the result of radioactive decay) that also will not decay, its amount should be constant.  This means that for different mineral samples we can measure the ratio of parent isotope versus the non-radiogenic isotope ($P/D_i$) and daughter isotope ($D$) versus the non-radiogenic isotope ($D/D_i$) to build an geochron plot.  For example, using the following isotopes

- $D_i$ (non-radiogenic isotope of daughter element)
- $D$ (Daughter Isoptope)
- $P$ (Parent isotope)

an geochron plot could plot $D/D_i$ versus $P/D_i$.  

What sets the *geochron method* (also known as the *isochron method*) apart from the just measuring parent and daughter abundances is the use of the non-radiogenic isotope of the daughter element.  This avoids the assumption of no initial daughter isotope before the rock solidified (radioactive decay can occur while rock is molten).

Some minerals in the rock incorporate the parent better than daughter which is why the initial amount of parent 
isotope versus daughter isotope can vary.  We expect daughter versus non-radiogenic isotope ratio to be constant
if we pick the non-radiogenic isotope to be the same element as the daughter isotope.

With all this said, it is actually often not this simple as many daughter isotopes are themselves radioactive and decay, leading to a chain of reactions, so comparing abundances of parent to daughter isotopes is not simple.

*Note:* The idea for the geochron dating interactive came from a Isochron Diagram Java app at *ScienceCourseware.org*.  However that app had some issues in that it didn't divide by a non-radiogenic isotope (or at least didn't mention it).  In fact, they used $D_i$ for the initial amount of daughter isotope instead of the non-radiogenic isotope of the same element as the daughter isotope.

Consider the following questions:

1. Notice that the geochron shown here is using the parent and daugther isotope ratios for 4 mineral samples in a rock.  Consider the sample that starts off with the most parent isotope initially (the point initially farthest to the right).  Adjust the geochron to show the samples after 1 half-life.  How much of that parent isotope was there initially?  How much is there after 1 half-life?  Does this make sense? 
2. Consider the sample that starts off with the least parent isotope initially (the point initially farthest to the left).  Adjust the geochron to show the samples after 1 half-life.  How much of that parent isotope was there initially?  How much is there after 1 half-life?  Does this make sense? 
3. What fraction of the parent isotope should have decayed into daughter isotope after one half-life?  Does it matter if the mineral sample we look at started with more parent isotope than another mineral sample in the same rock?  Why or why not?  
4. Why is it as time elapses that the points representing the 4 mineral samples all move toward the upper left?  Can you explain why their motions are parallel to one another?
4. Imagine you are looking at the parent isotope Rubidium-87 which decays into Strontium-87.  You examine 4 mineral samples in an meteorite and they line up in a line with a slope of 0.0666.  Determine the age of that meteorite (or rather, the time since it solidified).  Also explain how we can determine how much of the daughter isotope was in the meteorite initially.


##
## Define the various isotopes we want to consider
##

isotope_info = pd.DataFrame(columns=['Name', 'PName', 'PAbbrev', 'DName', 'DAbbrev', 'DiName', 'DiAbbrev', 'HalfLife', 'HLUnits'])
isotope_info['index'] = ['generic', 'Rb87']
isotope_info['Name'] = ['Generic', 'Rb-87->Sr-87']
isotope_info['PName'] = ['Parent', 'Rubidium-87']
isotope_info['PAbbrev'] = ['P', 'Rb-87']
isotope_info['DName'] = ['Daughter', 'Strontium-87']
isotope_info['DAbbrev'] = ['D', 'Sr-87']
isotope_info['DiName'] = ['Non-Radiogenic Isotope of Daughter Element', 'Strontium-86']
isotope_info['DiAbbrev'] = ['D_i', 'Sr-86']
isotope_info['HalfLife'] = [ 1, 48.8 ]
isotope_info['HLUnits'] = [ 'half-lives', 'Billion years']
isotope_info = isotope_info.set_index('index')

# Set initial isotope to plot
init_isotope = 'generic'

##
## Define the initial amounts of parent and daughter in the sample.
##
## In principle, I would change this depending on the isotopes we plot.  But I am only plotting
## Rb87 --> Sr-87, since that is the most classical use of this Geochron approach.
##

# Range of P to D_i fractions and initial amounts of D to D_i to consider
P2Di_min = 0.05
P2Di_max = 0.40
D2Di0_min = 0.05
D2Di0_max = 0.75

# Generate three mineral samples in different thirds of the entire range
range_P2Di  = (P2Di_max-P2Di_min)

# Create sample amounts
n_samples = 4
nums = np.array(list(range(1, n_samples+1)))
initial_samples = pd.DataFrame(index=nums)
initial_D2Di0 = D2Di0_min + (D2Di0_max - D2Di0_min) * np.random.random()
initial_samples['P2Di'] = P2Di_min + (range_P2Di/n_samples) * (nums - np.random.random(n_samples))
initial_samples['D2Di'] = initial_D2Di0*np.ones_like(nums)


##
## Define functions to call when building interactive plot
##

def amt_left(sample_in, taus):
    # Generate a sample DataFrame after tau half-lifes given an initial DataFrame
    sample = sample_in.copy(deep = True)
    sample['P2Di'] = sample_in['P2Di']*((1/2)**(taus))
    sample['D2Di'] = sample_in['D2Di'] + sample_in['P2Di']*(1 - (1/2)**(taus))
    return sample

def line_points(sample):
    global x_min, x_max, y_min, y_max, initial_D2Di0
    
    # Determine the end points of a line going through the sample points.
    x_range = x_max - x_min
    y_range = y_max - y_min
    
    # Slope (extrapolate from first two points - could be done by a fit to the points)
    slope = (sample['D2Di'][2]-sample['D2Di'][1])/(sample['P2Di'][2]-sample['P2Di'][1])
    y_final = initial_D2Di0 + slope*x_range
    x_points = (x_min, x_max)
    y_points = (initial_D2Di0, y_final)
    return x_points, y_points, slope

def init2current(samples0, samples):
    # Compute the lines connecting initital and final points for plotting
    n_pts = len(samples0)

    xlist = []
    ylist = []
    for pt in range(1, n_pts+1):
        x = np.array([ samples0['P2Di'][pt], samples['P2Di'][pt] ])
        y = np.array([ samples0['D2Di'][pt], samples['D2Di'][pt] ])
        xlist.append(x)
        ylist.append(y)
    
    return(xlist, ylist)
    
def HL_changed(change):
    global isotope, sample, initial_samples, dots_current, line_current, connectors, slope_label
    
    # Determine half-life of this isotope
    idx = (isotope_info.Name == isotope.value)
    HL = float(isotope_info[idx].HalfLife.tolist()[0])
    
    # How many half-lives have passed?  Use this to get new sample and line info
    this_tau = HL_slider.value / HL
    sample = amt_left(initial_samples, this_tau)
    x_sample, y_sample, slope =  line_points(sample)
    
    # Update plot
    dots_current.x = sample['P2Di']
    dots_current.y = sample['D2Di']
    line_current.x = x_sample
    line_current.y = y_sample
    slope_label.value = 'Slope: {0:0.4f}'.format(slope)
    xlist, ylist = init2current(initial_samples, sample)
    connectors.x = xlist
    connectors.y = ylist
    
    
def isotope_changed(change):
    global ax_x_P2Di, ax_y_D2Di, HL_slider, HLlabel, UnitsText, Max_half_lives

    # Extract the necessary isotope descriptors from the Pandas DataFrame
    idx = (isotope_info.Name == change.new)
    HL = float(isotope_info[idx].HalfLife.tolist()[0])
    HLUnits = isotope_info[idx].HLUnits.tolist()[0]
    PAbbrev = isotope_info[idx].PAbbrev.tolist()[0]
    DAbbrev = isotope_info[idx].DAbbrev.tolist()[0]
    DiAbbrev = isotope_info[idx].DiAbbrev.tolist()[0]

    # Get old half-life
    idx_old = (isotope_info.Name == change.old)
    HL_old = float(isotope_info[idx_old].HalfLife.tolist()[0])

    # Determine current age reading from slider and adjust to new units
    init_age = HL_slider.value 
    
    # Hard code generic versus others
    if (change.new != isotope_info.loc['generic'].Name):
        HL_slider.description = "Time"
    else: 
        HL_slider.description = "Half-lives"    

    # Adjust time scales
    if (HL_old < HL):
        # Adjust maximum limits first before adjusting values (since new HL > old HL)
        HL_slider.max = Max_half_lives*HL
        HLlabel.max = HL_slider.max 
        HL_slider.value = HL*(init_age/HL_old)
        HLlabel.value = HL_slider.value       
    else:
        # Adjust maximum limits after adjusting values (since new HL < old HL)
        HL_slider.value = HL*(init_age/HL_old)
        HLlabel.value = HL_slider.value
        HL_slider.max = Max_half_lives*HL
        HLlabel.max = HL_slider.max 
                
    # Set the axes and other labels to display
    UnitsText.value = HLUnits
    ax_x_P2Di.label = '{0} / {1}'.format(PAbbrev, DiAbbrev)
    ax_y_D2Di.label = '{0} / {1}'.format(DAbbrev, DiAbbrev)



##
## Set up isochron plot
##

# Largest possible fraction of decay (only go out to 5 half-lives)
Max_half_lives = 5
Max_decay_fraction = 1 - (1/2)**(Max_half_lives)

# detemine maximum and minimum values of X and Y axes
x_step = 0.05
x_min = 0
x_max = x_step * ceil(initial_samples['P2Di'][n_samples] / x_step)
y_step = 0.04
y_min = y_step * floor(initial_D2Di0 / y_step)
y_max = y_step * ceil((initial_D2Di0 + initial_samples['P2Di'][n_samples] * Max_decay_fraction) / y_step)

# Labels and scales for Axes
x_P2Di = bq.LinearScale(min = x_min, max = x_max)
y_D2Di = bq.LinearScale(min = y_min, max = y_max)
ax_x_P2Di = bq.Axis(label='P / D_i', scale=x_P2Di)
ax_y_D2Di = bq.Axis(label='D / D_i', scale=y_D2Di, orientation='vertical')

# Set up initial conditions
taus = 0    # zero half lives past
sample = amt_left(initial_samples, taus)

##
## Define the lines
##

# Initial amount of daughter line (with dots for initial amounts of parent)
x_init, y_init, slope_init =  line_points(initial_samples)
line_initial = bq.Lines(x=x_init, y=y_init, scales={'x': x_P2Di, 'y': y_D2Di}, 
                   line_style='dashed', colors=['red'], labels=['Initial Sample'])
dots_initial = bq.Scatter(x=initial_samples['P2Di'], y=initial_samples['D2Di'], scales={'x': x_P2Di, 'y': y_D2Di}, 
                   colors=['white'], stroke='red', fill= True, labels=['Initial Isochron'])

# Current quantities on isochron line
x_sample, y_sample, slope =  line_points(sample)
line_current = bq.Lines(x=x_sample, y=y_sample, scales={'x': x_P2Di, 'y': y_D2Di}, 
                   line_style='solid', colors=['red'], labels=['Current Isochron'])
dots_current = bq.Scatter(x=sample['P2Di'], y=sample['D2Di'], scales={'x': x_P2Di, 'y': y_D2Di}, 
                   colors=['red'], stroke='red', fill= True, labels=['Current Isochron'])

# Connect Initial and Current quantities on isochron line
xlist, ylist = init2current(initial_samples, sample)
connectors = bq.Lines(x=xlist, y=ylist, scales={'x': x_P2Di, 'y': y_D2Di}, 
                   line_style='dotted', colors=['black'])

##
## Construct plot
##
isochron = bq.Figure(axes=[ax_x_P2Di, ax_y_D2Di], 
                     marks=[connectors, line_initial, dots_initial, line_current, dots_current],
                     title='Geochron Diagram', 
                     layout={'width': '700px', 'height': '500px', 
                             'max_width': '700px', 'max_height': '500px',
                             'min_width': '600px', 'min_height': '400px'})

##
## Construct controls
##

# Select Generic or Specific Isotopes
isotope = widgets.RadioButtons(options=list(isotope_info.Name), 
                               value=isotope_info.loc[init_isotope].Name, description='Isotope:', 
                               disabled=False, 
                               layout=widgets.Layout(height='75px', max_height='100px', min_height='50px', 
                                                    width='200px', max_width='300px',  min_width='100px'))
isotope.observe(isotope_changed, 'value')

# Slider and text field controling age
idx = (isotope_info.Name == isotope.value)
HL = float(isotope_info[idx].HalfLife.tolist()[0])
HLUnits = isotope_info[idx].HLUnits.tolist()[0]

HL_slider = widgets.FloatSlider(value=0, min=0, max=Max_half_lives*HL, step=0.02,
                                description='Half-lives', disabled=False,
                                continuous_update=False, orientation='horizontal',
                                readout=False, readout_format='.2f',
                                layout=widgets.Layout(height='75px', max_height='100px', min_height='50px', 
                                                    width='200px', max_width='300px',  min_width='100px'))
HL_slider.observe(HL_changed, 'value')

# Get units value and units for age label, then apply them
HLlabel = widgets.BoundedFloatText(value = HL_slider.value, min = HL_slider.min, max = HL_slider.max, 
                                   step = HL_slider.step,
                                       layout={'width': '75px', 'height': '50px', 
                                               'max_width': '75px', 'max_height': '75px',
                                               'min_width': '50px', 'min_height': '50px'})
UnitsText = widgets.Label(value=HLUnits)
age_label = widgets.HBox([HLlabel, UnitsText])
# Link HL slider with this text
widgets.jslink((HL_slider, 'value'), (HLlabel, 'value'))

# Describe slope
slope_label = widgets.Label(value = 'Slope: {0:0.4f}'.format(slope),
                                       layout={'align_items':'center','align_content':'center', 
                                               'justify_content':'center', 
                                               'width': '100px', 'height': '50px', 
                                               'max_width': '100px', 'max_height': '75px',
                                               'min_width': '50px', 'min_height': '50px'})


controls = widgets.VBox( [isotope, HL_slider, age_label, slope_label], 
                        layout=widgets.Layout(align_content='center', align_items='center', 
                                              justify_content='center', 
                                              width='300px', height='500px', 
                                              max_width='300px', max_height='500px',
                                              min_width='100px', min_height='400px',
                                              overflow_x='hidden', overflow_y='hidden') )

display(widgets.HBox( [isochron, controls] ) )