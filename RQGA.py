#########################################################
#                                                       #
#   REDUCED QUANTUM GENETIC ALGORITHM (25.05.2016)      #
#                                                       #
#                 R. Lahoz-Beltra                       #
#                                                       #    
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR "AS IS" AND   #
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT #
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY #
# AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.  #
# THE SOFWTARE CAN BE USED BY ANYONE SOLELY FOR THE     #
# PURPOSES OF RESEARCH AND EDUCATION.                   #
#                                                       #
#########################################################
import math
import numpy as np

#########################################################
# VARIABLES ALGORITHM AND PARAMETERS                    #
#########################################################
n=4;
fitness = np.empty([2**n])
cutoff=99;

#########################################################
# CONVERTS A NON-SUPERPOSED BINARY STATE TO             #
# |psi> REGISTER IN SUPERPOSITION                       #  
#########################################################
def bin2dec(string_num):
    return str(int(string_num, 2))

def dec2vec(dec,n):
    vec=np.zeros((2**n,1))
    vec[dec,0]=1;
    return vec
    
def psi(string_num):
    dec=bin2dec(string_num)
    return dec2vec(dec,len(string_num))

#########################################################
# CREATES AN N-BIT HADAMARD MATRIX                      #
#########################################################
def hadamard(n):
    r2=math.sqrt(2.0)
    H1=np.array([[1/r2,1/r2],[1/r2,-1/r2]])
    if n==1:
        H=H1
    else:
        H=1;
        i=1;
        for i in range(1,n+1):
            H=np.kron(H,H1)
    return H

#########################################################
# FITNESS QUANTUM GATE                                  #
#########################################################  
def bin(i):
    if i == 0:
        return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i >>= 1
    return s

def Fitness_evaluation():
    for i in range(0,2**n):
        fitness[i]=0
        
 #########################################################
 # Define your problem in this section. For instance:    #
 #                                                       #
 # Let f(x)=abs(x-5/2+sin(x)) be a function that takes   #          
 # values in the range 0<=x<=15. Within this range f(x)  #
 # has a maximum value at x=11 (binary is equal to 1011) #                   
 #########################################################
    for i in range(0,16):
        x=int(bin(i),2)
        # replaces the value of x in the function f(x)
        y=np.fabs((x-5)/(2+np.sin(x)))
        # the fitness value is calculated below:
        # (Note that in this example is multiplied
        # by a scale value, e.g. 100)
        fitness[i]=y*100

 #########################################################
    # Best chromosome selection
    the_best_chrom=0;
    fitness_max=fitness[1];
    for i in range(0,16):
        if fitness[i]>=fitness_max:
            fitness_max=fitness[i]
            the_best_chrom=i
        cutoff=the_best_chrom
    return cutoff

#########################################################
# ORACLE:UNITARY F-CONDITIONAL INVERTER FOR N BITS INPUT#
#########################################################  
def U_Oracle(n):
    zero_mat=np.zeros((2**n,2**n))
    i=0;
    for i in range(0,2**n):
    ###########################
    # Define here your oracle #
    ###########################
        if i==Fitness_evaluation():
            O=1
        else:
            O=0
    # Inverter
        zero_mat[i,i]=(-1)**O
    return zero_mat

#########################################################
# GROVER'S DIFFUSION OPERATOR                           #
#########################################################
# Inversion about average
def ia(n):
    ia_mat=2*np.ones(2**n)/(2**n)
    ia_mat=ia_mat-np.identity(2**n)
    return ia_mat

#########################################################
# GROVER'S MAXIMUM ITERATIONS                           #
#########################################################
def maxiter(n):
    max_iter=(np.pi/4)*math.sqrt(2**n)
    return max_iter

#########################################################
# REDUCED QUANTUM GENETIC ALGORITHM                     #
#########################################################
def RQGA(n, string_num):
    psi_=psi(string_num)
    H=hadamard(n)
    psi_=np.dot(H,psi_)
    print(psi_)
    print()
    iter=np.trunc(maxiter(n))
    iter=int(round(iter))
    for i in range (1,iter):
        U_O=U_Oracle(n)
        print(U_O)
        print()
        psi_=np.dot(U_O,psi_)
        print(psi_)
        print()
        D=ia(n)
        psi_=np.dot(D,psi_)
    print(psi_)

#########################################################
#                                                       #
# MAIN PROGRAM                                          #
#                                                       #
#########################################################
print("REDUCED QUANTUM GENETIC ALGORITHM")
input("Press Enter to continue...")
RQGA(4,'0000');




 



    
    



