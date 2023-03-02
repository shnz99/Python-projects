import gym
import os
from stable_baselines3 import PPO
from stable_baselines3.ppo import MlpPolicy

models_dir = f"models/Cart-Pole"
if not os.path.exists(models_dir):
    os.makedirs(models_dir)

env = gym.make("CartPole-v1")

model = PPO(MlpPolicy, env, learning_rate=0.01, device="cuda", verbose=1)

TIMESTEPS = 1000
for _ in range(10):
    model = PPO.load(f"{models_dir}/test-best-model", env=env)
    for _ in range(10):
        model.learn(
            total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name="PPO"
        )
        model.save(f"{models_dir}/test-best-model")
    del model

model = PPO.load(f"{models_dir}/test-best-model", env=env)

####################################################################################################
################## VIDEO RECORDING #################################################################
os.system("Xvfb :1 -screen 0 1024x768x24 &")
os.environ["DISPLAY"] = ":1"
import base64
from pathlib import Path

from IPython import display as ipythondisplay


def show_videos(video_path="", prefix=""):
    """
    Taken from https://github.com/eleurent/highway-env

    :param video_path: (str) Path to the folder containing videos
    :param prefix: (str) Filter the video, showing only the only starting with this prefix
    """
    html = []
    for mp4 in Path(video_path).glob("{}*.mp4".format(prefix)):
        video_b64 = base64.b64encode(mp4.read_bytes())
        html.append(
            """<video alt="{}" autoplay
                    loop controls style="height: 400px;">
                    <source src="data:video/mp4;base64,{}" type="video/mp4" />
                </video>""".format(
                mp4, video_b64.decode("ascii")
            )
        )
    ipythondisplay.display(ipythondisplay.HTML(data="<br>".join(html)))


from stable_baselines3.common.vec_env import VecVideoRecorder, DummyVecEnv


def record_video(env_id, model, video_length=500, prefix="", video_folder="videos/"):
    """
    :param env_id: (str)
    :param model: (RL model)
    :param video_length: (int)
    :param prefix: (str)
    :param video_folder: (str)
    """
    eval_env = DummyVecEnv([lambda: gym.make("CartPole-v1")])
    # Start the video at step=0 and record 500 steps
    eval_env = VecVideoRecorder(
        eval_env,
        video_folder=video_folder,
        record_video_trigger=lambda step: step == 0,
        video_length=video_length,
        name_prefix=prefix,
    )

    obs = eval_env.reset()
    for _ in range(video_length):
        action, _ = model.predict(obs)
        obs, _, _, _ = eval_env.step(action)

    # Close the video recorder
    eval_env.close()


record_video("CartPole-v1", model, video_length=1000, prefix="ppo-cartpole")
show_videos(".day-videos", prefix="ppo")
