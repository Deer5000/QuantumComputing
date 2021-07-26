from qiskit import *


#A regular computer can solve this problem in 6 tries
#A Quantum computer can solve this in 1.

secretNumber = "100101"

circuit = QuantumCircuit(len(secretNumber)+1, len(secretNumber))
# circuit.h([0,1,2,3,4,5])
circuit.h(range(len(secretNumber)))
circuit.x(len(secretNumber))
circuit.h(len(secretNumber))

circuit.barrier()
for i, yesno in enumerate(reversed(secretNumber)):
    if yesno == '1':
        circuit.cx(i, len(secretNumber))


# circuit.cx(5,6)
# circuit.cx(3,6)
# circuit.cx(0,6)

circuit.barrier()
# circuit.h([0,1,2,3,4,5])
circuit.h(range(len(secretNumber)))

circuit.barrier()
# circuit.measure([0,1,2,3,4,5], [0,1,2,3,4,5])
circuit.measure(range(len(secretNumber)), range(len(secretNumber)))
                
                
simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = simulator, shots = 1).result()
counts = result.get_counts()
print(counts)

circuit.draw(output= 'mpl')