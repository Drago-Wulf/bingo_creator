import sys, csv, argparse, random

parser = argparse.ArgumentParser(description='Takes a txt file of bingo entries and outputs a board')
parser.add_argument("--file", type=str, default='skyrim.txt')
parser.add_argument("--columns", type=int, default=5)
parser.add_argument("--rows", type=int, default=5)


def main(csv_file,columns,rows):
    # Initialize Bingo Array to be able to create the resultant Bingo Board
    bingo_array = [[0]*columns]*rows
    
    #Initialize Entry list for bingo with the "Abwa Spot".  This is to make sure that we have a place to store all data from the CSV
    bingo_entry_list = list((["abwa Spot"]))

    # Open the text file that stores all entries to be a part of the bingo board and save entries to the entry list
    with open(csv_file, newline='') as file:
        bingo_entries = csv.reader(file, delimiter = ' ', quotechar = '|')
        for row in bingo_entries:
            bingo_entry_list.append(row.pop())
    
    #Shuffle the entries to make sure that the board is sufficently randomized.  This makes sure that we are not using the order of the list
    random.shuffle(bingo_entry_list)

    for column in range(columns):
        bingo_row = [0] * rows
        for row in range(rows):
            bingo_entry = bingo_entry_list.pop()
            bingo_row[row] = bingo_entry
        bingo_array[column] = bingo_row

    print(bingo_array)
    
        
            


if __name__=="__main__":
    args = parser.parse_args()
    main(args.file,args.columns,args.rows)