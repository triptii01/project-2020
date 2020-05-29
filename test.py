#median of the three numbers
def median(a,b,c):
      if a<b and a>c:
          if b>c or c>b:
             print(a)
      else:
          if b<c and b>a:
               if c>a or a>c:
                   print(b)
          else:
               print(c)

median(32,88,60)
median(13,130,17)
median(32,65,32)

