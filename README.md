What is this?
=============

Bunny Islands is a puzzle game for the Sugar desktop.

![image](https://github.com/user-attachments/assets/dd8e11b2-bb73-4f79-ac82-2fe608b15969)

There are 6 pieces of a puzzle. On each piece, there's a bunny which is either colored red or green. The goal of the puzzle is to organise each piece on the board in such a fashion that the red colored bunnies and green colored bunnies are never on the same island. There are 400+ solutions to this puzzle. 


How to use?
===========

Bunny Islands can be run on the Sugar desktop.  Please refer to;

* [How to Get Sugar on sugarlabs.org](https://sugarlabs.org/),
* [How to use Sugar](https://help.sugarlabs.org/)

How to run?
=================

Dependencies:- 
- Python >= 3.10
- PyGObject >= 3.42
- PyGame >= 2.5
  
These dependencies need to be manually installed on Debian, Ubuntu and Fedora distributions.


**Running outside Sugar**


- Install the dependencies

- Clone the repo and run -
```
git clone https://github.com/vaibhav-sangwan/bunny-islands.git
cd bunny-islands
python main.py
```

**Running inside Sugar**

- Open Terminal activity and change to the Bunny Islands activity directory
```
cd activities\BunnyIslands.activity
```
- To run
```
sugar-activity3 .
```
