# 2021-advent-of-code

![Build status](https://github.com/andrewfitzy/2021-advent-of-code/actions/workflows/build-and-test-project.yml/badge.svg)

Each day, [advent of code](https://adventofcode.com/2021) presents a challenge for those of brave heart to complete.
This repo contains my answers to the 2021 version of advent of code, not all challenges have been completed. I complete
AoC to get familiar with a technology, its build tools and testing tools, it's kind of a mini-production type workflow
I follow.

In this year I chose to use the following tools:
- [Python v3.11.5](https://www.python.org). Language for this years AOC solutions.
- [black v23.9.1](https://black.readthedocs.io/en/stable/). Prettifier for python code.
- [ruff v0.1.0](https://docs.astral.sh/ruff/). Linter for python code.
- [isort v5.12.0](https://pycqa.github.io/isort/). Sorts imports in python code.
- [pytest v7.4.2](https://docs.pytest.org/en/7.4.x/). Testing framework for python code.
- [pre-commit v3.5.0](https://pre-commit.com). Used for pre commit hooks.

All development was completed using [PyCharm](https://www.jetbrains.com/pycharm/) which is an awesome IDE.

## Setup
With Python, I like to work with virtual envs, this keeps the development environments for each project separate.

First step is to install the version of python to use. I use pyenv to manage my python versions, so I install
the version I want to use with the following command:
```bash
pyenv install 3.11.5
````

Next I create a virtual environment for the project:
```bash
pyenv virtualenv 3.11.5 2021-advent-of-code
```

Then I activate the virtual environment:
```bash
pyenv activate 2021-advent-of-code
```

Finally, I install the dependencies:
```bash
pip install -r requirements-dev.txt
```
My environment is now setup and ready to go.

## Testing
```bash
$ make test
```

## Committing
The pre-commit hook should kick-in, when it does it will lint and prettify the code.
```bash
$ git add --all
$ git commit -a
```

## Progress
|                                                | Challenge               |                                         Task 1                                         |                                         Task 2                                         |
|:-----------------------------------------------|:------------------------|:--------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| [Day 01](https://adventofcode.com/2021/day/1)  | Sonar Sweep             | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day01/Task01.py) | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day01/Task02.py) |
| [Day 02](https://adventofcode.com/2021/day/2)  | Dive!                   | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day02/Task01.py) | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day02/Task02.py) |
| [Day 03](https://adventofcode.com/2021/day/3)  | Binary Diagnostic       | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day03/Task01.py) | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day03/Task02.py) |
| [Day 04](https://adventofcode.com/2021/day/4)  | Giant Squid             | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day04/Task01.py) | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day04/Task02.py) |
| [Day 05](https://adventofcode.com/2021/day/5)  | Hydrothermal Venture    | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day05/Task01.py) | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day05/Task02.py) |
| [Day 06](https://adventofcode.com/2021/day/6)  | Lanternfish             | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day06/Task01.py) | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day06/Task02.py) |
| [Day 07](https://adventofcode.com/2021/day/7)  | The Treachery of Whales | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day07/Task01.py) | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day07/Task02.py) |
| [Day 08](https://adventofcode.com/2021/day/8)  | Seven Segment Search    | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day08/Task01.py) | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day08/Task02.py) |
| [Day 09](https://adventofcode.com/2021/day/9)  | Smoke Basin             | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day09/Task01.py) | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day09/Task02.py) |
| [Day 10](https://adventofcode.com/2021/day/10) | Syntax Scoring          | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day10/Task01.py) | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day10/Task02.py) |
| [Day 11](https://adventofcode.com/2021/day/11) | Dumbo Octopus           | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day11/Task01.py) | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day11/Task02.py) |
| [Day 12](https://adventofcode.com/2021/day/12) | Passage Pathing         | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day12/Task01.py) | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day12/Task02.py) |
| [Day 13](https://adventofcode.com/2021/day/13) | Transparent Origami     | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day13/Task01.py) | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day13/Task02.py) |
| [Day 14](https://adventofcode.com/2021/day/14) | Extended Polymerization | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day14/Task01.py) | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day14/Task02.py) |
| [Day 15](https://adventofcode.com/2021/day/15) | Chiton                  | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day15/Task01.py) | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day15/Task02.py) |
| [Day 16](https://adventofcode.com/2021/day/16) | Packet Decoder          | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day16/Task01.py) |                                                                                        |
| [Day 17](https://adventofcode.com/2021/day/17) | Trick Shot              |                                                                                        |                                                                                        |
| [Day 18](https://adventofcode.com/2021/day/18) | Snailfish               |                                                                                        |                                                                                        |
| [Day 19](https://adventofcode.com/2021/day/19) | Beacon Scanner          |                                                                                        |                                                                                        |
| [Day 20](https://adventofcode.com/2021/day/20) | Trench Map              | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day20/Task01.py) | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day20/Task02.py) |
| [Day 21](https://adventofcode.com/2021/day/21) | Dirac Dice              | [🌟](https://github.com/andrewfitzy/2021-advent-of-code/blob/main/src/Day21/Task01.py) |                                                                                        |
| [Day 22](https://adventofcode.com/2021/day/22) | Reactor Reboot          |                                                                                        |                                                                                        |
| [Day 23](https://adventofcode.com/2021/day/23) | Amphipod                |                                                                                        |                                                                                        |
| [Day 24](https://adventofcode.com/2021/day/24) | Arithmetic Logic Unit   |                                                                                        |                                                                                        |
| [Day 25](https://adventofcode.com/2021/day/25) | Sea Cucumber            |                                                                                        |                                                                                        |