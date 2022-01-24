if __name__ == '__main__':
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
