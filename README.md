# Blockchain Mining Simulation Using Python

## Project Overview

This project implements a blockchain mining simulation using **Python** and the **SHA-256 cryptographic hashing algorithm**.

The objective was to generate new hashes with progressively increasing difficulty by searching for nonce values that produce hashes with more leading zero bits than the previously accepted hash.

The simulation uses the previously accepted hash as the starting point for each subsequent mining round.

## Technologies Used

- Python 3
- SHA-256
- Python `hashlib` library
- Random nonce generation
- Time measurement

## How the Mining Algorithm Works

The mining process follows these steps:

1. Initialise the process with a predefined previous hash, pseudonym and difficulty level.
2. Generate a random 16-character hexadecimal nonce.
3. Concatenate the previous hash, pseudonym and nonce.
4. Generate a SHA-256 hash from the combined string.
5. Calculate the difficulty by counting the consecutive leading zero bits in the resulting hash.
6. Accept the new hash if its difficulty exceeds the previous difficulty.
7. Update the previous hash and difficulty before starting the next mining round.

The process continues until the target difficulty of **42** is reached.

## Difficulty Calculation

The program calculates mining difficulty by counting the number of consecutive zero bits from the beginning of a SHA-256 hash.

A hash with more leading zero bits represents a higher difficulty level.

The program uses a custom Python function called `calculate_difficulty()` to examine the binary representation of the hash and determine its difficulty.

## Mining Results

The supplied mining output contains 12 successfully generated blocks.

| Metric | Result |
|:---|:---|
| Starting difficulty | 22 bits |
| Highest recorded difficulty | 39 bits |
| Successful blocks recorded | 12 |
| Hashing algorithm | SHA-256 |
| Nonce format | 16-character hexadecimal |
| Target difficulty | 42 bits |

Each successful block uses the previously accepted hash as the input for the next mining round.

The recorded results demonstrate progressively increasing mining difficulty, from 23 bits to 39 bits.

## How to Run the Project

### Requirements

- Python 3
- No external dependencies required.

### Execution

Clone the repository:

```bash
git clone https://github.com/yourgirlsimdi/blockchain-mining.git
```

Navigate into the project directory:

```bash
cd blockchain-mining
```

Run the Python script:

```bash
python version4.py
```

The program continues searching for valid hashes until the target difficulty of 42 is reached.

## Repository Structure

```text
blockchain-mining/
│
├── version4.py
├── mining_results.txt
└── README.md
```

| File | Description |
|:---|:---|
| `version4.py` | Python implementation of the mining algorithm |
| `mining_results.txt` | Recorded successful hashes, pseudonyms and nonce values |
| `README.md` | Project documentation |

## Key Learning Outcomes

Through this project, I developed practical experience in:

- Implementing SHA-256 cryptographic hashing.
- Understanding proof-of-work mining principles.
- Working with hexadecimal and binary representations.
- Developing random nonce-search algorithms.
- Calculating hash difficulty using leading zero bits.
- Understanding sequential hash validation and blockchain linking.
- Measuring computational effort during mining.

## Project Information

**Project:** Blockchain Mining Simulation

**Programming Language:** Python

**Algorithm:** SHA-256

**Focus Areas:** Blockchain Technology, Cryptography and Computational Problem-Solving
