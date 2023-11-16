# Artificial-Intelligence
![image](https://github.com/mjmaher987/Artificial-Intelligence/assets/77095635/1b6ddfe3-5207-4bb0-9ecd-960ba3024ba9)

## General Information
* Author: Mohammad Javad Maheronnaghsh
* Last Update: October 25th, 2023

## Adversarial Search
### What is it?
Adversarial search is like a strategy game between two players, where one player tries to make the best moves to win, while the other player tries to stop them. It's used in things like chess or tic-tac-toe, where we plan your moves while thinking about what our opponent might do to counter our plans.
### What did I implement?
As you can see in the following picture, this is a Game between 2 players (red and blue) to draw the map. There is another rule in the game that we have some walls (drawn in yellow). If a player enters the yellow area, it will draw walls till it enters the yellow area again.
Note that a player defeats when it doesn't have any choice.

I have implemented this game in 3 modes:
- Min-max vs. Min-max
- Min-max vs. Random Walk
- Random Walk vs. Random Walk

And compare the results with each other which you can see in the "main.ipynb" file.
![image](https://github.com/mjmaher987/Artificial-Intelligence/assets/77095635/4764a30e-e26c-454f-a368-fd462c884adf)


## Local Search
### What is it?
In local search, we begin with a solution and try to make it better by making small changes. It's like trying to find a better route to visit cities one by one in the Traveling Salesman Problem by re-arranging them slightly. We keep doing this until you can't make it any better. It's a way to find a good solution, even if it's not necessarily the best one.

### What did I implement?
As you can see in the picture, we have some cities in beginning and want to travel between them, reaching all cities and get back to the first city again.

![image](https://github.com/mjmaher987/Artificial-Intelligence/assets/77095635/0bc4e5ba-025f-4256-b3b0-40c30321b5af)

I have implemented 3 different algorithms to do that:
#### Hill Climbing
![image](https://github.com/mjmaher987/Artificial-Intelligence/assets/77095635/72349f06-8b55-40f9-bd4a-e29f927b66d0)
#### Simulated Annealing
![image](https://github.com/mjmaher987/Artificial-Intelligence/assets/77095635/b56a8514-2bd7-4331-b5cb-511e3d754741)
#### Genetic Algorithm
![image](https://github.com/mjmaher987/Artificial-Intelligence/assets/77095635/d0f84c24-a9ed-4084-93a0-2b5e9e8f54a8)




## Informed Search
### What is it?
Informed search, like A* with heuristics, is like using a map to find the quickest way to your destination. It considers both how far we've traveled (the cost) and an estimate of how much is left (the heuristic) to guide us towards the best path. This helps us make smarter decisions to reach our goal more efficiently.
### What did I implement?
We have a table like this:

![image](https://github.com/mjmaher987/Artificial-Intelligence/assets/77095635/446f5e7e-bd4c-4e22-ba44-89046fdbe327)

And we want to reach this one (for instance):

![image](https://github.com/mjmaher987/Artificial-Intelligence/assets/77095635/a2dafcc8-7753-4cdf-a418-067a9236299a)

The starting and final tables are given in this format:

![image](https://github.com/mjmaher987/Artificial-Intelligence/assets/77095635/1a219e6b-3c4c-458d-ac82-5780b502fc80)

The allowed actions are moving an arbitrary column upward or downward **OR** moving an arbitrary row to left of right. Note that the cells are circularly shifted.

I used my own heuristic which you can find more on the repository.


## Optimization
### What is it?
Optimization is the key component used in ML and AI pipelines. We use it to reach the optimum point that our algorithm/model works best. 

Gradient Descent plays a pivotal role in the optimization process. In the followint, I am going to tell more explanations about what I have implemented:
- Optimization: Optimization is like finding the **best solution** to a problem. It's about making things as good as they can be. For example, imagine we have a limited amount of money and we want to buy the most things with it. We're optimizing our spending to get the most value.
- Gradient Descent: This is a method used in optimization. Imagine we're trying to find the highest point on a hilly terrain but can't see the whole landscape. So, we **take a step** in the direction that **looks steepest uphill**. We keep doing this until we reach the highest point. This step-by-step process of finding the best point is like gradient descent.

### What did I implement?
#### Derivatives of some Functions
![image](https://github.com/mjmaher987/Artificial-Intelligence/assets/77095635/05ae4c25-6787-45b4-8c78-1e7cf4dbacf2)
#### Gradient Descent (1D)
- Learning Rate = 0.1
  
![image](https://github.com/mjmaher987/Artificial-Intelligence/assets/77095635/0c2a2712-7767-4a53-8382-cb596a66431a)

- Learning Rate = 0.5
  
![image](https://github.com/mjmaher987/Artificial-Intelligence/assets/77095635/39acfd2b-f120-47be-93fa-ae56d4a5c3f2)

- Learning Rate = 0.001
  
![image](https://github.com/mjmaher987/Artificial-Intelligence/assets/77095635/82e16d49-9631-42c7-9dd3-4da8eddbabf7)
#### Gradient Descent (2D)
![image](https://github.com/mjmaher987/Artificial-Intelligence/assets/77095635/823b8e66-c3f3-437c-8ac3-93bff1323541)

## Reinforcement Learning
### What is it?
Reinforcement learning (RL) is a machine learning approach based on rewarding desired behaviors and punishing undesired ones. In RL, an agent learns by interacting with its environment and receiving positive or negative feedback for its actions.

The agent seeks to maximize cumulative reward through trial and error. Key elements of reinforcement learning include:

- Agent - The learner and decision maker
- Actions - Possible moves the agent can make
- Environment - The agent's surrounding context
- States - The agent's situation at a given time
- Reward - Feedback for guiding the agent's learning
Unlike supervised learning which trains on example input-output pairs, RL agents learn from voluntary interaction. And unlike unsupervised learning which finds patterns in data, RL actively maximizes a reward signal.

### What did I implement?
We implemented a Q-Learning Algorithm on 2 envoronments:
#### Frozen Lake (Discrete)
- Before Training:

![naive](https://github.com/mjmaher987/Artificial-Intelligence/assets/77095635/4bdc077c-ef62-4661-9cb0-1a41bd1b8a43)

- After Training:

![professional](https://github.com/mjmaher987/Artificial-Intelligence/assets/77095635/c915f6cc-8735-4d6d-8c4c-ddcec90d6246)

#### Mountain Car (Continual)
- Before Training:

![mountain-1](https://github.com/mjmaher987/Artificial-Intelligence/assets/77095635/295d897a-da23-40c7-b93c-ed653b64d516)

- After Training:

![mountain-2](https://github.com/mjmaher987/Artificial-Intelligence/assets/77095635/ab943d37-8e69-4102-8fd2-4e2a442573b1)

## MDP (Markov Decision Processes)
### What is it?

### What did I implement?

## Particle Filtering
### What is it?

### What did I implement?

## Bayesian Networks
### What is it?

### What did I implement?

## Deep Learning
### What is it?

### What did I implement?


Other Topics:
uninformed search - csp - rl - mdp - bn - hmm - particle filtering - regression - classification - nn (neural networks)




## Ideas / Brain Stormings
- Reinforcement learning: growing a child, learning and understanding, and also voice recognition of animals (signal processing)
- CSP: assigning tasks to TAs regarding their abilities, interests, and the needs
- HMM: the unknown reseaon behind extending/not-extending the deadline by head TA
- Particle Filtering: Robot Navigation
- Bayesian Networks: Cause and Effects in Psychology
- Regression: X=behaviour and attributes of people   |   Y=GPA
- Classification: X=different attibutes of thinking     |    Classes=Nationalities

## TODOs
I kindly request other GitHub members (specially experts in AI) to contribute to this repository so that we can have a more valuable source of AI materials.

- Upload the lecture notes
- Upload useful slides
- Upload Useful assignments and answers
- Add links of useful courses (videos) and their assignments with answers
- The previous suggestion can be converted into a bank of questions that is useful for teaching assisstants to design homeworks
- Add same respositories


