def kiem_tra_palindrome(penguin):
    i=0
    j=len(penguin)-1
    a=True
    while i<j:
        if penguin[i]!=penguin[j]:
            a=False
            break
        i+=1
        j-=1
       
    return(a)
penguin=input()
end=kiem_tra_palindrome(penguin)
if end:
    print(True)
else:print(False)