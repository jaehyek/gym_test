import gym

import matplotlib.pyplot as plt
import cv2

def main():
    # env = gym.make("Breakout-v4", render_mode='human')
    env = gym.make('CartPole-v1')
    observation, info = env.reset(seed=42, return_info=True)

    for loop in range(1000):
        print(f'loop:{loop}')
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        # env.render()
        img = env.render(mode='rgb_array')
        plt.imshow( img)

        if done:
            print(f'done')
            observation, info = env.reset(return_info=True)
    env.close()
    print('env closed')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


