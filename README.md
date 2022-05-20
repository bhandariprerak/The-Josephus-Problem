# The-Josephus-Problem
In computer science and mathematics, the Josephus Problem (or Josephus permutation) is a theoretical problem.
Following is the problem statement:  
There are n people standing in a circle waiting to be executed. The counting out begins at some point in the circle and proceeds around the circle in a fixed direction. In each step, a certain number of people are skipped and the next person is executed. The elimination proceeds around the circle (which is becoming smaller and smaller as the executed people are removed), until only the last person remains, who is given freedom. Given the total number of persons n and a number k which indicates the starting position from where the execution begins. The task is to choose the place in the initial circle so that you are the last one remaining and so survive.
Here in every turn the person next in number is killed i.e, the adjacent person.
For example, if n = 5 and k = 1, then the safe position is 3. Firstly, the person at position 2 is killed, then person at position 4 is killed, then person at position 1 is killed. Finally, the person at position 5 is killed. So the person at position 3 survives.  
