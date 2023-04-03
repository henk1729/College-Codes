# DAA-Assignment

###### Contains the solution code for majority element using Divide and Conquer approach

#### Problem Statement:
Accept a one-dimensional array using random number generator. the array may be in the range of ```[0, 1, 2]```. (Only three numbers are permitted.)\
Scan the array and print ```X``` if number of ```0``` is more than number of ```1``` and ```2```.\
Print ```Y``` if number of ```1``` is more than number of ```0``` and ```2```.\
Print ```Z``` if number of ```2``` is more than number of ```0``` and ```1```.

#### Approach:
1. Create a vector ```cnt``` of size three for storing count of ```0```, ```1``` and ```2``` at respective indices.
2. Recursively divide the array into two halves from indices ```l``` to ```m-1``` and ```m+1``` to ```r``` where ```m```=```(l+r)/2```.
3. If the length of the subarray is less than or equal to ```2```, return maximum out of the three counts.
