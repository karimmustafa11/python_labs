#1. Given a list of numbers, create a function that returns a list where all similar adjacent elements have been reduced to a single element, so [1,2,3,3] returns [1,2,3]

def reduce_adjacent(lst):
    result = []
    
    for i in range(len(lst)):
        if i == 0 or lst[i] != lst[i-1]:
            result.append(lst[i])
    
    return result

lst = [1, 2, 3, 3]
print(reduce_adjacent(lst))  

#...................................................................



#2. Consider dividing a string into two halves
def split_combine(a, b):
    mid_a = (len(a) + 1) // 2 
    a_front = a[:mid_a]
    a_back = a[mid_a:]
    
    mid_b = (len(b) + 1) // 2
    b_front = b[:mid_b]
    b_back = b[mid_b:]
    
    return (a_front + b_front) + (a_back + b_back)

a = "abcd"
b = "ef"
print(split_combine(a, b))  

#.........................................................................


#3. Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each othe

def all_different(numbers):
    return len(numbers) == len(set(numbers))

print(all_different([1, 2, 7, 8]))  
print(all_different([1, 4, 3, 3, 6]))  

#.....................................................................

#4. Given unordered list, sort it using algorithm bubble sort (read about bubble sort and try to implement it
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

lst = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(lst))  

#.......................................................



#5.Guesses game

import random

def guess_game():
    while True:
        target = random.randint(1, 100)
        tries = 10
        print("You have 10 tries to guess the number between 1 and 100!")
        
        while tries > 0:
            try:
                guess = int(input(f"Tries left: {tries}, Enter your guess: "))
            except ValueError:
                print("Please enter a valid number!")
                continue
            
            if guess < 1 or guess > 100:
                print("Not allowed! The number must be between 1 and 100.")
                continue
            
            tries -= 1
            
            if guess == target:
                print(f"Congratulations! You guessed the number {target}!")
                break
            elif guess < target:
                print("The number is bigger!")
            else:
                print("The number is smaller!")
        
        if tries == 0 and guess != target:
            print(f"You ran out of tries! The number was {target}.")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

guess_game()