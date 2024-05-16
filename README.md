#  Data Streams in Python 


### Challenges
- [Challenge 1:](#1-challenge-data-streams-in-python) Data Streams in Python
- [Challenge 2:](#2-challenge-map-function) *map()* function
- [Challenge 3:](#3-challenge-reduce-function) *reduce()* function
- [Challenge 4:](#4-challenge-sort-function) *sort()* function
- [Challenge 5:](#5-challenge-pipeline-for-product-codes) Pipeline for Product Codes
- [Challenge 6:](#6-challenge-run-unit-tests) Run Unit Tests
- [Challenge 7:](#7-challenge-sign-off) Sign-off

Points: [1, 2, 3, 3, 2, 0, 1]


&nbsp;
### 1.) Challenge: Data Streams in Python

Data streams are powerful abstractions for data-driven applications that also work in distributed environments. Big Data platforms often build on streams such as
[Spark Streams](https://spark.apache.org/docs/latest/streaming-programming-guide.html) or
[Kafka](https://kafka.apache.org/documentation/streams).

A data stream starts with a *source* (here just a list of names) followed by a pipeline of *chainable operations* performed on each data element passing through the stream. Results can be collected at the *terminus* of the stream.



Application of the stream can demonstrated by the example of a stream of names. The stream is instantiated from the `names` list. The `source()` - method returns the first `__Stream_op` - instance onto which chainable stream methods can be attached.

The stream in the example filters names of lenght = 4, prints those names and counts their number. The *lambda*-expression controls the filter process. Only names of length 4 pass to subsequent pipeline operations.

```py
names = ['Gonzalez', 'Gill', 'Hardin', 'Richardson', 'Buckner', 'Marquez',
    'Howe', 'Ray', 'Navarro', 'Talley', 'Bernard', 'Gomez', 'Hamilton',
    'Case', 'Petty', 'Lott', 'Casey', 'Hall', 'Pena', 'Witt', 'Joyner',
    'Raymond', 'Crane', 'Hendricks', 'Vance', 'Cleveland', 'Duncan', 'Soto',
    'Brock', 'Graham', 'Nielsen', 'Rutledge', 'Strong', 'Cox']

```

Output:
```c++
['Gill', 'Howe', 'Case', 'Lott', 'Hall', 'Pena', 'Witt', 'Soto']
found 8 names with 4 letters.
```
**Questions:**

 - How does method chaining work?
    - What is required for chainable methods? 
 - How does a data pipeline gets formed in the example?
    - Draw a sketch of data objects and how they are linked from the example above.


&nbsp;
### 2.) Challenge: *map()* function

Complete the `map()` function in [stream.py](stream.py) so that the example produces
the desired result: Names are mapped to name lengths for the first 8 names.
Name lengths are then compounded to a single result.


Output:
```c++
['Gonzalez', 'Gill', 'Hardin', 'Richardson', 'Buckner', 'Marquez', 'Howe', 'Ray']
[8, 4, 6, 10, 7, 7, 4, 3]
```


&nbsp;
### 3.) Challenge: *reduce()* function

Complete the `reduce()` function in [stream.py](stream.py) so that name lengths are
compounded (added one after another) to a single result.

Output:
```c++
['Gonzalez', 'Gill', 'Hardin', 'Richardson', 'Buckner', 'Marquez', 'Howe', 'Ray']
[8, 4, 6, 10, 7, 7, 4, 3]
compound number of letters in names is: 49.
```


3.1) Test your implementation to also work for the next example that produces
a single string of all n-letter names:


Output for n=3 and n=5:
```c++
['Ray', 'Cox']
compounded 3-letter names: RAYCOX.

['Gomez', 'Petty', 'Casey', 'Crane', 'Vance', 'Brock']
compounded 5-letter names: GOMEZPETTYCASEYCRANEVANCEBROCK.
```


&nbsp;
### 4.) Challenge: *sort()* function

Complete the `sort()` function in [stream.py](stream.py) so that the example produces
the desired result (use Python's built-in `sort()` or `sorted()` functions).


Output:
```c++
unsorted: ['Gonzalez', 'Gill', 'Hardin', 'Richardson', 'Buckner', 'Marquez', 'Howe', 'Ray']
  sorted: ['Buckner', 'Gill', 'Gonzalez', 'Hardin', 'Howe', 'Marquez', 'Ray', 'Richardson']
```

4.1) Understand the sorted sequence below and define a `comperator` (expression that compares two elements (n1, n2) and yields `-1` if n1 should come before n2, `+1` if n1 must be after n2 or `0` if n1 is equal to n2):

Output:
```c++
sorted: ['Cox', 'Ray', 'Case', 'Gill', 'Hall', 'Howe', 'Lott', 'Pena', 'Soto', 'Witt', 'Brock', 'Casey', 'Crane', 'Gomez', 'Petty', 'Vance', 'Duncan', 'Graham', 'Hardin', 'Joyner', 'Strong', 'Talley', 'Bernard', 'Buckner', 'Marquez', 'Navarro', 'Nielsen', 'Raymond', 'Gonzalez', 'Hamilton', 'Rutledge', 'Cleveland', 'Hendricks', 'Richardson']
```

4.2) Extend the pipeline so that it produces the following output:
```c++
sorted: [('Cox', 'Xoc', 3), ('Ray', 'Yar', 3), ('Brock', 'Kcorb', 5), ('Casey', 'Yesac', 5), ('Crane', 'Enarc', 5), ('Gomez', 'Zemog', 5), ('Petty', 'Yttep', 5), ('Vance', 'Ecnav', 5), ('Bernard', 'Dranreb', 7), ('Buckner', 'Renkcub', 7), ('Marquez', 'Zeuqram', 7), ('Navarro', 'Orravan', 7), ('Nielsen', 'Neslein', 7), ('Raymond', 'Dnomyar', 7), ('Cleveland', 'Dnalevelc', 9), ('Hendricks', 'Skcirdneh', 9)]
\\
16 odd-length names found.
```


&nbsp;
### 5.) Challenge: Pipeline for Product Codes

Build a pipeline that produces batches of five 6-digit numbers with prefix 'X'.
Numbers are in ascending order within each batch and end with a 1-digit checksum
after a dash. The checksum is the sum of all six digits of the random number modulo 10.

Output:
```c++
batch 1: ['X102042-9', 'X102180-2', 'X103228-6', 'X104680-9', 'X106782-4']
batch 2: ['X200064-2', 'X200732-4', 'X202090-3', 'X209056-2', 'X211464-8']
batch 3: ['X300186-8', 'X301416-5', 'X305962-5', 'X307938-0', 'X312524-7']
batch 4: ['X400216-3', 'X401436-8', 'X401682-1', 'X405256-2', 'X406376-6']
```

5.1) Alter the pipeline such that it produces only even digit codes:
```c++
batch 1: ['X226840-2', 'X284240-0', 'X448288-4', 'X804080-0', 'X888620-2']
batch 2: ['X220640-4', 'X248066-6', 'X648466-4', 'X680404-2', 'X882868-0']
batch 3: ['X262626-4', 'X608662-8', 'X626404-2', 'X662424-4', 'X846228-0']
batch 4: ['X224200-0', 'X282204-8', 'X448426-8', 'X600282-8', 'X802882-8']
```


&nbsp;
### 6.) Challenge: Run Unit Tests

Pull file
[test_stream.py](test_stream.py)

Output:

Ran 12 tests in 0.001s

OK
Unit testing using test objects:
 - test_filter_1()
 - test_filter_11()
 - test_filter_12()
 - test_filter_13()
 - test_map_2()
 - test_map_21()
 - test_reduce_3()
 - test_reduce_31()
 - test_sort_4()
 - test_sort_41()
 - test_sort_42()
 - test_stream_generation()
---> 12/12 TESTS SUCCEEDED
```


&nbsp;
### 7.) Challenge: Sign-off

For sign-off, change into `E_streams` directory and copy commands into a terminal:


Result:

```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  6264  100  6264    0     0  38354      0 --:--:-- --:--:-- --:--:-- 38666
Unit testing using test objects:
<stdin>:153: DeprecationWarning: unittest.makeSuite() is deprecated and will be
removed in Python 3.13. Please use unittest.TestLoader.loadTestsFromTestCase() i
nstead.
----------------------------------------------------------------------
Ran 12 tests in 0.001s

OK
```

12 tests succeeded.

