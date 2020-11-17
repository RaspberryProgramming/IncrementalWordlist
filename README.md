# IncrementalWordlist

Created to make it easy to generate a wordlist workload for a distibuted bruteforce application. Giving the program an integer and a list of characters will generate a number. Starting at 0, the program creates 1, 2, 3, etc. character words in an incremental order.

# Benchmark Example

Clone the Repo
 
`git clone https://github.com/RaspberryProgramming/IncrementalWordlist`

CD into the Repo

`cd IncrementalWordlist`

CD into the python folder

`cd python3`

Run iw.py

`python3 iw.py`

# Example python code

Convert number to hashcode

```
import iw
iw.numToTextCode(number)
```

Create Wordlist from 0 - 9

```
import iw
for i in range(0,10):
    iw.numToTextCode(i)
```
Use custom chars list

```
import iw

chars = ["a", "b", "c", "d"]

iw.numToTextCode(10, chars=chars)
```
