from src.luserta.extendict import ExtenDict


def test_extendict():
    assert ExtenDict({1: 1}).get(1) == 1

    assert {}.get(1, 0) == 0
    assert ExtenDict({}).get(1, 0) == 0
    assert ExtenDict({}).coalesce(1, 0) == 0

    assert {1: None}.get(1, 0) is None
    assert ExtenDict({1: None}).get(1, 0) is None
    assert ExtenDict({1: None}).coalesce(1, 0) == 0

    assert {1: 0}.get(1,5) == 0
    assert ExtenDict({1: 0}).coalesce(1, 5) == 0
    
