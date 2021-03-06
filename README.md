# Python-Workouts
In this repository some proposed solutions (and some suggestions) to interesting exercises found on the web, in Python. New exercises and related solutions will be added. Requests to find solutions to Python problem of all kinds are welcome. Write me!


## Array subsets
Given an array of integers, divide the array into 2 subsets: A and B; while respecting the following conditions:
- The intersections of A and B is null
- The union A and B is equal to original array
- The number of elements in subset A is minimal
- The sum of A's elements is greater than the sum of B's elements

If more then one subset A exists, return the one with the maximal sum

>Solution in file : [array_subsets.py](https://github.com/MarioFiorino/Python-Workouts/blob/main/array_subsets.py)

## Degree of array and more

Given an array of integer, its degree is defined as the number of occurrences of the element that occurs most frequently in array.
Determine two properties:
- Degree of the array given
- The shortest sub-array that share that degree     

>Solution in file : [degree_of_array.py](https://github.com/MarioFiorino/Python-Workouts/blob/main/degree_of_array.py)

## Reverse array in k group

Given an array of integer, reverse the values of the array k at a time, and return the modified array.

k is a positive integer and is less than or equal to the length of the array. If the number of values is not a multiple of k then left-out values, in the end, should remain as it is.

E.g.:

input1  : l = [1,2,3,4,5,6], k = 2 ;  &nbsp; &nbsp; &nbsp; &nbsp;  output : [2,1,4,3,6,5]

input2  : l = [1,2,3,4,5,6], k = 4 ;  &nbsp; &nbsp; &nbsp; &nbsp; output : [4,3,2,1,5,6]

>Solution in file : [reverse_arr_kgroup.py](https://github.com/MarioFiorino/Python-Workouts/blob/main/reverse_arr_kgroup.py)

##  Sliding Window Maximum
Given an array of integer, there is a sliding window of size k which is moving from the very left of the array to the very right. Each time the sliding window moves right by one position. Return the maximun value for each sliding window.

E.g.:

input : [1,3,-1,-3,5,3,6,7], k = 3 ;  &nbsp; &nbsp; &nbsp; &nbsp;  output :   [3,3,5,5,6,7]

Explanation:    

[1  3  -1] -3  5  3  6  7    --->    3

 1 [3  -1  -3] 5  3  6  7    --->    3
 
 1  3 [-1  -3  5] 3  6  7    --->    5
 
 1  3  -1 [-3  5  3] 6  7    --->    5
 
 1  3  -1  -3 [5  3  6] 7    --->    6
 
 1  3  -1  -3  5 [3  6  7]   --->    7
 

>Solution in file : [Slid_Window_Max.py](https://github.com/MarioFiorino/Python-Workouts/blob/main/Slid_Window_Max.py)


## First repeated word in a sentence
Given an sentence, find the first repeated word. Note: each sentence is bounded by comma, colon, semicolon, ect.

E.g. : 

input : " We work hard becouse hard work pays."

output: "hard"

>Solution in file : [first_repeated_word.py ](https://github.com/MarioFiorino/Python-Workouts/blob/main/first_repeated_word.py)

>Solution, more complex version, in file : [first_repeated_word2.py ](https://github.com/MarioFiorino/Python-Workouts/blob/main/first_repeated_word2.py)

## Maximum difference records

Given an array of integers, without reordering, determine the maximum diffrence between any element and any prior smaller difference.

E.g. :

input : [15,3,7,6,2,1]

out : The maximum trailing record is  l[2] -  l[1]  = 4

>Solution in file : [max_diff_rec.py](https://github.com/MarioFiorino/Python-Workouts/blob/main/max_diff_rec.py)

## Minimum unique array sum

Given an array, increment any duplicate elements until all elements are unique. The sum of the elements must be the minimum possible.

>Solution in file : [minimum_unique_array_sum.py](https://github.com/MarioFiorino/Python-Workouts/blob/main/minimum_unique_array_sum.py)

## Motorcycles and cars in a garage

In a garage there are count 16 fuel tanks and 62 wheels among cars and motorcycles. How many motorcycles and how many cars there are in the garage?

>Solution in file : [moto_car_in_garage.py](https://github.com/MarioFiorino/Python-Workouts/blob/main/moto_car_in_garage.py)


## Right triangles

Given an array of positive integers, find the number of orthogonal triangles that can be formed with three elements of this array.

>Solution in file : [right_triangles.py](https://github.com/MarioFiorino/Python-Workouts/blob/main/right_triangles.py)

## At the Zoo

Using object-oriented programming (OOP), is defined a zoo, with cages and animals. In addition, is given the opportunity to formulate queries about animals present in zoo.

>In file : [At_the_zoo.ipynb](https://github.com/MarioFiorino/Python-Workouts/blob/main/At_the_zoo.ipynb)


## Work with files in Google Colab

Some instructions and tips on how to manage files in Colab cell

>In file : [Work_with_file_in_colab.ipynb](https://github.com/MarioFiorino/Python-Workouts/blob/main/Work_with_file_in_colab.ipynb)

## Tips: strings, sets, lists, dictionaries

Some tips for using strings, sets, lists, and dictionaries

>In file : [str_set_list_dict.ipynb](https://github.com/MarioFiorino/Python-Workouts/blob/main/str_set_list_dict.ipynb)           
