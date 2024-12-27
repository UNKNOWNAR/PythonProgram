class TrainRoutesGraph:
    def DirectRoutes(trains):
        # Step 1: Collect all unique stations
        stations = {}
        for t in trains.keys():
            stations[trains[t]['start']] = True
            stations[trains[t]['end']] = True

        # Step 2: Number of unique stations
        n = len(stations)

        # Step 3: Create a direct connection matrix
        direct = [[0 for _ in range(n)] for _ in range(n)]

        # Step 4: Map station names to indices
        stnindex = {}
        i = 0
        for s in stations.keys():
            stnindex[s] = i
            i += 1

        # Step 5: Populate the direct connection matrix
        for t in trains.keys():
            i = stnindex[trains[t]['start']]
            j = stnindex[trains[t]['end']]
            direct[i][j] = 1

        # Return the direct connection matrix
        return direct
if __name__=="__main__":
    trains = {
        'train1': {'start': 'A', 'end': 'B'},
        'train2': {'start': 'B', 'end': 'C'},
        'train3': {'start': 'C', 'end': 'A'},
        'train4': {'start': 'A', 'end': 'C'}
    }

    routes = TrainRoutesGraph()
    direct_matrix = routes.DirectRoutes(trains)

    # Print the resulting matrix
    print("Direct Routes Matrix:")
    for row in direct_matrix:
        print(row)