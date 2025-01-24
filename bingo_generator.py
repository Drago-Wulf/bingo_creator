import sys, csv, argparse, random

parser = argparse.ArgumentParser(description='Takes a json file of bingo entries and outputs a board')
parser.add_argument("--file", type=str, default='skyrim.json')
parser.add_argument("--columns", type=int, default=5)
parser.add_argument("--rows", type=int, default=5)


def main(csv_file,columns,rows):
    bingo_array = [[0]*columns]*rows
    bingo_entry_list = list((["abwa Spot"]))
    with open(csv_file, newline='') as file:
        bingo_entries = csv.reader(file, delimiter = ' ', quotechar = '|')
        for row in bingo_entries:
            bingo_entry_list.append(row)
    random.shuffle(bingo_entry_list)
    for row in range(rows):
        for column in range(columns):
            bingo_entry = bingo_entry_list.pop(0)
            bingo_array[row][column] = bingo_entry
            print(bingo_entry_list)
    print(bingo_array)
    
        
            


if __name__=="__main__":
    args = parser.parse_args()
    main(args.file,args.columns,args.rows)