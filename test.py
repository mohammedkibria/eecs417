from neuron import h
import neuron

pre = h.Section()
post = h.Section()

for sec in pre, post:
    sec.insert("hh")

stim = h.IClamp(0.5, sec=pre)
stim.amp = 10.0
stim.delay = 5.0
stim.dur = 5.0

syn = h.ExpSyn(0.5, sec=post)

nc = h.NetCon(pre(0.5)._ref_v, syn)
nc.weight[0] = 2.0

vec = {}
for var in 'v_pre', 'v_pre2', 'v_post', 'i_syn', 't':
    vec[var] = h.Vector()

vec['v_pre'].record(pre(0.5)._ref_v)
vec['v_pre2'].record(pre(0.9)._ref_v)
vec['v_post'].record(post(0.5)._ref_v)
vec['i_syn'].record(syn._ref_i)
vec['t'].record(h._ref_t)

neuron.init()
neuron.run(20.0)

import pylab
pylab.subplot(3,1,1)
pylab.plot(vec['t'], vec['v_pre'],
           vec['t'], vec['v_post'])
pylab.subplot(3,1,2)
pylab.plot(vec['t'], vec['v_pre2'],
           vec['t'], vec['v_post'])
pylab.subplot(3,1,3)
pylab.plot(vec['t'], vec['i_syn'])
pylab.show()
