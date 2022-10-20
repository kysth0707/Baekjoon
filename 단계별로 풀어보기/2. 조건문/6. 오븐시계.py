h,m=map(int,input().split())
t=int(input())
RealTime = h * 60 + m + t
RealTime = RealTime % (24*60)
print(f"{RealTime // 60} {RealTime % 60}")