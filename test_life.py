from main import next_board_state

def test_dead_state():
    init_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    expected_next_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    assert next_board_state(init_state1) == expected_next_state1

def test_alive_state():
    init_state2 = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]
    expected_next_state2 = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]
    assert next_board_state(init_state2) == expected_next_state2

def test_oscillating_state():
    init_state3 = [
        [0,1,0],
        [0,1,0],
        [0,1,0]
    ]
    expected_next_state3 = [
        [0,0,0],
        [1,1,1],
        [0,0,0]
    ]
    assert next_board_state(init_state3) == expected_next_state3
