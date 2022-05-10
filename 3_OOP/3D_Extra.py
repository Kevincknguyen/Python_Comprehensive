#MULTIPLE ARGUMENTS

def multipleArgs(arg,*args):
    print("Specific arg",arg,"+ other args packed as tuple",args)
    for a in args:
        print(a)

multipleArgs("Like so","One","Two","Three")