import math

cutoff_freq = 350*(10**6) # 350MHz
#cutoff_freq = 2.5*(10**9) TESTE OK!
Z0 = 50 # 50 Ohms

# ith element, order n filter
def Ci(i, n):
    return (1.0/(math.pi*cutoff_freq*Z0))*math.sin(((2*i-1)*math.pi)/(2*n))
def Li(i, n):
    return (Z0/(math.pi*cutoff_freq))*math.sin(((2*i-1)*math.pi)/(2*n))
def beta_l(L):
    return L*2*math.pi*cutoff_freq/Z0
def beta_c(C):
    return C*2*math.pi*cutoff_freq*Z0
def print_filter(n):
    for i in range(1, n+1):
        if i%2 == 1:
            print(f"CAPACITOR C_{i} = {Ci(i,n)} length = {beta_c(Ci(i,n))} rad = {beta_c(Ci(i,n))*180/math.pi} deg")
        else:
            print(f"INDUTOR L_{i} = {Li(i,n)} length = {beta_l(Li(i,n))} rad = {beta_l(Li(i,n))*180/math.pi} deg")

order = int(input())
print_filter(order)