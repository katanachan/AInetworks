# AInetworks
<br> Paper referred to : http://www.ncbi.nlm.nih.gov/pubmed/19499317
<br> Self-sustained asynchronous irregular states and Up-Down states in thalamic, cortical and thalamocortical networks of nonlinear integrate-and-fire neurons.
<br> Alain Destexhe et al. J. Computational Neuroscience: 2009

<br>
For single neuron model:
<br> 9 different types of results were recorded in the simulation:
<br>1. For a hyperpolarising current:
<br>a = 0.001 microSiemens, b = 0.04 nanoAmpere, we get fast spiking
<br>a = 0.001, b = 0.005, we get bursting
<br>a = 0.001, b = 0, we get fast spiking
<br>If we consider a moderate value of a=0.02 and b=0, the model also displays spike frequency adaptation. However, this model also generates a rebound burst in response to hyperpolarising pulses. This behaviour is seen in cortical low-threshold spike.
<br>A further increase in parameter a leads to more robust bursting activity and weaker spike-frequency adaptation and strong rebound bursts. This is observed in a = 0.04 and b = 0.
<br> With larger values, a = 0.08 and b = 0.03, the model generated bursting activity in response to both depolarising and hyperpolarising stimuli. As seen in thalamus reticular neurons.

<br>For network model:
<br>To initiate activity, a number of randomly-chosen neurons (from 2% to 10% of the network) were stimulated by random excitatory inputs during the first 50 ms of the simulation. The mean frequency of this random activity was high enough (200–400 Hz) to evoke random firing in the recipient neurons. In cases where selfsustained activity appeared to be unstable, different parameters of this initial stimulation were tested.  It is
important to note that after this initial period of 50 ms, no input was given to the network and thus the activity states described here are self-sustained with no external input or added noise. The only source of noise was the random connectivity (also termed “quenched noise”).

<br>The plots for a network of neurons of 20, 40, 60, 80 and 100 neurons in the network are present in the networks/ folder. The Poisson Input was given at 200 ms at a rate of 300 Hz.
<br>Observations: As we increase the networks size, the mean firing rate increased and the irregulariy and asynchrony became higher.
