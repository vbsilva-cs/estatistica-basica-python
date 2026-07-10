# test unitário de funções matemáticas no arquivo estatistica.py

from estatistica import desvio_padrao, media, variancia


def test_media():
    assert media([1, 2, 3, 4, 5]) == 3
    assert media([]) == 0

def test_variancia():
    assert variancia([1, 2, 3, 4, 5]) == 2
    assert variancia([]) == 0

def test_desvio_padrao():
    assert desvio_padrao([1, 2, 3, 4, 5]) == 2 ** 0.5
    assert desvio_padrao([]) == 0