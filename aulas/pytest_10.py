import pytest

class Test_simulacao():

    @pytest.mark.simulacao
    def test_simulacao(self):
        assert 1+1 == 2
    @pytest.mark.simulacao02
    @pytest.mark.skip
    def test_simulacao_02(self):
        assert 1 == 1