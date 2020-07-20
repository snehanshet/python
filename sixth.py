largest = None
smallest = None
while True:
    n = input("Enter a number: ")
    if n == "done" :
        break
    try:
        num=int(n)
    except:
        print('Invalid input')
        continue
    if largest is None:
        largest = num
    elif num>largest:
        largest=num
    if smallest is None:
        smallest=num

    elif num<smallest:
        smallest=num


print("Maximum is", largest)
print("Minimum is", smallest)
