#  Missionaries-Cannibals Problem: Best First Search Algorithm

## Overview
This repository provides a solution to the classic Missionaries-Cannibals problem using the Best First Search algorithm. The problem involves three missionaries and three cannibals who must cross a river using a boat that can carry at most two people. The goal is to ensure that at no point do the cannibals outnumber the missionaries on either side of the river, to prevent the missionaries from being eaten.

## Problem Description
### Rules
1. The boat can carry a maximum of two people.
2. There must be at least one person on the boat to row it.
3. If cannibals ever outnumber missionaries on either side of the river, the missionaries will be eaten.
   
### Objective
Safely transport all missionaries and cannibals from the left bank to the right bank of the river.

## Algorithm: Best First Search
Best First Search (BFS) is a search algorithm that explores a graph by expanding the most promising node chosen according to a specified rule. This implementation uses a heuristic to guide the search towards the goal state efficiently.

## Heuristic Function
The heuristic function is critical for the Best First Search algorithm. For the Missionaries-Cannibals problem, a suitable heuristic could be the number of people left to move to the other side of the river.

Repository Contents
README.md: This document.
1. Problem Description: Detailed explanation of the problem.
2. Algorithm Explanation: Step-by-step guide on the Best First Search algorithm used.
3. Heuristic Explanation: Rationale behind the chosen heuristic.
4. Solution Implementation: A walkthrough of how the algorithm is implemented to solve the problem.
5. State Representation: Description of how the state of the problem is represented in the implementation.
6. Result Analysis: Analysis of the solution's performance and effectiveness.

```python
https://github.com/kishorkumarnaikp/-Missionaries-Cannibals-Problems.git
