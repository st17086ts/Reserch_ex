import copy
import matplotlib.pyplot as plt
import numpy as np

WHITE = 0
BLACK = 1
BOARD_SIZE = 4

WHITE_WIN = 0
BLACK_WIN = 0
DRAW = 0

MAX_LEVEL = 100

#白ー黒の個数を表示
POINT_RESULT = []

def put_disk(x, y, brd, player):
    # 既にほかの石があれば置くことができない
    cells = copy.deepcopy(brd)
    if cells[y][x] is not None:
        return False

    # 獲得できる石がない場合も置くことができない
    flippable = list_flippable_disks(x, y, cells, player)
    if flippable == []:
        return False

    # 実際に石を置く処理
    cells[y][x] = player
    for x,y in flippable:
        cells[y][x] = player

    return cells

def list_flippable_disks(x, y, cells, player):

    PREV = -1
    NEXT = 1
    DIRECTION = [PREV, 0, NEXT]
    flippable = []

    for dx in DIRECTION:
        for dy in DIRECTION:
            if dx == 0 and dy == 0:
                continue

            tmp = []
            depth = 0
            while(True):
                depth += 1

                # 方向 × 深さ(距離)を要求座標に加算し直線的な探査をする
                rx = x + (dx * depth)
                ry = y + (dy * depth)

                # 調べる座標(rx, ry)がボードの範囲内ならば
                if 0 <= rx < BOARD_SIZE and 0 <= ry < BOARD_SIZE:
                    request = cells[ry][rx]

                    # Noneを獲得することはできない
                    if request is None:
                        break

                    if request == player:  # 自分の石が見つかったとき
                        if tmp != []:      # 探査した範囲内に獲得可能な石があれば
                            flippable.extend(tmp) # flippableに追加
                        break

                    # 相手の石が見つかったとき
                    else:
                        # 獲得可能な石として一時保存
                        tmp.append((rx, ry))
                else:
                    break
    return flippable

def show_board(cells, player = None, level=None, set = None):
        """ボードを表示する"""
        print("--" * 20)
        for i in cells:
            for cell in i:
                if cell == WHITE:
                    print("W", end=" ")
                elif cell == BLACK:
                    print("B", end=" ")
                else:
                    print("*", end=" ")
            print("\n", end="")
        if player == 0:
            print("{} th move, White:{}".format(level, set))
        elif player == 1:
            print("{} th move, Black:{}".format(level, set))
        else:
            pass
            

def list_possible_cells(cells, player):
        possible = []
        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                if cells[y][x] is not None:
                    continue
                if list_flippable_disks(x, y, cells, player) == []:
                    continue
                else:
                    possible.append((x, y))
        return possible

def shift_player(player):
    if player == BLACK:
        return WHITE
    else:
        return BLACK

def finish(brd, array, skip):

    if array == [] and skip + 1 == 2:
        return True

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if (brd[i][j] == None):
                return False
    return True

def count(brd):
    point = [0, 0]
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if brd[i][j] == 0:
                point[0] = 1 + point[0]
            elif brd[i][j] == 1:
                point[1] = 1 + point[1]
    return point



def play(brd, player, level, skip):

    possible = list_possible_cells(brd, player)
    if level > MAX_LEVEL:
        print("end!")
    elif finish(brd, possible, skip):
        global WHITE_WIN, BLACK_WIN, DRAW
        #print("GAME OVER")
        point = count(brd)
        POINT_RESULT.append(point[0] - point[1])
        if point[0] > point[1]:
            WHITE_WIN = WHITE_WIN + 1
            #print("WHITE WIN!")
        elif point[0] < point[1]:
            BLACK_WIN = BLACK_WIN + 1
            #print("BLACK WIN")
        else:
            DRAW = DRAW + 1
            #print("DRAW")
    else:
        #おける場所がない
        if possible == []:
            #print("skip")
            play(brd, shift_player(player), level+1, skip+1)

        skip = 0

        for i in range(len(possible)):
            nbrd = put_disk(*possible[i], brd, player)
            #show_board(nbrd, player, level, possible[i])
            play(nbrd, shift_player(player), level+1, skip)


def print_win_rate_Graph(brd = None):

    global BLACK_WIN, WHITE_WIN, DRAW

    if brd != None:
        print("init board")
        show_board(brd)

    left = np.array([0, 1, 2])
    height = np.array([BLACK_WIN, WHITE_WIN, DRAW])
    label = ["BLACK_WIN", "WHITE_WIN", "DRAW"]
    plt.bar(left, height, tick_label = label, align = "center")
    plt.title("Reversi score")
    plt.ylabel("Wins")
    plt.show()
    print("MATCHES:{}".format(BLACK_WIN + WHITE_WIN + DRAW))
    print("BLACK_WIN:{}".format(BLACK_WIN))
    print("WHITE_WIN:{}".format(WHITE_WIN))
    print("DRAWS:{}".format(DRAW))

    BLACK_WIN = WHITE_WIN = DRAW = 0

def print_AREA_GRAPH(brd = None):

    global POINT_RESULT

    if brd != None:
        print("init board")
        show_board(brd)

    result = np.array(POINT_RESULT)
    times = np.arange(len(POINT_RESULT))

    for i in range(len(POINT_RESULT)):
        if result[i] > 0:
            plt.bar(i, result[i], color = "orange")
        else:
            plt.bar(i, result[i], color = "blue")

    plt.show()

    POINT_RESULT = []

def Show_Graph(brd = None):
    print_AREA_GRAPH(brd)
    print_win_rate_Graph(brd)

def match_count():
    global BLACK_WIN, WHITE_WIN, DRAW
    print("MATCHES:{}".format(BLACK_WIN + WHITE_WIN + DRAW))
    # print("BLACK_WIN:{}".format(BLACK_WIN))
    # print("WHITE_WIN:{}".format(WHITE_WIN))
    # print("DRAWS:{}".format(DRAW))
    BLACK_WIN = WHITE_WIN = DRAW = 0

def area():
    result = np.array(POINT_RESULT)
    times = np.arange(len(POINT_RESULT))
       

    plt.bar(times, result,color="C1")

    plt.bar(times[:4], result[:4], color = "b")

    plt.bar(times[4:4 + 9], result[4:4+9], color = "g")

    plt.bar(times[4 + 9:4 + 9 + 5], result[4 + 9:4 + 9 + 5], color = "r")

    #plt.bar(times[19 + 100 + 56: 19 + 100 + 56 + 36], result[19 + 100 + 56:19 + 100 + 56 + 36], color = "C2")

    plt.show()