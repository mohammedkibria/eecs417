import neuron
from matplotlib import pyplot as plt
import math
import numpy as np

h = neuron.h
soma = h.Section(name="soma")
soma.nseg = 3000
soma.L = 10000
soma.insert("hh")

simulation_length = 40 # msec
dt = .0000001 # msec
frequency = 50000 # Hertz
t_values = np.arange(0, simulation_length, dt)
# sin_values = 10000 * np.sin(t_values * 2 * np.pi * frequency / 1000)
# sin_vector = h.Vector(sin_values)
# stimobj  = h.IClamp(soma(0.5))
# stimobj.delay = 0
# stimobj.dur = 10000000000
# sin_vector.play(stimobj._ref_amp, dt)

apobj = h.IClamp(0.1, sec=soma)
apobj.delay = 1
apobj.dur = 5
apobj.amp = 1000


v_vec = h.Vector()
t_vec = h.Vector()
v_length = []
amp_vec = h.Vector()
# amp_vec.record(stimobj._ref_amp)
v_vec.record(soma(0.9)._ref_v)
t_vec.record(h._ref_t)

neuron.init()
neuron.h.finitialize(-65)
neuron.run(40.0)

plt.figure(figsize=(8,4))
plt.plot(t_vec,v_vec)
plt.xlabel('time (ms)')
plt.ylabel('mV')
plt.show()
