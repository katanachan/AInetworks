from brian2 import *
import matplotlib


### Cell parameters ###
S       = 20000.* um2 # Area of membrane
gl      = 0.05 * msiemens/ cm2# Membrane time constant
c_m     = 1.0 * uF/cm2 # Capacitance
tau_ref = 2.5* ms # Refractory period
El      = -60 * mV # Leak potential
Vt      = -50 * mV # Spike Threshold
Vr      = -60 * mV # Spike Reset
Delta   = 2.5 * mV # Steepness of exponential approach to threshold 
tw      = 600. *ms # Adaptation



#Synapses
g_exc         =   6.  * nS# Excitatory conductance
g_inh         =   67. * nS# Inhibitory conductance
Ee            =  -70. * mV # Reversal potential (excitation)
Ei            =   0.* mV # Reversal potential (inhibition)
tau_exc       =   5. * ms # Synaptic time constant (excitatory)
tau_inh       =   10. * ms # Synaptic time constant (inhibitory)

ext_rate      = 300 * Hz                # Rate of the external source
#ext_input     = 0 * nA #external current

# Pick an electrophysiological behaviour
a, b= 0.001* usiemens, 0.04 * nA # Regular spiking (as in the paper)
# a, b= 0.001 * usiemens, 0.005 * nA # Bursting
# a, b= 0.001  *usiemens, 0 * nA # Fast spiking
#a, b = 0.02 *usiemens, 0 * nA #LTS Low Threshold Spiking
a, b = 0.04 *usiemens, 0 *nA # TC cells - more robust bursting activity and weaker spike-frequency adaptation
a, b = 0.08 *usiemens, 0.03 * nA #bursting activity in response to depolarising and hyperpolarising stimuli

### Equation for a Conductance-based IAF ####
eqs = Equations('''
dv/dt  = (gl*(El-v) + ge*(Ee-v)/ S +gi*(Ei-v)/ S + I_ext / S + gl*Delta*exp((v-Vt)/Delta) - wa/S)/c_m: volt
dwa/dt  = (a*(v - El)-wa)/tw : amp
dge/dt = -ge*(1./tau_exc) : siemens
dgi/dt = -gi*(1./tau_inh) : siemens
I_ext : amp                                             # external current
''')
P = NeuronGroup(1, eqs, threshold='v>Vt', refractory='tau_ref', reset="v=Vr; wa+=b", method='euler')
P.v = -60*mV

trace = StateMonitor(P, 'v', record=0)
spikes = SpikeMonitor(P)

stim = StateMonitor(P, 'I_ext', record=0)

P.I_ext = 0.25*nA
run(200 * ms)
P.I_ext = 0.*nA
run(50 * ms)
P.I_ext = 0*nA
run(750 * ms)
P.I_ext = -0.25*nA
run(400 * ms)
P.I_ext = 0*nA
run(400 * ms)

import seaborn
seaborn.set()


# We draw nicer spikes
vm = trace[0].v[:]
for t in spikes.t:
    i = int(t / defaultclock.dt)
    vm[i] = 20*mV

plot(trace.t / ms, vm / mV)
xlabel('time (ms)')
ylabel('membrane potential (mV)')
xlim(0,1000)
title("Regular spiking neuron")

figure()

plot(trace.t/ms, [0].rates[:]/ Hz)
title("Random rate stimulus")
xlabel('time (ms)')
ylabel('Rate (Hz)')


figure()
vlines(spikes.t/ms, spikes.i-0.5, spikes.i+0.5)
xlabel('time (ms)')
ylabel('NEURON ID')
title("Raster plot")
xlim(0, 1000)
ylim(0, 20)
#ylim(0, 40)
#ylim(0, 60)
#ylim(0, 80)
#ylim(0, 100)
show()
