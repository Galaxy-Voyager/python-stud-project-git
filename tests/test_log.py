import pytest
from src.decorators.log import log
import os


@pytest.fixture
def log_file(tmp_path):
    filename = tmp_path / "test_log.txt"
    yield filename
    if os.path.exists(filename):
        os.remove(filename)


def test_log_to_file(log_file):
    @log(filename=log_file)
    def add(a, b):
        return a + b

    add(1, 2)

    with open(log_file, "r") as f:
        assert "add ok" in f.read()


def test_log_to_console(capsys):
    @log()
    def divide(a, b):
        return a / b

    divide(4, 2)
    captured = capsys.readouterr()
    assert "divide ok" in captured.out


def test_log_error(log_file):
    @log(filename=log_file)
    def fail():
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        fail()

    with open(log_file, "r") as f:
        assert "fail error: ValueError" in f.read()
