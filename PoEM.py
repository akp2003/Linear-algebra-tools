#Write the matrix as Product of Elementary Matrices
#This code is written by Arshak Parsa
from sympy.matrices import Matrix,eye
from sympy import Rational,pprint
d=[]
def swap_rows(M,a,b):
	row=M[b,:]
	M[b,:]=M[a,:]
	M[a,:]=row
	return M

def sr(M,a,b):
	#print("swap")
	swap_rows(M,a,b)
	I=eye(M.shape[0])
	swap_rows(I,a,b)
	d.append(I)
	#pprint(M)

def mr(M,a,c):
	#print("mr")
	M[a,:]*=c
	I=eye(M.shape[0])
	I[a,:]*=Rational(1,c)
	d.append(I)
	#pprint(M)

def amr(M,a,b,c):
	#print("amr")
	M[a,:]+=M[b,:]*c
	I=eye(M.shape[0])
	I[a,:]+=I[b,:]*(-c)
	d.append(I)
	#pprint(M)
	
def PoEM(M):#n×m
	if M.det()==0:
		print("Impossible!")
		return
	n,m=M.shape
	k=0
	for i in range(m):
		j=k
		while (M[j,i]==0):
			j+=1
		
		
		if (M[j,i]!=0):
			if (M[j,i]!=1):
				mr(M,j,Rational(1,M[j,i]))
			if (j!=k):
				sr(M,j,k)
			k+=1
			
		
		for p in range(n):
			if p!=j and (M[p,i]!=0):
				amr(M,p,j,-M[p,i])
	

A=Matrix([
[1,2,4],
[0,1,5],
[1,0,3]
])

pprint(A)
PoEM(A.copy())

print("end")
x=eye(3)
d=d[::-1]
for i in d:
	pprint(i)
	x=i*x
pprint(x)
print(A==x)
