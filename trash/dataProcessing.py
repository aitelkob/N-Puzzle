import sys
import argparse
from mapChecker import getData
from is_solvable import solve_or_nop

if __name__ == "__main__":
    parser = argparse.ArgumentParser()


    parser.add_argument("file", help="input file")
    parser.add_argument("-c", "--colors")
    parser.add_argument("-f", "--distance", default="manhattan", help="{hamming,manhattan,conflicts} heuristic function")
    parser.add_argument("-p", "--pretty")
    parser.add_argument("-v", "--visualisation")

    args = parser.parse_args()
    if args.distance in ("hamming", "manhattan", "conflicts"):
        distance = args.distance
    else:
        print("the distance can only be one of hamming,manhattan,conflicts")
        sys.exit(1)
    if args.file:
        data = getData(args.file)
        data.append(distance)
        if solve_or_nop(data[1], data[0]):
            data.append(True)
        else:
            data.append(False)

    #here i changed some things to fit well the list is [map, size, distance, solvable]
    