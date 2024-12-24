# def interpreter():
#     while True:
#         try:
#             expression=input("enter your expression")
#             if expression.lower()=="exit":
#                 print("Goodbye")
#                 break

#             result=eval(expression)
#             print(result)
#         except Exception as e:
#             print("wrong input")
#Above code is correct but doesnt satisfy the condition

expression=input("enter A expression")
x,y,z=expression.split(" ")
newx=float(x)
newz=float(z)
if y=="+":
    print(newx+newz)
elif y=="-":
    print(newx-newz)
elif y=="*":
    print(newx*newz)
elif y=="/":
    print(newx/newz)
else:
    print("Wrong input")
