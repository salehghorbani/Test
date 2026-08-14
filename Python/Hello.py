"""Simple greeting program.

This module provides a `greet` function and a small CLI to print a greeting.
"""
from __future__ import annotations

import argparse


def greet(name: str = "World") -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


def main() -> None:
    parser = argparse.ArgumentParser(description="Greet someone.")
    parser.add_argument("name", nargs="?", default="World", help="Name to greet")
    args = parser.parse_args()
    print(greet(args.name))


if __name__ == "__main__":
    main()
