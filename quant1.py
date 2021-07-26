from qiskit import *
from qiskit.tools.visualization import plot_histogram

print(qiskit.__qiskit_version__)


qr = QuantumRegister(2)
cr = ClassicalRegister(2)
circuit = QuantumCircuit(qr, cr)

print(circuit.draw())


print(circuit.h(qr[0]))
print(circuit.cx(qr[0], qr[1]))

print(circuit.draw(output='mpl'))

print(circuit.measure(qr, cr))

simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = simulator).result()
print(plot_histogram(result.get_counts(circuit)))

IBMQ.save_account('cd1a99404503d45a3902290c1b03750b261fe05368b504337a534b920642d39aef15c8f65e23a00ae563fd6deb62e68eb3e538538efb6bb764bd0a058a31f7fa')
IBMQ.load_account()
provider = IBMQ.get_provider('ibm-q')
qcomp = provider.get_backend('ibmq_santiago')
job = execute(circuit, backend=qcomp)
from qiskit.tools.monitor import job_monitor
job_monitor(job)
result = job.result()
plot_histogram(result.get_counts(circuit))

