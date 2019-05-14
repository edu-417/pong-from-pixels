import numpy as np

import gym

env = gym.make("Pong-v0")

threshold = 0.5
observation = env.reset()

def random_policy():
    action = 2 if np.random.uniform() < threshold  else 3

    return action

while(True):
    env.render()
    action = random_policy()
    observation, reward, done, info = env.step(action)
    if(done):
        break

env.close()
