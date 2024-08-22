For run project checkout to the main branch
and run:

- python main.py rules.cfg text.txt

P.s. you can choose different filenames
but: <br>
First arg must be cfg file and ends with ".cfg"<br>
Second one sample text file and ends with ".txt"

All tests in branch tests_add
For launch them just use one of commands below:

- pytest
- pytest -v

----

(important!) Before run tests install all requirements to your venv by command below:

- pip install -r req.txt

---
# Task
Get a list of pairs from a configuration file (sample configuration file is provided below), and replace value1
by value2 for all matches in a given text file (sample text file is provided below). All values in configuration
file are unique; no need to take care of preventing change of already changed value. Names of both files are
passed as command line arguments. Sort changed lines by the total number of symbols replaced, starting
from the most changed line. Output resulting text to console.

Sample configuration file:

a=z\
b=y\
c=x


Sample text file:

jgrebk6hnae\
cnhjrfyjvth3nxr\
b#sjcf_ansvo!\
djf#aemfaaofna%