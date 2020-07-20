#smallest so far
smallest_so_far=657
print 'before',smallest_so_far
for num in [4,67,89,43,7,98,0,657,1,90]:
    if num<smallest_so_far:
        smallest_so_far=num
    print smallest_so_far,num
print 'after',smallest_so_far


#largest so far
largest_so_far=-1
print 'before',largest_so_far
for num in [4,67,89,43,7,98,0,657,1,90]:
    if num>largest_so_far:
        largest_so_far=num
    print largest_so_far,num
print 'after',largest_so_far
