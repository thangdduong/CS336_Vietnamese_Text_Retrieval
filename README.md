# CS336 Final Project: Text Retrieval
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/)

## Description
In this project, we tackle the Vietnamese Text Retrieval problem using the Vector Space Model. This model is built from the corpus of 43303 Vietnam news. We also build a web demo that can input a query and retrieve the top 10 documents that might relevant to the query.
## Instructor
<b>Ph.D. Thanh Duc Ngo</b>

## Members
<table>
  <tr>
    <th>No.</th>
    <th>Full Name</th>
    <th>Student ID</th>
    <th>Gmail</th>
  </tr>
  <tr>
    <th>1</th>
    <th>Dương Đình Thắng</th>
    <th>19522195</th>
    <th>19522195@gm.uit.edu.vn</th>
  </tr>
  <tr>
    <th>2</th>
    <th>Lý Hoàng Thuận</th>
    <th>19522315</th>
    <th>19522315@gm.uit.edu.vn</th>
  </tr>
</table>

## Installation

We highly recommend using Anaconda for creating a virtual enviroment, this ensure the program can run perfectly. You can download Anaconda in the following instruction: [download](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html).

After Anaconda is downloaded, create a virtual enviroment and install required libraries:

```bash
$ conda create -n vsm_env -y
$ pip install -r requirements.txt
```

## Dataset
The dataset we use in this project can be downloaded from the following [link](https://drive.google.com/drive/folders/1CnBSEoWIVuZ3RwZE6JfP0HTge7UIMDD4?usp=sharing)

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

We also build a simple web demo using Flask, if you want to have a look at it please run:

```bash
$ python main.py
```
