# https://www.acmicpc.net/problem/6527

from sys import stdin
import math
import re


def main():
    inputs: list[str] = []
    while (inp := stdin.readline().strip()) != "":
        inputs.append(inp)

    words = re.split(r"[^a-zA-Z]+", " ".join(inputs))

    n_games = 0
    n_words = 0
    game_word_set: set[str] = set()

    for word in words:
        if word != "BULLSHIT":
            game_word_set.add(word.lower())
            continue

        # Game ends
        n_games += 1
        n_words += len(game_word_set)
        game_word_set.clear()

    # Simplify fraction
    gcd = math.gcd(n_games, n_words)
    print(f"{n_words // gcd} / {n_games // gcd}")


if __name__ == "__main__":
    main()
