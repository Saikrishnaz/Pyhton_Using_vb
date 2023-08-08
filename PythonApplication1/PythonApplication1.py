# program to sort an list using bubble shorting method 
def bub_short(list):
    print("List Before Sorting : \n")
    print(L1,"\n")
    for i in range(len(L1)) :
        print(f"phase :{i+1} ")
        print(L1)
        for j in range(len(L1)-1):
            if L1[j]>L1[j+1] :            # swaping method         
                L1[j]=L1[j]+L1[j+1]         # 74 = 31 + 43
                L1[j+1]=L1[j]-L1[j+1]       # 31 = 74 - 43
                L1[j]=L1[j] - L1[j+1]       # 43 = 74 - 31
            #print(L1)
    print("List After Sorting :\n")
    print(L1)
L1=[58,74,85,88,94,31,43,57,25,48,53,39,23,42,101]
bub_short(L1)
    