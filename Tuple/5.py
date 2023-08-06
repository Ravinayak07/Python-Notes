tuple1=(10,35,8)
tuple2=(9,10,8)
for x in range(0,3):
    for y in range(0,3):
        if tuple1[x]>tuple2[y]:
            print("%i is greater than"%tuple1[x] ,tuple2[y])
        elif tuple1[x]<tuple2[y]:
            print("%i is less than"%tuple1[x],tuple2[y])
        else:
            print("%i equal to "%tuple1[x],tuple2[y])
          
        