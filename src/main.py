from minesweeper import board


def main():
    b = board.Board()
    b.generate_board(5, 5, 5)
    print(b.show_board())


if __name__ == "__main__":
    main()
