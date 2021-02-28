def swap_case(s):
    x = ''
    for i in s: #iterate one by one through the string
        if i.isupper == True:
            i = i.lower() #if it has upper case then change it to lower 
        else:
            i = i.upper()
        x = ''.join(i) #put this element in the empty string. with join function
    return x
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
