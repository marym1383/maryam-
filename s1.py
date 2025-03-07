def main():
    usernames=[]

    while True:
        username=input("pleas enter a username(for end enter num -1):")

        if username=="-1":
            break
        if username.isdigit():
            usernames.append(int(username))

    usernames.sort()

    print("Sorted num usernames in ascending order:")
    for username in usernames:
        print(username)

if __name__== "__main__":
    main()
    
