def swap(a, b):
    print("container1 has", a)
    print("container2 has", b)

    a = a + b
    b = a - b
    a = a - b

    print("container1 now has", a)
    print("container2 now has", b)

c1 = int(input("Enter a number for container1 :"))
c2 = int(input("Enter a number for container2 :"))
swap(c1, c2)