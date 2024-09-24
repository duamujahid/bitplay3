def swap(a, b):
    print("The container1 has", a)
    print("The container2 has", b)

    a = a^b
    b = a^b
    a = a^b

    print("The container1 after swapping has", a)
    print("The container2 after swapping has", b)

c1 = int(input("Enter a number for container1"))
c2 = int(input("Enter a number for container2"))
swap(c1, c2)