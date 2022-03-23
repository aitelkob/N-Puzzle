from distance_algo import manhattan_distance , hamming_distance ,euclidean_distance

def heuristic(state,dist_type):
    distance = 0
    for i in range(N):
        for j in range(N):
            num = state[i][j]
            if num != GOAL_STATE[i][j] and num != 0:
                goal = GLOBAL_STATE_DICT[num]
                if (dist_type == 'M'):
                    distance += manhattan_distance((i, j), goal)
                elif (dist_type == 'H'):
                    distance += hamming_distance((i, j), goal)
                else:
                    distance += euclidean_distance((i, j), goal)
    return distance
