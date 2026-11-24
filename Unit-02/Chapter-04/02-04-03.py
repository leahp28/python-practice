print("Enter the height of the str(3) \
siblings in cm first Alex, then Ben,\
then Chloe")
A = int(input())
B = int(input())
C = int(input())

if A >= B and A >= C:
    print(A)
elif B >= A and B >= C:
    print(B)
elif C >= A and C >= B:
    print(C)