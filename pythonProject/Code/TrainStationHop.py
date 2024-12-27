class TrainStationHop:
    def OneHop(self ,dict):
        n = len(dict)
        onehop = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                onehop[i][j] = dict[i][j]
                for k in range(n):
                    if dict[i][k] ==1 and dict[k][j]==1:
                       onehop[i][j] = 1
        return onehop

    def TwoHop(self ,dict):
        n = len(dict)
        onehop = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                onehop[i][j] = dict[i][j]
                for k in range(n):
                    if dict[i][k] == 1 and dict[k][j] == 1:
                        onehop[i][j] = 1
        n = len(onehop)
        twohop = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                twohop[i][j] = onehop[i][j]
                for k in range(n):
                    if onehop[i][k] ==1 and onehop[k][j]==1:
                       twohop[i][j] = 1
        return twohop

if __name__=="__main__":
    dict=[[0,1,0,0],
          [0,0,1,0],
          [0,0,0,1],
          [0,0,0,0]]
    d = TrainStationHop()
    dict = d.OneHop(dict)
    for row in dict:
        print(row)
    print()
    dict = d.TwoHop(dict)
    for row in dict:
        print(row)