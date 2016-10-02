from machinekit import hal
from machinekit import rtapi as rt

# we need a thread to execute the component functions
rt.newthread('main-thread', 1000000, fp=False)

# create the signal for connecting the components
input0 = hal.newsig('input0', hal.HAL_BIT)
input1 = hal.newsig('input1', hal.HAL_BIT)
output = hal.newsig('output', hal.HAL_BIT)

# and2 component
and2 = rt.newinst('and2', 'and2.demo')
and2.pin('in0').link(input0)
and2.pin('in1').link(input1)
and2.pin('out').link(output)
hal.addf(and2.name, 'main-thread')

# create remote component
rcomp = hal.RemoteComponent('anddemo', timer=100)
rcomp.newpin('button0', hal.HAL_BIT, hal.HAL_OUT)
rcomp.newpin('button1', hal.HAL_BIT, hal.HAL_OUT)
rcomp.newpin('led', hal.HAL_BIT, hal.HAL_IN)
rcomp.ready()

# link remote component pins
rcomp.pin('button0').link(input0)
rcomp.pin('button1').link(input1)
rcomp.pin('led').link(output)

# ready to start the threads
hal.start_threads()

# start haltalk server after everything is initialized
# else binding the remote components on the UI might fail
hal.loadusr('haltalk')
