# 승리 조건 확인 (board는 main에서 정의 예정)
def check_win(board, player):
    # 가로 체크
    for i in range(3):
        if (board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] == player):
            return True
    # 세로 체크
    for i in range(3):
        if (board[i] == board[i + 3] == board[i + 6] == player):
            return True
    # 대각선 체크
    if (board[0] == board[4] == board[8] == player) or (board[2] == board[4] == board[6] == player):
        return True
    return False