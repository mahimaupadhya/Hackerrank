if __name__ == '__main__':
    si = input()
    s=type(si)
    for c in [s.isalnum,s.isalpha,s.isdigit,s.islower,s.isupper]:
        print(any( c(b) for b in si))
    
