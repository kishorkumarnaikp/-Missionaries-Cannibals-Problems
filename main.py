from queue import PriorityQueue  # Importing the PriorityQueue class from the queue module

# Define the state class
class State:
    def __init__(self, missionaries, cannibals, boat_side):
        self.m = missionaries  # Number of missionaries on the current side
        self.c = cannibals  # Number of cannibals on the current side
        self.b = boat_side  # Side of the boat (0 for left, 1 for right)
    
    # Define equality between two states
    def __eq__(self, other):
        return self.m == other.m and self.c == other.c and self.b == other.b
    
    # Define comparison between two states based on heuristic value
    def __lt__(self, other):
        return (self.m + self.c) < (other.m + other.c)
    
    # Define hash function for state objects
    def __hash__(self):
        return hash((self.m, self.c, self.b))
    
    # Define string representation of a state
    def __str__(self):
        return f"M: {self.m}, C: {self.c}, Boat: {'left' if self.b == 0 else 'right'}"

# Define the successors function to generate possible next states
def successors(state):
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]  # Possible moves: (m, c)
    for move in moves:
        if state.b == 0:  # If the boat is on the left side
            new_state = State(state.m - move[0], state.c - move[1], 1)  # Move from left to right
        else:  # If the boat is on the right side
            new_state = State(state.m + move[0], state.c + move[1], 0)  # Move from right to left
        if is_valid(new_state):  # Check if the new state is valid
            yield new_state  # Yield the valid new state as a successor

# Define the validity check function
def is_valid(state):
    if state.m < 0 or state.c < 0 or state.m > 3 or state.c > 3:  # Check if missionaries and cannibals are within bounds
        return False
    if state.m != 0 and state.m < state.c:  # Check if missionaries are outnumbered by cannibals on the left side
        return False
    if state.m != 3 and 3 - state.m < 3 - state.c:  # Check if missionaries are outnumbered by cannibals on the right side
        return False
    return True

# Define the best-first search function
def best_first_search():
    start_state = State(3, 3, 0)  # Start state with all missionaries and cannibals on the left side
    frontier = PriorityQueue()  # Priority queue to store states based on heuristic values
    frontier.put(start_state)  # Put the start state into the priority queue
    visited = set()  # Set to store visited states
    while not frontier.empty():  # Continue until the priority queue is empty
        current_state = frontier.get()  # Get the state with the lowest heuristic value from the priority queue
        if current_state == goal_state:  # If the current state is the goal state
            return current_state  # Return the solution
        visited.add(current_state)  # Add the current state to the set of visited states
        for next_state in successors(current_state):  # Iterate over the successors of the current state
            if next_state not in visited:  # If the successor has not been visited
                frontier.put(next_state)  # Put the successor into the priority queue
    return None  # Return None if no solution is found

# Define the goal state
goal_state = State(0, 0, 1)  # Goal state with all missionaries and cannibals on the right side

# Main function
def main():
    result = best_first_search()  # Find the solution using best-first search
    if result:  # If a solution is found
        print("Solution found:", result)  # Print the solution
    else:  # If no solution is found
        print("No solution found.")  # Print a message indicating no solution

if __name__ == "__main__":
    main()  # Call the main function if the script is executed directly
