"""Tests for the hello world function."""

from teacupy.helloworld import hello_world


def test_hello_world() -> None:
    """Tests that the hello world function returns the expected string."""
    assert hello_world() == "Hello, World!"


def test_hello_world_fails() -> None:
    """A failing test for demonstration purposes."""
    assert hello_world() == "Hello, Universe!"
