while True:
    try:
        n = int(input())
        
        def can(n):
            if n == 0:
                return '-'
            return can(n-1) + ' ' * 3 ** (n-1) + can(n-1)
        
        print(can(n))
    
    except EOFError:
        break