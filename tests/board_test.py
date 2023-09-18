from schack import board


def test_board():
    b = board.Board()
    b.Setup_Board()
    assert b is not None
