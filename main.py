import neuron
from matplotlib import pyplot as plt

h = neuron.h
soma = h.Section(name="soma")
soma.nseg = 15
soma.insert("hh")
soma.L = 20
asyn = h.AlphaSynapse(soma(0.5))
asyn.onset = 20
asyn.gmax = 1
h.psection()

v_vec = h.Vector()
t_vec = h.Vector()
x_vec = h.Vector()
v_vec.record(soma(0.8)._ref_v)
t_vec.record(h._ref_t)

neuron.init()
neuron.run(40.0)

plt.figure(figsize=(8,4))
plt.plot(t_vec,v_vec)
plt.xlabel('time (ms)')
plt.ylabel('mV')
plt.show()