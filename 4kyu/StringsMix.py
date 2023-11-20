def mix(s1, s2):
    s = "qwertyuiopasdfghjklzxcvbnm"
    dic = {}
    for i in s:
       dic[i] =[0,0]
    for i in s1:
        if i in s:
            dic[i][0] += 1
    for i in s2:
        if i in s:
            dic[i][1] += 1
    lis = sorted(list(s),key=lambda x: max(dic[x]))
    for i in range(26):
        temp = dic[lis[i]]
        if temp[0]>temp[1]:
            lis[i] = "1:"+temp[0]*lis[i]
        elif temp[0] < temp[1]:
            lis[i] = "2:"+temp[1]*lis[i]
        elif temp[0]==0:
            lis[i] = ""
        else:
            lis[i] = "3:"+temp[0]*lis[i]
    lis = sorted([i for i in lis if (i !="" and len(i)>3)], key = lambda x:(-len(x),x[0],x[2]))
    lis = [i.replace("3","=") for i in lis]
    return "/".join(i for i in lis)