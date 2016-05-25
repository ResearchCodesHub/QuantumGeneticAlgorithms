# QuantumGeneticAlgorithms

Genetic algorithms (GAs) are a class of evolutionary algorithms inspired by Darwinian natural selection.  They are popular heuristic optimisation methods based on simulated genetic mechanisms, i.e. mutation, crossover, etc. and population dynamical processes such as reproduction, selection, etc. Over the last decade, the possibility to emulate a quantum computer (a computer using quantum-mechanical phenomena to perform operations on data) has led to a new class of GAs known under the name of ‘Quantum Genetic Algorithms’. In this repository we present three programs that illustrate different versions of quantum evolutionary algorithms: QGA, HGA and RQGA.

Quantum Genetic Algorithm (QGA) is a QGA that can be used for the purposes of education and research. 
QGA is applied in a simple optimization problem: Let  f(x)=abs(x-5/2+sin(x)) be a function that takes
values in the range 0<=x<=15. Within this range f(x) has a maximum value at x=11 (binary value is equal to 1011).

Hybrid Genetic Algorithm (HGA) is a GA that combines quantum operators (rotation, measure, quantum chromosomes, etc.) 
with classical genetic operators (crossover and mutation).It  can be used for the purposes of education and research.
HGA is applied in a simple optimization problem: Let  f(x)=abs(x-5/2+sin(x)) be a function that takes values in the 
range 0<=x<=15. Within this range f(x) has a maximum value at x=11 (binary value is equal to 1011).

Reduced Quantum Genetic Algorithm (RQGA) is a program in Python showing how to implement a 'true' quantum genetic algorithm
based on a fitness quantum gate and Grover's search algorithm. It  can be used for the purposes of education and research. 
RQGA is applied in a simple optimization problem: Let  f(x)=abs(x-5/2+sin(x)) be a function that takes values in the range
0<=x<=15. Within this range f(x) has a maximum value at x=11 (binary value is equal to 1011). The program should be understood as a thinker toy, illustrating the ideas taken from the papers cited below.

REFERENCES

Udrescu, M.; Prodan, L.; Vladutiu, M. Implementing  quantum genetic algorithms: a solution based on Grover’s algorithm.
CF '06 Proceedings of the 3rd conference on Computing frontiers, Ischia, Italy, 3-5 May, 2006; pp. 71-82.

Goswami, D.; Kumar, N. Quantum algorithm to solve a maze: converting the maze problem into a search problem.
arXiv:1312.4116v1 [quant-ph]. 2013.

Sofge, D.A. Prospective algorithms for quantum evolutionary computation. Proceedings of the Second Quantum Interaction
Symposium (QI-2008), College Publications, Oxford, UK, 26-28 March, 2008. Available online: http://arxiv.org/ftp/arxiv/papers/0804/0804.1133.pdf

Malossini, A.; Blanzieri, E.; Calarco, T. Quantum genetic optimization. IEEE Transactions on Evolutionary Computation.
2008, 12, 231-241.

Ahuja, A.; Kapoor, S. A quantum algorithm for finding the maximum. arXiv:quant-ph/9911082v1. 1999.
