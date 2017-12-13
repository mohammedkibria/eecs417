import neuron
from matplotlib import pyplot as plt
import math
import numpy as np


def ez_record(h,var='v',sections=None,order=None,
              targ_names=None,cust_labels=None):
    """
    Records state variables across segments
    Args:
        h = hocObject to interface with neuron
        var = string specifying state variable to be recorded.
              Possible values are:
                  'v' (membrane potential)
                  'cai' (Ca concentration)
        sections = list of h.Section() objects to be recorded
        targ_names = list of section names to be recorded; alternative
                     passing list of h.Section() objects directly
                     through the "sections" argument above.
        cust_labels =  list of custom section labels
    Returns:
        data = list of h.Vector() objects recording membrane potential
        labels = list of labels for each voltage trace
    """
    if sections is None:
        if order == 'pre':
            sections = allsec_preorder(h)
        else:
            sections = list(h.allsec())
    if targ_names is not None:
        old_sections = sections
        sections = []
        for sec in old_sections:
            if sec.name() in targ_names:
                sections.append(sec)

    data, labels = [], []
    for sec in sections:
        positions = np.linspace(0,1,sec.nseg+2)
        for position in positions[1:-1]:
            # record data
            data.append(h.Vector())
            if var is 'v':
                data[-1].record(sec(position)._ref_v)
            elif var is 'cai':
                data[-1].record(sec(position)._ref_cai)
            # determine labels
            lab = sec.name()+'_'+str(round(position,5))
            labels.append(lab)

    return data, labels


def ez_convert(data):
    """
    Takes data, a list of h.Vector() objects filled with data, and converts
    it into a 2d numpy array, data_clean. This should be used together with
    the ez_record command.
    """
    data_clean = np.empty((len(data[0]),len(data)))
    for (i,vec) in enumerate(data):
        data_clean[:,i] = vec.to_python()
    return data_clean


h = neuron.h
soma = h.Section(name="soma")
soma.nseg = 1000
soma.L = 100000 # um
soma.diam = 10 # um
soma.Ra = 100 # Axial resistance Ohm * cm
soma.cm = 1 # Membrane capacitance in uF / cm^2
soma.insert("hh")

simulation_length = 100 # msec
h.dt = .01 # msec
frequency = 1000 # Hertz
t_values = np.arange(0, simulation_length + 2*h.dt, h.dt)
sin_values = 10 * np.sin(t_values * 2 * np.pi * frequency / 1000)
sin_vector = h.Vector(sin_values)
stimobj  = h.IClamp(soma(0.5))
stimobj.delay = 0
stimobj.dur = 1E10
sin_vector.play(stimobj._ref_amp, h.dt)

apobj = h.IClamp(0.05, sec=soma)
apobj.delay = 10
apobj.dur = 5
apobj.amp = 1000

voltages, labels = ez_record(h, sections=[soma])

v_vec1 = h.Vector()
v_vec2 = h.Vector()
v_vec3 = h.Vector()
v_vec4 = h.Vector()
v_vec5 = h.Vector()
v_vec6 = h.Vector()
v_vec7 = h.Vector()
v_vec8 = h.Vector()
v_vec9 = h.Vector()
t_vec = h.Vector()
v_length = []
amp_vec = h.Vector()
v_vec1.record(soma(0.1)._ref_v)
v_vec2.record(soma(0.2)._ref_v)
v_vec3.record(soma(0.3)._ref_v)
v_vec4.record(soma(0.4)._ref_v)
v_vec5.record(soma(0.5)._ref_v)
v_vec6.record(soma(0.6)._ref_v)
v_vec7.record(soma(0.7)._ref_v)
v_vec8.record(soma(0.8)._ref_v)
v_vec9.record(soma(0.9)._ref_v)
t_vec.record(h._ref_t)

neuron.h.finitialize(-70)
neuron.run(100)

fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)
ax1.plot(t_vec,v_vec1,
         t_vec,v_vec2,
         t_vec,v_vec3,
         t_vec,v_vec4)
ax2.plot(t_vec, sin_values)
ax3.plot(t_vec,v_vec6,
         t_vec,v_vec7,
         t_vec,v_vec8,
         t_vec,v_vec9)

plt.xlabel('time (ms)')
plt.ylabel('mV')
plt.show()
