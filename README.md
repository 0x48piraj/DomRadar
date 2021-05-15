# Dom Radar

Lightning fast Python tool for discovering  available domain names.


## Installation

Use pip to install DomRadar's . This is the recommended way of running DomRadar.

```shell
# clone the repo
$ git clone https://github.com/0x48piraj/DomRadar.git

# change the working directory to DomRadar
$ cd DomRadar
```

#### Prerequisites

- Python 3.5+

Run the following to install all the following required python libraries,

```
$ pip install -r requirements.txt
```

- [python-whois](http://pypi.org/project/python-whois/)
- [tqdm](https://pypi.org/project/tqdm/)
- [requests](http://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)


## Usage

```python
$ python3 main.py --help
usage: main.py [-h] [-ds {all,animal,random}] [-v {0,1,2}] (-d | -p)

Example:
    $ python3 main.py --print or python3 main.py --dataset all --print
    $ python3 main.py --dataset animal --dump/--print
    $ python3 main.py -ds animal -d/-p

optional arguments:
  -h, --help            show this help message and exit
  -ds {all,animal,random}, --dataset {all,animal,random}
                        name of the dataset to use
  -v {0,1,2}, --verbosity {0,1,2}
                        increase output verbosity (default: 0)
  -d, --dump            stdout the results to file
  -p, --print           stdout the results to console
```


## DISCLAMER

This project is a [personal development](https://en.wikipedia.org/wiki/Personal_development). Please respect it's philosophy and don't use it for evil purposes. By using DomRadar, you agree to the MIT license included in the repository. For more details at [The MIT License &mdash; OpenSource](https://opensource.org/licenses/MIT). It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.


## Licensing

This project is licensed under the MIT license.