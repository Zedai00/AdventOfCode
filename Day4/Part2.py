from os import remove
import sys


def main(file):
    numbers = file.readline().strip().split(',')
    file = clean(file)
    boards = createBoards(file)
    marked = createMarked(boards)
    board, number = checkBoards(boards, numbers, marked)
    Score = score(boards, board, number, marked)
    print(Score)


def score(boards, board, number, marked):
    score = 0
    for i in range(len(boards[board])):
        for j in range(len(boards[board])):
            if marked[board][i][j] != True:
                score += int(boards[board][i][j])
    return score * number


def checkBoards(boards, numbers, marked):
    currentBoard = []
    for num in numbers:
        for b in range(len(boards)):
            rows, cols = 0, 0
            for i in range(len(boards[b])):
                for j in range(len(boards[b][i])):
                    rows = boards[b][i][j]
                    if boards[b][i][j] == num:
                        marked[b][i][j] = True
                    cols = boards[b][j][i]
                    if boards[b][j][i] == num:
                        marked[b][j][i] = True
        for b in range(len(boards)):
            for i in range(len(boards[b])):
                rows, cols = 0, 0
                for j in range(len(boards[b][i])):
                    if marked[b][i][j] == True:
                        rows += 1
                    if marked[b][j][i] == True:
                        cols += 1
                    if rows == 5 or cols == 5:
                        if b not in currentBoard:
                            currentBoard.append(b)
                        if len(currentBoard) == len(boards):
                            return currentBoard[-1], int(num)
                        break


def createMarked(boards):
    marked = []
    for board in range(len(boards)):
        marked.append([])
        for row in range(len(boards[board])):
            marked[board].append([])
            for col in range(len(boards[board][row])):
                marked[board][row].append(None)
    return marked


def clean(file):
    file = file.readlines()
    for i in file:
        if i == '\n':
            file.remove(i)
    for i in range(len(file)):
        file[i] = file[i].strip('\n')
    return file


def createBoards(file):
    boards = [[]]
    i = 0
    for j in range(len(file)):
        boards[j] = file[i:i+5]
        i += 5
        if i == len(file):
            break
        boards.append([])
    for i in range(len(boards)):
        for j in range(5):
            boards[i][j] = boards[i][j].split()
    return boards


if __name__ == "__main__":
    with open(f"{sys.path[0]}/input.txt") as input:
        main(input)
