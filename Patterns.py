//Pattern7
5
        *         
      * * *       
    * * * * *     
  * * * * * * *   
* * * * * * * * * 
n = int(input())
for i in range(n):
    for j in range(0, n-i-1):
        print(' ', end = ' ')
    for k in range(0, 2*i+1):
        print('*', end = ' ')
    for l in range(0, n-i-1):
        print(' ', end = ' ')
    print()

//Pattern8
5
        *         
      * * *       
    * * * * *     
  * * * * * * *   
* * * * * * * * * 
n = int(input())
for i in range(n):
    for j in range(0, i):
        print(' ', end = ' ')
    for k in range(0, 2*n-(2*i+1)):
        print('*', end = ' ')
    for l in range(0, i):
        print(' ', end = ' ')
    print()

//Pattern9
5
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
n = int(input())
for i in range(1, 2*n-1+1):
    stars = i
    if i > n:
        stars = 2*n - i
    for j in range(1, stars+1):
        print('*', end=' ')
    print()
    
    
