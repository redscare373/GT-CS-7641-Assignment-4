import gym
from gym.envs.registration import register

from .cliff_walking import *
from .frozen_lake import *


__all__ = ['RewardingFrozenLakeEnv', 'WindyCliffWalkingEnv']

register(
    id='RewardingFrozenLake4x4-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '4x4'},
)

register(
    id='RewardingFrozenLake8x8-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '8x8'}
)

register(
    id='RewardingFrozenLake15x15-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '15x15'}
)

register(
    id='RewardingFrozenLake20x20-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '20x20'}
)

register(
    id='RewardingFrozenLakeNoRewards4x4-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '4x4', 'rewarding': False}
)

register(
    id='RewardingFrozenLakeNoRewards8x8-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '8x8', 'rewarding': False}
)

register(
    id='RewardingFrozenLakeNoRewards15x15-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '15x15', 'rewarding': False}
)

register(
    id='RewardingFrozenLakeNoRewards20x20-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '20x20', 'rewarding': False}
)

register(
    id='WindyCliffWalking-v0',
    entry_point='environments:WindyCliffWalkingEnv',
)


#def get_rewarding_frozen_lake_environment():
#    return gym.make('RewardingFrozenLake4x4-v0')


def get_rewarding_frozen_lake_environment():
    return gym.make('RewardingFrozenLake8x8-v0')


#def get_large_rewarding_frozen_lake_environment():
#    return gym.make('RewardingFrozenLake12x12-v0')


def get_large_rewarding_frozen_lake_environment():
    return gym.make('RewardingFrozenLake15x15-v0')


#def get_large_rewarding_frozen_lake_environment():
#    return gym.make('RewardingFrozenLake20x20-v0')


def get_frozen_lake_environment():
    return gym.make('FrozenLake-v0')


#def get_rewarding_no_reward_frozen_lake_environment():
#    return gym.make('RewardingFrozenLakeNoRewards4x4-v0')


def get_rewarding_no_reward_frozen_lake_environment():
    return gym.make('RewardingFrozenLakeNoRewards8x8-v0')


#def get_large_rewarding_no_reward_frozen_lake_environment():
#    return gym.make('RewardingFrozenLakeNoRewards12x12-v0')


def get_large_rewarding_no_reward_frozen_lake_environment():
    return gym.make('RewardingFrozenLakeNoRewards15x15-v0')


#def get_large_rewarding_no_reward_frozen_lake_environment():
#    return gym.make('RewardingFrozenLakeNoRewards20x20-v0')


def get_cliff_walking_environment():
    return gym.make('CliffWalking-v0')


def get_windy_cliff_walking_environment():
    return gym.make('WindyCliffWalking-v0')

