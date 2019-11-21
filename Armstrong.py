def dinesh(p):
  sum=0
  temp=p
  while temp >0:
    digit =temp % 10
    sum+= digit**3
    temp //=10
  if p==sum:
    print(p," it is armstrong number")   
  else:
    print(p,"it is not an armstrong number")
dinesh(153)