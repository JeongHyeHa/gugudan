def multi(start, end):
    for i in range(1,10):
        for j in range(start, end+1):
            print("{} x {} = {}".format(j, i, i*j), end="\t")
        print("")
    print("")


row = int(input("한 행에 출력할 구구단의 개수를 입력하세요: "))
stage = int(input("최대 출력할 단 수를 입력하세요: "))

if row>0 and stage>0:
    #구구단 총 행 개수 출력    
    n = stage//row
    if stage%row !=0:
        n += 1
    
    for i in range(0, n):   #i=0,1
        end = row*(i+1)
        if end>stage:
            end = stage
        multi(row*i+1, end)

elif row==0 or stage == 0:
    print("%d" % 0)