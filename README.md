![Advent of Code Logo](https://adventofcode.com/favicon.png)

# Advent of Code 2024

This repository contains my solutions for the [Advent of Code 2024](https://adventofcode.com/2024) challenges.

## Requirements

The solutions were written in Python 3.10. To install the required packages, run:

```bash
pip install -r requirements.txt
```

## Repository structure

The repository is structured as follows:

```markdown
│
├── README.md
├── .gitignore
├── requirements.txt
├── aoc/
│   ├── __init__.py
│   ├── utils.py
│   ├── day01.py
│   ├── day02.py
│   ├── ...
│   └── day25.py
│
├── input/
│   ├── day01.txt
│   ├── day02.txt
│   ├── ...
│   └── day25.txt
│
├── tests/
│   ├── __init__.py
│   ├── test_day01.py
│   ├── test_day02.py
│   ├── ...
│   └── test_day25.py
│
└── scripts/
    ├── fetch_inputs.py
    └── run_day.py
```

The `input/` directory is not included in the repository, as requested by the challenge author. To fetch the input files for each day, you can use the `fetch_inputs.py` script.

## Running the solutions

To run the solutions for a specific day, use the `run_day.py` script. For example, to run the solutions for day 1, while in the root directory, run:

```bash
PYTHONPATH=. python scripts/run_day.py 1
```

## Running the tests

To run the tests, use the following command:

```bash
pytest
```

## License

This project is licensed under the [MIT License](LICENSE).
