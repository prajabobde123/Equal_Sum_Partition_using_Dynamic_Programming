def subset(arr,n,sum):
    dp=[]
    for i in range(0,n+1):
        x=[]
        for j in range(0,sum+1):
            x.append(0)
        dp.append(x)
    for i in range(0,n+1):
        dp[i][0] = 1
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if(arr[i-1]<=sum):
                dp[i][j] = max(dp[i-1][j-arr[i-1]],dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][sum]


arr = [1,5,5,11]
n=len(arr)
s=sum(arr)
if(s%2!=0):
    print("Not possible")
else:
    x=subset(arr,n,s//2)
    if(x==1):
        print("Possible")
    else:
        print("Not possible")
