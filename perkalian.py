def perkalian(a,b): 
    print(f'{a} x {b}',end=' = ')
    for i in range(a-1):
        total = a*b
        print(b,end=' + ')
    print(f'{b}',end=' = ')
    print(total)
    


perkalian(5, 6)