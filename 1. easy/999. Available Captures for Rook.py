class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        board_size = 8

        # Find rook
        # O(n^2)
        rook_i, rook_j = -1, -1
        for idx in range(board_size * board_size):
            i = idx // board_size
            j = idx % board_size
            if board[i][j] == "R":
                rook_i = i
                rook_j = j
                break

        # Seek for direct pawn in every direction
        # O(4 * n-1) = O(n)
        count_direct_pawns = 0
        for mode in range(4):
            for x in range(1, board_size):
                target_i = rook_i + (mode == 0) * x - (mode == 1) * x
                target_j = rook_j + (mode == 2) * x - (mode == 3) * x

                if target_i < 0 or target_i >= board_size or target_j < 0 or target_j >= board_size or board[target_i][target_j] == "B":
                    break

                if board[target_i][target_j] == "p":
                    count_direct_pawns += 1
                    break

        return count_direct_pawns
