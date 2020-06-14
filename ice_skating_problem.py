N=10
dirs=[[0,1],[1,0],[0,-1],[-1,0]] # derictions

def dive(arr,i,j):
    arr[i][j]=0
    for d in dirs:
        a = i + d[0]
        b = j + d[1]
        if arr[i][j] == 0:
            while a>=0 and a<N and b>=0 and b<N and arr[a][b]!=1:
                a+=d[0]
                b+=d[1]
        if a>=0 and a<N and b>=0 and b<N and arr[a][b]==1:
            dive(arr,a,b)



def main():  # main method
    n = int(input())
    arr = [[0 for j in range(N)] for i in range(N)]

    for i in range(n):
        a,b=(map(int,input().split()))
        arr[a][b]=1

    res=-1
    for i in range(1,N):
        for j in range(1,N):
            if arr[i][j]==1:
                res+=1
                dive(arr,i,j)

    print(res)

if __name__ == '__main__': main()  # call main method