from random import shuffle,randint

def roullete(n):
   if n <= 0 or n>= 5 or type(n) != int:
    return 'This game cant be real'
   bullet_index  = 0
   bullets = []
   for el in range(n):
        if len(bullets) >= 6:
          break
        if bullet_index > n-1:
           bullets.append(0)
        
        else:       
         bullets.append(1)
         bullet_index += 1
   shuffle(bullets)
   k = 0
   while True:
    try:
     n = input('enter 1 for countinue or 2 for spin: ')
     if n == '1':
      
      if x[k] == 1:
        return 'boom'
   
     elif n == '2':
      shuffle(bullets)
      k = 0 
     
     else:
      k += 1
      pass
    except Exception:
      print('Something wrong !')

print(roullete(4))
 