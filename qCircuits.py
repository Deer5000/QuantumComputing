from qiskit import *

from qiskit.tools.visualization import plot_bloch_multivector

#Statevector simulator
circuit = QuantumCircuit(1,1)
circuit.x(0)
simulator = Aer.get_backend('statevector_simulator')
result = execute(circuit, backend = simulator).result()
statevector = result.get_statevector()
print(statevector)
print(circuit.draw(output='mpl'))

plot_bloch_multivector(statevector)


circuit.measure([0], [0])
backend = Aer.get_backend('qasm_simulator')
results = execute(circuit, backend = backend, shots = 1024).result()
counts = results.get_counts()
from qiskit.tools.visualization import plot_histogram
plot_histogram(counts)




#Unitary simulator
circuit = QuantumCircuit(1,1)
circuit.x(0)
simulator = Aer.get_backend('unitary_simulator')
result = execute(circuit, backend = simulator).result()
unitary = result.get_unitary()
print(unitary)
print(circuit.draw(output='mpl'))



#4 different ways to talk about a quantum gate.


# 1.) Bra-Ket
#      x|0> = |1>   
#      x|1> = |0>

# 2.) Matrix

#         |0  1|      |1|        |0|
#                 *        =     
#         |1  0|      |0|        |1|


# 3.) Bloch Sphere

#     Plot out state vector that results from applying
#     that gate on a bloch vector.

# 4.) Measurement

#         running circuit through a measurement and find out what the
#         measurement outcomes are.
