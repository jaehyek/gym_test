import gym
import cv2

# pip install gym[atari,accept-rom-license]==0.21.0

def main():
    # env = gym.make("Breakout-v4", render_mode='human')
    env = gym.make("BreakoutNoFrameskip-v4")
    # env = gym.make('CartPole-v1')
    observation, info = env.reset(seed=42, return_info=True)
    img = env.render(mode='rgb_array')
    h, w, c = img.shape         # type(img) = <class 'numpy.ndarray'>

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = 30
    filename_video ="record_breakout.mp4"
    cv2_video_writer = cv2.VideoWriter(filename_video, fourcc, fps, (w, h))

    for loop in range(1000):
        print(f'loop:{loop}')
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        # env.render()
        img = env.render(mode='rgb_array')
        cv2_video_writer.write(img[:,:,::-1])       # format change : rgb --> bgr

        if done:
            print(f'done')
            observation, info = env.reset(return_info=True)
    env.close()
    cv2_video_writer.release()
    print('env closed')


if __name__ == '__main__':
    main()


