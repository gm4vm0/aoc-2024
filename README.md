# 🎄 Advent of Code 2024 🎄

## Setup

Create a .env file in the root directory with the AoC session cookie to enable input downloads:

```env
AOC_SESSION=<aoc_session>
```

## Available Scripts

### Generate template files and download input data

Input data are not included in the repo, run the command to generate and download inputs for each day:

```bash
poetry run add-day <day_number>
```

### Run solution

Run solution against downloaded input data for a specified day:

```bash
poetry run run-day <day_number>
```

### Run tests

Run tests for a specified day:

```bash
poetry run test-day <day_number>
```

### Run visualizations

Run visualizations for a specified day (only for some):

```bash
poetry run vis-day <day_number>
```
