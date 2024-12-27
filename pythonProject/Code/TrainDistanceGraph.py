class TrainDistanceGraph:
    def OneHopDistance(self,directdist):
        n = len(directdist)
        onehopdist = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                onehopdist[i][j] = directdist[i][j]
                for k in range(n):
                    if directdist[i][k]>0 and directdist[k][j]>0:
                        newdist = directdist[i][k]+directdist[k][j]
                        if onehopdist[i][j]>0:
                            onehopdist[i][j] = min(onehopdist[i][j],newdist)
                        else:
                            onehopdist[i][j] = newdist
        return onehopdist

    def DirectDistance(self,trains):
        # Step 1: Collect all unique stations
        stations = {}
        for t in trains.keys():
            stations[trains[t]['start']] = True
            stations[trains[t]['end']] = True

        # Step 2: Number of unique stations
        n = len(stations)

        # Step 3: Create an edge-labelled graph (direct distance matrix)
        directdist = [[0 for _ in range(n)] for _ in range(n)]

        # Step 4: Map station names to indices
        stn2idx = {}
        idx = 0
        for s in stations.keys():
            stn2idx[s] = idx
            idx += 1

        # Step 5: Populate the direct distance matrix
        for t in trains.keys():
            i = stn2idx[trains[t]['start']]
            j = stn2idx[trains[t]['end']]

            # If no direct distance exists, set it
            if directdist[i][j] == 0:
                directdist[i][j] = trains[t]['distance']
            else:
                # Update the distance to the minimum
                directdist[i][j] = min(directdist[i][j], trains[t]['distance'])

        # Return the direct distance matrix
        return directdist
if __name__=="__main__":
    trains = {
        'train1': {'start': 'A', 'end': 'B', 'distance': 50},
        'train2': {'start': 'B', 'end': 'C', 'distance': 70},
        'train3': {'start': 'C', 'end': 'A', 'distance': 120},
        'train4': {'start': 'A', 'end': 'B', 'distance': 40},  # Shorter route A → B
        'train5': {'start': 'A', 'end': 'C', 'distance': 90}
    }

    distance = TrainDistanceGraph()
    direct_distance_matrix = distance.DirectDistance(trains)

    # Print the resulting distance matrix
    print("Direct Distance Matrix:")
    for row in direct_distance_matrix:
        print(row)

    print()

    direct_onehop_distance_matrix = distance.OneHopDistance(direct_distance_matrix)

    # Print the resulting distance matrix
    print("Direct Distance Matrix:")
    for row in direct_onehop_distance_matrix:
        print(row)