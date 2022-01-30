# CS336 Final Project: Vector Space Model
[Python](https://www.python.org/)

## Installation

```bash
$ pip install -r requirements.txt
```

## Usage

Run `index.py` script to index documents stored in `resources/dataset` directory:

```bash
$ python index.py
```

The indexed data is stored in `data/` directory. The set of words is stored in `dictionary.txt` file.
The list of all documents and inverted index is serialized into `docs.pickle` and `inverted_index.pickle` files (using `pickle` serializer module). These files will be read by `query.py` script to perform query.

To perform query, run `query.py` script and provide an argument for it:

```bash
$ python query.py "your query here"
```
