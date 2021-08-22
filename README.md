# Rush-hour
The puzzle called "Rush Hour" (c. ThinkFun, Inc., www.thinkfun.com) begins 
with a six-by-six grid of squares. Little plastic cars and trucks are distributed 
across the grid in such a way as to prevent one special car from moving off the 
grid, thereby escaping the traffic jam. The initial configuration of cars and trucks 
is preordained by a set of cards, each containing a different starting pattern. A 
player draws a card from the deck of cards, sets up the cars and trucks according 
to the pattern, and then tries to move the special car off the grid by sliding the 
cars and trucks up and down or left and right, depending on the starting 
orientation of the cars and trucks.
The grid looks something like this:
---------------------------
| --- --- --- --- --- --- |
| | | | | | | | |
| --- --- --- --- --- --- |
| | | | | | | | |
| --- --- --- --- --- --- |
| | | | | | | | <-- this is the only 
| --- --- --- --- --- --- | escape from the grid
| | | | | | | | |
| --- --- --- --- --- --- |
| | | | | | | | |
| --- --- --- --- --- --- |
| | | | | | | | |
| --- --- --- --- --- --- |
---------------------------
Cars occupy two contiguous squares, while trucks occupy three contiguous 
squares. All vehicles are oriented horizontally or vertically, never on the 
diagonal. Vehicles that are oriented horizontally may only move horizontally; 
vehicles that are oriented vertically may only move vertically. Vehicles may not 
be lifted from the grid, and there is never any diagonal movement. Vehicles may 
not be partially on the grid and partially off the grid.
The special car is called the X car. We'll represent it on the grid as two 
contiguous squares with the letter X in them. (We'll represent all other cars and 
trucks with different letters of the alphabet, but the special car will always be 
labeled with the letter X.) The X car is always oriented horizontally on the third 
row from the top; otherwise, the X car could never escape. If it were the only car 
on the grid, it might look like this (although it could start anywhere on that third 
row):
---------------------------
| --- --- --- --- --- --- |
| | | | | | | | |
| --- --- --- --- --- --- |
| | | | | | | | |
| --- --- --- --- --- --- |
| | X | X | | | | | <-- the X car will 
| --- --- --- --- --- --- | always start on 
| | | | | | | | | this row
| --- --- --- --- --- --- |
| | | | | | | | |
| --- --- --- --- --- --- |
| | | | | | | | |
| --- --- --- --- --- --- |
---------------------------
Let's put a blocking car and a blocking truck on the grid now too. We'll label the 
car as A and the truck as B:
---------------------------
| --- --- --- --- --- --- |
| | | | B | | | | |
| --- --- --- --- --- --- |
| | | | B | | | | |
| --- --- --- --- --- --- |
| | X | X | B | | | | 
| --- --- --- --- --- --- |
| | | | A | A | | | |
| --- --- --- --- --- --- |
| | | | | | | | |
| --- --- --- --- --- --- |
| | | | | | | | |
| --- --- --- --- --- --- |
---------------------------
Car A is oriented horizontally on the fourth row, and it can slide only left or 
right. Truck B is oriented vertically in the third column from the left, and it can 
slide only up or down. If this configuration were the starting state for a puzzle, it 
would be pretty simple for us to solve it. To slide the X car all the way to the 
right and off the grid, we'd have to move the B truck out of the way. But to move 
the B truck, we'll first have to move the A car out of the B truck's path. So the 
first solution step might be to move the A car to the right by one square:
---------------------------
| --- --- --- --- --- --- |
| | | | B | | | | |
| --- --- --- --- --- --- |
| | | | B | | | | |
| --- --- --- --- --- --- |
| | X | X | B | | | | 
| --- --- --- --- --- --- |
| | | | | A | A | | |
| --- --- --- --- --- --- |
| | | | | | | | |
| --- --- --- --- --- --- |
| | | | | | | | |
| --- --- --- --- --- --- |
---------------------------
Note that moving the A car further to the right works, as does moving it two 
squares to the left, but the best solution would move the X car off the grid in the fewest 
moves possible. When any car or truck is moved one square in any direction, that 
adds one to the total number of moves. If a car or truck is moved one square in 
one direction, then later is moved back one square to where it started, that counts 
as two moves.
The next step would be to slide the B truck down three squares:
---------------------------
| --- --- --- --- --- --- |
| | | | | | | | |
| --- --- --- --- --- --- |
| | | | | | | | |
| --- --- --- --- --- --- |
| | X | X | | | | | 
| --- --- --- --- --- --- |
| | | | B | A | A | | |
| --- --- --- --- --- --- |
| | | | B | | | | |
| --- --- --- --- --- --- |
| | | | B | | | | |
| --- --- --- --- --- --- |
---------------------------
Now it's possible to move the X car all the way to the right and off the grid. It's 
not necessary to move it off the grid though; it's sufficient to move the X car to 
cover the rightmost two squares of the third row from the top:
---------------------------
| --- --- --- --- --- --- |
| | | | | | | | |
| --- --- --- --- --- --- |
| | | | | | | | |
| --- --- --- --- --- --- |
| | | | | | X | X | 
| --- --- --- --- --- --- |
| | | | B | A | A | | |
| --- --- --- --- --- --- |
| | | | B | | | | |
| --- --- --- --- --- --- |
| | | | B | | | | |
| --- --- --- --- --- --- |
---------------------------
Now we've solved the puzzle. Let's take another look at solving this "Rush 
Hour" puzzle, but this time from the perspective of a best-first search. The initial 
state in the state space may be any configuration of cars and trucks such that the 
X car is always oriented horizontally on the third row from the top. The goal 
state is any configuration of cars and trucks that can be obtained through correct 
application of the operators, such that the X car covers the rightmost two squares 
of the third row from the top. The operators are simply these: move a 
horizontally-oriented vehicle one square to the left, move a horizontally-oriented 
vehicle one square to the right, move a vertically-oriented vehicle one square up, 
and move a vertically-oriented vehicle one square down.
Your assignment is to use Python to write a program called rushhour which 
employs best-first search with the A* algorithm to solve a "Rush Hour" puzzle 
with any legal initial state. Your rushhour program expects two arguments. 
The second argument is a description of the initial-state as a list of six strings, 
each string containing six characters. For this initial configuration:
---------------------------
| --- --- --- --- --- --- |
| | | | B | | | | |
| --- --- --- --- --- --- |
| | | | B | | | | |
| --- --- --- --- --- --- |
| | X | X | B | | | | 
| --- --- --- --- --- --- |
| | | | A | A | | | |
| --- --- --- --- --- --- |
| | | | | | | | |
| --- --- --- --- --- --- |
| | | | | | | | |
| --- --- --- --- --- --- |
---------------------------
the list of strings passed to rushhour would look like this:
["--B---","--B---","XXB---","--AA--","------","------"]
The first string corresponds to the top row, the second string corresponds to the 
next row down, and so on. If this list were formatted nicely, it would look more 
like the grid above:
["--B---",
 "--B---",
 "XXB---",
 "--AA--",
 "------",
 "------"]
We don't need to pass the goal state, as it will always be the same regardless of 
the initial state. The goal state will always be a legally-obtained configuration of 
cars and trucks with the X car on the rightmost two squares of the third row.
When (if?) the goal has been reached, rushhour should terminate and print a 
list of successive states that constitutes the path from the initial state to the goal 
state. So, if your TA invokes rushhour in this way (we'll explain that integer in 
the first argument later):
>>> rushhour(0, ["--B---","--B---","XXB---","--AA--",
"------","------"])
your program should print a solution like this:
 --B---
 --B---
 XXB---
 --AA--
 ------
 ------
--B---
 --B---
 XXB---
 ---AA-
 ------
 ------
------
 --B---
 XXB---
 --BAA-
 ------
 ------
------
 ------
 XXB---
 --BAA-
 --B---
 ------
------
 ------
 XX----
 --BAA-
 --B---
 --B---
------
 ------
 -XX---
 --BAA-
--B---
 --B---
------
 ------
 --XX--
 --BAA-
 --B---
 --B---
------
 ------
 ---XX-
 --BAA-
 --B---
 --B---
------
 ------
 ----XX
 --BAA-
 --B---
 --B---
Total moves: 8
Total states explored: 37
