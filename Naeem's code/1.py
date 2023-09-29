n=input().strip()
arr=[[''for i in range(1000) for i in range(1000)]]
count=0
column=0
r=0
l=0
row=0
for i in range(len(n)):
    if n[i]=='L':
        l+=1
        arr[row][column]='L'
    else:
        r+=1
        arr[row][column]='R'
    colum+=1
    if(r==1):
        count+=1
        column=0
        row+=1
        r=0
        l=0

        prints(count)

        for i in range(1000):
            if ar[i][0]=='L' or arr[i][0]=='R':
                print("".join(arr[i]))
                count-=1
            if count==0:
                break