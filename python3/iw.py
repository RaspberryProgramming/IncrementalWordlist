import time

def_chars = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z"
    ]
    
def floor(num):
    i= int(num)
    if (i > num):
        i -= 1
    
    return i

def getLevelSize(level, arraySize):
    size = 0
    i = 1
    while (i <= level): 
        size = arraySize ** i + size
        i += 1

    return size


def getLevel(id, arraySize):
    id += 1
    level = 0
    beggining = 0
    while (beggining < id):
        beggining = 0
        level += 1
        i = 1
        while (i<= level): 
            beggining = arraySize ** i + beggining
            i+=1


    if beggining == 0:
        return level
    else:
        return level - 1


def numToTextCode(num, chars=None):
    if chars==None:
        chars=def_chars

    charslen = len(chars)

    level = getLevel(num, charslen)

    
    line = ""  # clear the line
    
    num -= getLevelSize(level - 1, charslen)
    
    # The new code is generated
    while True:
    # The code is determined by the remainder of the new text code and the size of chars array
        charLoc = num % charslen

        line += chars[charLoc]  # The first character is copied to the line

        # The division of the textcode and chars array size is stored. This moves us to the next char in the charcode
        num = floor(num / charslen)
    # Once tempTextCode is 0 or less, there aren't any more characters in the char code
        if(num <= 0):
            break
        
    startchar = chars[0]
    while (len(line) < level):
        # If the
        line += startchar
    return line

def benchmarkProcess(procnum, return_dict, start, stop, chars=None):
    """
    process function
    """
    import hashlib

    if chars==None:
        chars=def_chars
    
    text = ""
    for i in range(start, stop): # Iterates through start-stop
        text = numToTextCode(i) # Convert the given number to text code
        hashlib.sha256(text.encode('utf-8')).hexdigest() # Convert text code to hash

    return_dict[procnum] = True


def benchmarkMulti(start, stop, chars=None, processes=None):
    import multiprocessing

    if (chars==None):
        chars=def_chars

    if (processes==None):
        processes=multiprocessing.cpu_count()

    time1 = time.time()
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    jobs = []
    step = int((stop-start)/processes)
    print(start, stop, step)
    for i in range(start, stop, step):
        p = multiprocessing.Process(target=benchmarkProcess,
                                    args=(i, return_dict, i, i+step))
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()
    time2 = time.time()

    return time2-time1

def benchmarkSingle(start, stop, chars=None):
    """
    Runs a benchmark on the current computer using the following parameters.

        Parameters:
            chars (list): List of characters which will be used in the wordlist
            start (int): Starting number
            stop (int): Stopping number
    """
    import hashlib # We use the hashing functions in this library

    if chars==None:
        chars=def_chars

    time1 = time.time() # Set the starting time
    text = "" # Used to store the text which will be hashed
    
    for i in range(start, stop): # Iterates through start-stop
        text = numToTextCode(i) # Convert the given number to text code
        hashlib.sha256(text.encode('utf-8')).hexdigest() # Convert text code to hash
    
    time2 = time.time() # set the stopping time
    
    return time2 - time1 # Return time it took to run


if __name__ in '__main__':
    print(benchmarkMulti(0,1000000))
    print(benchmarkSingle(0,1000000))
