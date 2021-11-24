import torch
import random
import numpy as np
from dinogame import dinoGameAI
from collections import deque

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

class Agent:

    def __init__(self):
        self.n_games = 0
        self.epsilon = 0 #randomness
        self.gamma = 0
        self.memory = deque(maxlen=MAX_MEMORY)
        self.model = None #TODO
        self.trainer = None #TODO


    def get_state(self, game):
        isJump = game.dino.isJump
        isDuck = game.dino.isDuck
        distanceToNextObstacle = game.distanceNextObstacle
        state = [isJump, isDuck, distanceToNextObstacle]
        np.array(state, dtype=int)

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE)
        else:
            mini_sample = self.memory

        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)

    def train_short_memory(self, state, action, reward, next_state, done):
        self.trainer.train_step(state, action, reward, next_state, done)

    def get_action(self, state):
        #random moves: tradeoff exploration / exploitation
        self.epsilon = 80 - self.n_games
        final_move = [0,0]
        if random.randint(0, 200) < self.epsilon:
            move = random.randint(0,1)
            final_move[move] = 1
        else:
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model.predict(state0)
            move = torch.argmax(prediction).item()
            final_move[move] = move
        
        return final_move

    def train():
        plot_scores = []
        plot_mean_scores = []
        total_score = 0
        record = 0
        agent = Agent()
        game = dinoGameAI()
        while True:
            #get old state
            state_old = agent.get_state(game)

            #get move
            final_move = agent.get_action(state_old)

            #perform move
            reward, done, score = game.play_step(final_move)
            state_new = agent.get_state(game)

            #train short mem
            agent.train_short_memory(state_old, final_move, reward, state_new, done)

            #remember
            agent.remember(state_old, final_move, reward, state_new, done)

            if done:
                #train long memory, plot result
                game.reset()
                agent.n_games += 1
                agent.train_long_memory()

                if score > record:
                    record = score
                    #agent.model.save()

                print('Game: ',agent.n_games, 'Sore: ', score, 'Record: ',record)


    if __name__ == '__main__':
        train()