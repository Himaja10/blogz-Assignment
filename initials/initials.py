def get_initials(fullname):
    # some code here
    namelist = fullname.split()
    initials = ""
    for aname in namelist:
        initials = initials + aname[0].upper()
    return initials

   
    

def main():
    # some more code here (input and print statements)
    fullname = raw_input("Please Enter Your Name: ")
    initials = get_initials(fullname)
    print("The initials of '" + fullname + "' are " + initials)
    

if __name__ == '__main__':
    main()
