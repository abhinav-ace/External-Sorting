from collections import deque
import os

#Source File
file="D:\\External Sorting\\Copy of temp_words_1.txt"

extra=[]

filecount=1
linecount=0
maxlines=10000000


#Splitting the file into smaller files with number maxlines. 
reader=open(file)
line=reader.readline()

while line!="":
    if linecount==0:
        addcurr="D:\\External Sorting\\"+str(filecount)+".txt"
        extra.append(addcurr)
        writer=open(addcurr,"w")   
        filecount+=1
        
    writer.write(line)
    linecount+=1
    
    if linecount==maxlines:
        linecount=0
        writer.close()
        
    line = reader.readline()
writer.close()

print("DONE SPLITTING")


#Sorting individual splits
for i in range(1,filecount):
    arr=[]
    file="D:\\External Sorting\\"+str(i)+".txt"
    reader=open(file)
    addcurr="D:\\External Sorting\\"+str(i)+"sorted.txt"
    extra.append(addcurr)
    writer=open(addcurr,"w")
    line=reader.readline()
    
    while line!='':
        arr.append(line)
        line=reader.readline()
        
    arr.sort(key= lambda x:x.lower())
    
    for i in arr:
        writer.write(i)
    writer.close()    
     
print("SPLITS HAVE BEEN SORTED")
        
        
#Final Merge Step
arr=[0]*filecount
reader=[0]*filecount

for i in range(filecount):
    arr[i]=deque([])
    
writer=open("D:\\External Sorting\\FinalSorted.txt","w")
for i in range(1,filecount):
    reader[i]=open("D:\\External Sorting\\"+str(i)+"sorted.txt")
    for line in reader[i]:
        if len(arr[i])<1000000:
            arr[i].append(line)
        else:
            break
            
while arr!=[deque([])]*filecount:
    minval="zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
    ind=0
    for i in range(1,filecount):
        if len(arr[i])!=0 and arr[i][0]<minval:
            minval=arr[i][0]
            ind=i
            
    if ind!=0:
        val=arr[ind].popleft()
        writer.write(val)
        
        if len(arr[ind])==0:
            for line in reader[ind]:
                if len(arr[ind])<1000000:
                    arr[ind].append(line)
                else:
                    break
                    

for i in extra:
    os.remove(i)
    
    
print("SUCCESSFULLY SORTED")
