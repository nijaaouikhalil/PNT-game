# PNT-game
* Submission for Assignment 3, COMP 472: Artificial Intelligence
* **Team Members:**
  * Adrian Patterson 40048841
  * Khalil Nijaoui 40092653
  * Michel Abboud 40025378
  * Karl-Joey Chami 27736657
## Goal
* In this assignment, we compute the best move for the current player of the PNT game given the state of the game. Only a single move is computed and is evaluated using a static board evaluation function.

## Submission Contents
* This submission contains:
	* `/test_cases`
		* Contains the test cases and their outputs for the computation (Given).
	* `/results`
		* Contains the results of previously ran computations
	* `/src`
		* Holds the source files for the project (i.e. .py files)
## How to Run
* Clone this repository
* Open in IDE of your choice (or command line)
* Navigate to the /src directory
* Run `ab_pruning.py <#_of_tokens> <#_of_taken_tokens> <list_of_taken_tokens> <max_depth>` and generated results will be outputted in a directory named `/results`
    * `<#_of_tokens>` represents the total amount of tokens in the current game.
    * `<#_of_taken_tokens>` represents the total amount of tokens already picked by a player in the current game.
    * `<list_of_taken_tokens>` is the list of values of all picked tokens in the current game.
    * `<max_depth>` is the depth of the search algorithm. A depth of 0 denotes full depth search.
* Example
    * `ab_pruning.py 10 4 5 8 2 1 4`
        * `<#_of_tokens>` is 10
        * `<#_of_taken_tokens>` is 4
        * `<list_of_taken_tokens>` is 5,8,2,1
        * `<max_depth>` is 4
