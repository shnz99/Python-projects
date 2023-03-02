import gym
from stable_baselines3 import PPO
from stable_baselines3.ppo import MlpPolicy
from stable_baselines3.common.env_util import make_vec_env
import os
import time


models_dir = f"models/Mountain-Car"
if not os.path.exists(models_dir):
    os.makedirs(models_dir)

env = make_vec_env("MountainCarContinuous-v0", n_envs=1)

# The learning agent and hyperparameters
model = PPO(
    policy=MlpPolicy,
    env=env,
    seed=0,
    batch_size=256,
    ent_coef=0.00429,
    learning_rate=7.77e-05,
    n_epochs=10,
    n_steps=8,
    gae_lambda=0.9,
    gamma=0.9999,
    clip_range=0.1,
    max_grad_norm=5,
    vf_coef=0.19,
    use_sde=True,
    policy_kwargs=dict(log_std_init=-3.29, ortho_init=False),
    verbose=1,
)
# # Training and saving models along the way
TIMESTEPS = 1000
for _ in range(5):
    model.load(f"{models_dir}/best-car", env=env)
    for i in range(5):
        model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False)
        model.save(f"{models_dir}/best-car")
    del model

# Check model performance
# load the best model you observed from tensorboard - the one reach the goal/ obtaining highest return
models_dir = "models/Mountain-Car"
model_path = f"{models_dir}/best-car"
model.load(model_path, env=env)
obs = env.reset()
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()
