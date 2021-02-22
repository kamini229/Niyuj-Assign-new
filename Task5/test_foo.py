import pytest


@pytest.mark.regression
def test_perform():
    """This is a perform method with regression marker"""
    assert 3 == 4


@pytest.mark.sanity
def test_high():
    """This is a high method with sanity marker"""
    assert True


@pytest.mark.smoke
def test_sm():
    """This is a sm method with smoke marker"""
    assert False


class TestCsvFile:
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_func1(self):
        """This is a func1 with smoke and regression marker"""
        assert True

    @pytest.mark.sanity
    def test_func2(self):
        """This is a func2 with sanity marker"""
        assert 23 == 25
