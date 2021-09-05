# chapter 03 pratice project
# functiob collatz

def collatz(n):
    
    if n==0:
        print('Error')
       
        
    while n!=1 and n!=0:
        
        if n%2==0:
            n=n//2
        else:
            n=n*3+1
        
        print(n)
