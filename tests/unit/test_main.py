from src.main import main


def test_main_returns_hello_world() -> None:
    assert main() == "Hello, world!"
