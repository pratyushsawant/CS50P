def main():
    x=input("write a tweet: ")
    vowels=['A','E','I','O','U','a','e','i','o','u']
    for i in vowels:
        x=x.replace(i,"")
    print(x)

if __name__=="__main__":
    main()

