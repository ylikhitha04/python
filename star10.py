n=[1,2,5,1,4,3,6,5]
res={}
for num in n:
    if num not in res:
        res[num]=1
        else:
            res[num]=res[num]+1
            print(res)
            d={1:2,4:5,7:10}
            print(d.get(4))
