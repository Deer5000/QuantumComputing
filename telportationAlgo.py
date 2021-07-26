from qiskit import *


circuit = QuantumCircuit(3, 3)

# Empty Circuit
circuit = QuantumCircuit(3, 3)
# %matplotlib inline
circuit.draw(output = 'mpl')


# circuit with an x gate
circuit.x(0)
circuit.barrier()
circuit.draw(output='mpl')


# Enatnglement between q1 and q2 using hadamard gate and controlled xgate.
circuit.h(1)
circuit.cx(1,2)
circuit.draw(output='mpl')


# q1 and q2 are now entangled.
# The rest of the teleport protocol dictates that we apply the following two gates.

#controlled x-gate from q0 to q1
circuit.cx(0,1)
#hadamard gate on q0
circuit.h(0)
circuit.draw(output='mpl')


#There's one more missing aspect to the teleportation circuit.
#Which is to do two measurements. They are going to be on q0 and q1.

circuit.barrier()
circuit.measure([0,1], [0,1])
circuit.draw(output='mpl')


#To complete the teleportation protocol I must add two more gates.

circuit.barrier()
#controlled x from q1 to q2
circuit.cx(1, 2)
#controlled z from q0 to q2
circuit.cz(0, 1)

circuit.draw(output='mpl')


# The state of the first quibit(on the left) has been 
# teleported over to the second quibit(on the right).
# We can verify this by applying ameasurement on Q2 and seeing the outcomes.

circuit.measure(2,2)
simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = simulator, shots = 1024).result()
counts = result.get_counts()
from qiskit.tools.visualization import plot_histogram
plot_histogram(counts)


#Extra Verification
print(counts)