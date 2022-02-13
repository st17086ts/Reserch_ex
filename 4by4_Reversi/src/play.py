import main
import copy
import time

WHITE = 0
BLACK = 1
BOARD_SIZE = 4
#根源解析
#B1_1_1
# W B * *
# W B B *
# W B W *
# B * * *
B1_1_1 = [[0, 1, None, None], [0, 1, 1, None], [0, 1, 0, None], [1, None, None, None]]

#B1_1_2
# W B * *
# W B B *
# W B W *
# * B * *
B1_1_2 = [[0, 1, None, None], [0, 1, 1, None], [0, 1, 0, None], [None, 1, None, None]]

#B1_1_3
# W B * *
# W B B *
# W W B *
# * * B *
B1_1_3 = [[0, 1, None, None], [0, 1, 1, None], [0, 0, 1, None], [None, None, 1, None]]

#B1_1_4
# W B * *
# W B B *
# W W B *
# * * * B
B1_1_4 = [[0, 1, None, None], [0, 1, 1, None], [0, 0, 1, None], [None, None, None, 1]]

#B1
B1 = [[0, 0, 0, 1], [0, 0, 1, None], [0, 1, 0, None], [1, None, None, None]]
B2 = [[0, 0, 0, None], [0, 0, 0, None], [0, 1, 1, 1], [1, None, None, None]]

main.play([[0, 0, 0, None], [0, 0, 0, None], [0, 0, 1, 1], [1, 0, None, None]], BLACK, 0, 0)
main.print_AREA_GRAPH()
main.print_win_rate_Graph()

main.play(B2, WHITE, 0, 0)
main.print_AREA_GRAPH()
main.print_win_rate_Graph()

#B2 後で解析する
# main.play([[0, 0, 0, None], [0, 0, 0, None], [0, 1, 0, None], [None, 1, None, None]], BLACK, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()

# main.play([[0, 1, None, None], [0, 1, 1, None], [0, 0, 0, None], [None, 1, 0, None]] ,BLACK, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()


# main.play([[0, 1, None, None], [0, 0, 0, 0], [0, 1, 0, None], [None, 1, None, None]],BLACK, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()

##W1 of B2
# main.play([[0, 0, 0, 1], [0, 0, 1, None], [0, 1, 0, None], [None, 1, None, None]], WHITE, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()

###B2-> W1 -> BACK
# W1 = [[0, 0, 0, 1], [0, 0, 1, None], [0, 0, 0, None], [None, 1, 0, None]]
# W2 = [[0, 0, 0, 1], [0, 0, 0, 0], [0, 1, 0, None], [None, 1, None, None]]
# W3 = [[0, 0, 0, 1], [0, 0, 0, None], [0, 1, 0, 0], [None, 1, None, None]]

# main.play(W1, BLACK, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()
# main.play(W2, BLACK, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()
# main.play(W3, BLACK, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()

####W2 ->
# main.play([[0, 0, 0, 1], [0, 0, 0, 1], [0, 1, 1, 1], [None, 1, None, None]], WHITE, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()


#白必勝
# main.play([[0, 0, 0, None], [0, 0, 0, 1], [0, 1, 1, None], [None, 1, None, None]], WHITE, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()

# #白必勝
# main.play([[0, 0, 0, None], [0, 0, 0, None], [0, 1, 1, 1], [None, 1, None, None]], WHITE, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()

#B4
# main.play([[0, 0, 0, None], [0, 0, 1, None], [0, 0, 1, None], [None, None, None, 1]],BLACK, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()

# #これだ！
# main.play([[0, 1, None, 0], [0, 1, 0, None], [0, 0, 1, None], [None, None, None, 1]],BLACK, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()

# B3 = [[0, 1, None, None], [0, 0, 0, 0], [0, 0, 1, None], [None, None, None, 1]]
# B4 = [[0, 1, None, None], [0, 1, 1, None], [0, 0, 0, 0], [None, None, None, 1]]

# main.play(B3, BLACK, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()

# main.play(B4,BLACK, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()

## next WHITE これだ
# B1 = [[0, 1, None, 0], [0, 1, 0, None], [0, 1, 1, None], [None, 1, None, 1]]
B2 = [[0, 1, 1, 0], [0, 1, 1, None], [0, 0, 1, None], [None, None, None, 1]]
# B3 = [[0, 1, None, 0], [0, 1, 1, 1], [0, 0, 1, None], [None, None, None, 1]]
# B4 = [[0, 1, None, 0], [0, 1, 1, None], [0, 0, 1, 1], [None, None, None, 1]]

#1引き分けのみ
# main.play(B1, WHITE, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()
#やばい
# main.play(B2, WHITE, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()
#必勝
# main.play(B3, WHITE, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()
#負け１
# main.play(B4, WHITE, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()

###やばい
# main.play([[0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 1, None], [None, None, None, 1]], BLACK, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()

# main.play([[0, 1, 1, 0], [0, 1, 1, None], [0, 0, 0, 0], [None, None, None, 1]], BLACK, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()

###かなりやばい
# main.play([[0, 1, 1, 0], [0, 1, 0, 0], [0, 1, 1, None], [None, 1, None, 1]], WHITE, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()

# main.play([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 1], [None, None, None, 1]], WHITE, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()



# main.play([[0, 1, None, None], [0, 0, 0, 0], [0, 0, 1, None], [None, None, None, 1]],BLACK, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()

# main.play([[0, 1, None, None], [0, 1, 1, None], [0, 0, 0, 0], [None, None, None, 1]],BLACK, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()


# B1 = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 1], [None, None, None, 1]]
# B2 = [[0, 1, 1, 0], [0, 1, 1, None], [0, 1, 0, 0], [None, 1, None, 1]]
# B3 = [[0, 1, 1, 0], [0, 1, 1, None], [0, 0, 1, 0], [None, None, 1, 1]]

# main.play(B1, WHITE, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()

# main.play(B2, WHITE, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()

# main.play(B3, WHITE, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()


#[[0, 1, 1, 0], [0, 1, 1, 1], [0, 0, 0, 1], [None, None, None, 1]] #話と違う

# main.play([[0, 1, 1, 0], [0, 1, 1, 1], [0, 0, 0, 1], [None, None, None, 1]], BLACK, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()


#ありがとう兒玉先生 BLACK
#W1 = [[0, 0, 0, None], [0, 0, 1, None], [0, 0, 1, None], [1, 0, None, 1]]
# W2 = [[0, 0, 0, None], [0, 0, 0, None], [0, 0, 0, None], [1, None, 0, 1]]
# W3 = [[0, 0, 0, None], [0, 0, 0, 0], [0, 1, 1, None], [1, None, None, 1]]
# W4 = [[0, 0, 0, None], [0, 0, 0, None], [0, 0, 0, 0], [1, None, None, 1]]

# main.play(W1, BLACK, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()

# main.play(W2, BLACK, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()

# main.play(W3, BLACK, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()

# main.play(W4, BLACK, 0, 0)
# main.print_AREA_GRAPH()
# main.print_win_rate_Graph()

main.play([[None, None, None, None], [None, 0, 1, None], [None, 1, 0, None], [None, None, None, None]], BLACK, 0, 0)
main.Show_Graph()
