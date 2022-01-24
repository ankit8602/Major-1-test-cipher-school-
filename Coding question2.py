Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> if __name__ == '__main__':
    l=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        l.append([name,score])
    
    l.sort(key=lambda l:l[1])
    
    second_lowest=[]
    for i in range(len(l)):
        if l[i][1]!=l[0][1]:
            second_lowest.append(l[i][0])
            for j in range(i+1,len(l)):
                if l[j][1]==l[i][1]:
                    second_lowest.append(l[j][0])
                else:
                    break
            break        
           
                   
            
        else:
            continue
           

    second_lowest.sort()
    for i in second_lowest:
        print(i)