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

## Playing with DNA
DNA sequencing is the process of determining the nucleic acid sequence, i.e., the order of nucleotides in DNA. It includes any method or technology that is used to determine the order of the four bases: adenine (A), guanine (G), cytosine (C), and thymine (T).
In such a scenario, you are tasked with solving the following requests. You are free to tackle them in whichever manner you deem most reasonable, relying on data structures of your choice.

Task 1 - Basic sequencing
Given a sequence like "ACCGXXCXXGTTACTGGGCXTTGT" of nucleotides mixed up with other elements, return the sub-sequences containing only contiguous subsets of ACTG ordered by length. Example :  in = "ACCGXXCXXGTTACTGGGCXTTGT", out = ["GTTACTGGGC", "ACCG", "TTGT", "C"]

Task 2 - Counting bases
Given a sequence like "ACTWGTGCTYGATRGTAGCYZGTW", count bases and print out the distribution of the elements you find within the input sequence. For this task, take into account all the bases you may find, even those outside of the usual ACTG set.

Task 3 - Counting amino acids
Amino acids are identified by one (or more) among DNA codons, which are sequences of 3 bases, according to the following table. Given a DNA sequence, count the occurrences of each amino acid both by specific codons and by name. For instance, if you were to find both TTT and TTC, you would have two distinct codons accounting both for Phenylalanine.

>Solution in file : [Playing_with_DNA.ipynb](https://github.com/MarioFiorino/Python-Workouts/blob/main/Playing_with_DNA.ipynb)

## Titles trading

We want to manage a simplified trading market in which we have to keep tracks of stock titles and buy/sell operations. Each stock title is uniquely identified by an alphanumerical code. Each trading operation is characterised by the number of stocks of a given title effectively bought (or sold), the date/time of the operation and the price per stock. We are interested in keeping tracks of all the transactions for each title, the min/max/average stock price for a title in a given date and the overall number of stocks sold of a title in each date. Write a program taking into account the following tasks:

Devise an appropriate way to organise data in memory. -  Read titles and stock trades either from file or command line. -  Write a program that supports updating the available information introducing new titles, registering new operations and updating in turn the statistical values collected for each title.

>Solution in file : [Titles_trading.ipynb](https://github.com/MarioFiorino/Python-Workouts/blob/main/Titles_trading.ipynb))

## Deduction-based game

Implement a deduction-based game, where the user must guess a randomly generated three-digits value according to trial and errors (and clues). Whenever the user try to guess the number, one or more of the following response is generated:

Alfa if (at least) one correct digit is in the correct place;
Bravo if (at least) one correct digit is in the wrong place;
Charlie if no correct digits are present.

The program provide a response for all the conditions matched by the current guess. The user is granted a parametrized maximum number of guesses in which he has to successfully guess the number.

>Solution in file : [Deduction_based_game_3Digits.ipynb](https://github.com/MarioFiorino/Python-Workouts/blob/main/Deduction_based_game_3Digits.ipynb)

## Acrobatic gymnastics

Acrobatic gymnastics is a competitive gymnastic discipline where teams of gymnasts work together and perform routines consisting of acrobatic moves, dance and tumbling passes, set to music.
We are interested in modelling all the aspects pertaining to an acrobatic gymnastic competition.

>Solution in file : [Acrobatic_gymnastics.ipynb](https://github.com/MarioFiorino/Python-Workouts/blob/main/Acrobatic_gymnastics.ipynb)

## Doubly linked list

A linked list is a dynamic linear data structure used for storing collections of data. A linked list is represented as a collection of nodes, with a link between consecutive nodes. The number of nodes in a list is not fixed and can grow and shrink on demand. Each node of a linked list contains the data associated with a given node and a reference to the next node, in case of singly linked list. In this scenario, we are interested in keeping a reference to the previous node as well. The last node has a next reference to null. The first node has a previous reference to null. The entry point into a linked list is called the head of the list. The last node of a linked list is called the tail of the list. If the linked list is empty, then both head and tail are null references.

>Solution in file : [Doubly_linked_list.ipynb](https://github.com/MarioFiorino/Python-Workouts/blob/main/Doubly_linked_list.ipynb)

## Genetic algorithm, very easy version

Strive to algorithmically generate a breed of smarter dogs, i.e., generate a population of dogs with an average smart factor higher than a given threshold, starting from a population way duller than our target.

>Solution in file : [Easy_genetic_algorithm.ipynb](https://github.com/MarioFiorino/Python-Workouts/blob/main/Easy_genetic_algorithm.ipynb)

## Right triangles

Given an array of positive integers, find the number of orthogonal triangles that can be formed with three elements of this array.

>Solution in file : [right_triangles.py](https://github.com/MarioFiorino/Python-Workouts/blob/main/right_triangles.py)

## Mandelbrot Set

You are required to write a pure Python implementation of a function to evaluate the Mandelbrot set, using iteration, and a vectorized function using NumPy and its arrays. You then must evaluate and compare the performance of the two approaches.

>Solution in file : [Mandelbrot_Set_Compared.ipynb](https://github.com/MarioFiorino/Python-Workouts/blob/main/Mandelbrot_Set_Compared.ipynb)

## Descriptive analysis with Pandas

Take into account a dataset containing information regarding a market analysis in the mobile telephony sector. The dataset contains information regarding the technical characteristics of the devices and price ranges. The purpose of the analysis will be to study the various characteristics of the devices, in order to understand how these affect the price of the device.

>Solution in file : [Descriptive_Analysis_with_Pandas.ipynb](https://github.com/MarioFiorino/Python-Workouts/blob/main/Descriptive_Analysis_with_Pandas.ipynb)

## Weather Stations with NumPy 

Write a Python program to analyze atmospheric observations in file weather.csv using NumPy.

>Solution in file : [Weather_Stations_Stat.ipynb](https://github.com/MarioFiorino/Python-Workouts/blob/main/Weather_Stations_Stat.ipynb)

## Weather Stations with Pandas

Write a Python program to analyze atmospheric observations in file weather.csv using Pandas.

>Solution in file : [Pandas_Weather_Stations.ipynb](https://github.com/MarioFiorino/Python-Workouts/blob/main/Pandas_Weather_Stations.ipynb)

## At the Zoo

Using object-oriented programming (OOP), is defined a zoo, with cages and animals. In addition, is given the opportunity to formulate queries about animals present in zoo.

>In file : [At_the_zoo.ipynb](https://github.com/MarioFiorino/Python-Workouts/blob/main/At_the_zoo.ipynb)


## Work with files in Google Colab

Some instructions and tips on how to manage files in Colab cell

>In file : [Work_with_file_in_colab.ipynb](https://github.com/MarioFiorino/Python-Workouts/blob/main/Work_with_file_in_colab.ipynb)

>In file : [Work_with_file_in_colab_2.ipynb](https://github.com/MarioFiorino/Python-Workouts/blob/main/Work_with_file_in_colab_2.ipynb)


## Tips: strings, sets, lists, dictionaries

Some tips for using strings, sets, lists, and dictionaries

>In file : [str_set_list_dict.ipynb](https://github.com/MarioFiorino/Python-Workouts/blob/main/str_set_list_dict.ipynb)           
