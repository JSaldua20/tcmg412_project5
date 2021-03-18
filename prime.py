def prime_response():
    num = int(input('Input: '))
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                resp = False
                break
            else:
                resp = True
    else:
        resp = False
    
    return "{num} is Prime: {resp}"
