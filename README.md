# CS336 Final Project: Vector Space Model
![Python](https://www.python.org/)

## Instructor:
<ul>
  <li> <b>PhD. Thanh Duc Ngo</b></li>
</ul> 

## Members

<table>
  <tr>
    <th>No.</th>
    <th>Full name</th>
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

We highly recommend using Anaconda for creating a virtual enviroment, this ensure the program can run perfectly. You can download Anaconda in the following instruction: ![download](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html).

After Anaconda is downloaded, create a virtual enviroment and install required libraries:

```bash
$ conda create -n vsm_env -y
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
