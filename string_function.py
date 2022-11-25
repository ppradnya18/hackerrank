strr = "ABCDCDC"
substring = "CDC"
# nes=""
# newCount =0
# for i in range(len(strr)):
#     if strr[i:len(substring)+i] == substring:
#         newCount+=1
# print(newCount)
    

count=0
for i in range(len(strr)):
    s =""
    for q in range(len(substring),len(substring)+i+1):
        s=strr[i:q]
        if s == substring:
            count+=1
          
print(count)
ls = []