# AwesomeChallenge

This project implements a simple algorithm to perform some basic statistics on a collection of numbers less than one thousand.

## Project structure

It is made up of a challenge module (which contains the exercise's logic), a main and test scripts. The test script checks different cases to make sure the logic is correct. The main script is an example of usage for the DataCapture class. The project does not use any python external libraries.

```
.
├── challenge
│   ├── __init__.py
│   ├── data_capture.py
│   └── stats.py
├── main.py
├── test.py
├── Pipfile
└── README.md
```

## Run tests

```
python test.py
```

## Run main script

```
python main.py
```

## General usage

For using the module on a custom script, make sure to follow the next pattern:

```python
from challenge import DataCapture

capture = DataCapture()
capture.add(0)
capture.add(10)

stats = capture.build_stats()
```
