def okay(arr,n):
        k=[]
        j=n-1
        l=[-1]
        for i in range(n):
             k.append(arr[i])
        k.pop()
        print(k)
        print(arr)
        while k:
            s=k[-1]
            if arr[j]<s:
                j=j-1
            elif arr[j]>s:
                l.append(arr[j])
                j=j-1
                k.pop()
            elif arr[j]==s:
                o=-1
                l.append(o)
                k.pop()
                j=j-1
        return l
print(okay([1,3,2,4],4))