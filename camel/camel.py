def main():
    camel_case=input("enter:")
    snake_case=""
    for char in camel_case:
        if char.isupper():
            snake_case+="_" + char.lower()
        else:
            snake_case+=char.lower()
    print(snake_case)
if __name__=="__main__":
    main()



