import time

import numpy as np
from .base import BaseSolver, one_step_lookahead


# Constants (default values unless provided by caller)
DISCOUNT = 0.9
THETA = 0.0001


# Adapted from https://github.com/dennybritz/reinforcement-learning/blob/master/DP/Policy%20Iteration%20Solution.ipynb
class PolicyIterationSolver(BaseSolver):

    def __init__(self, env, discount_factor=DISCOUNT, max_policy_eval_steps=None, theta=THETA, verbose=False,
                 minimum_steps=0):

        self._env = env.unwrapped

        self._policy = np.ones([self._env.nS, self._env.nA]) / self._env.nA
        self._discount_factor = discount_factor
        self._steps = 0
        self._last_delta = 0
        self._step_times = []
        self._policy_stable = False
        self._max_policy_eval_steps = max_policy_eval_steps
        self._theta = theta
        # Policy iteration shouldn't need a minimum steps (when it converges, it is always converged) but left this in
        # since it was here before, just made it easy to zero.
        self._minimum_steps = minimum_steps

        super(PolicyIterationSolver, self).__init__(verbose)

    def step(self):
        """
        Perform one iteration of Policy Iteration.
        
        Computes a new value function given current policy, then computes a new policy for all states given this value 
        function
        
        :return: Tuple of:
            (   
                policy,
                value function,
                total number of policy iterations performed so far,
                time required to compute this policy iteration,
                sum of rewards obtained by best action across all states,
                maximum change in value of a state in this policy iteration,
                boolean denoting whether the policy changed in this policy iteration,
            )
        """
        start_time = time.clock()
        # Evaluate the current policy
        V = self.evaluate_policy(self._policy, discount_factor=self._discount_factor,
                                 max_steps=self._max_policy_eval_steps, theta=self._theta)

        # Set to True if steps > 10, false otherwise; will be set to False if we make any changes to the policy
        self._policy_stable = self._steps >= self._minimum_steps
        delta = 0
        reward = 0  # float('-inf')
        # For each state...
        for s in range(self._env.nS):
            # The best action we would take under the current policy
            chosen_a = np.argmax(self._policy[s])

            # Find the best action by one-step lookahead
            # Ties are resolved arbitrarily
            action_values = one_step_lookahead(self._env, self._discount_factor, s, V)
            best_a = np.argmax(action_values)
            best_action_value = np.max(action_values)

            # Calculate delta across all states seen so far
            delta = max(delta, np.abs(best_action_value - V[s]))
            reward += best_action_value

            # Greedily update the policy
            if chosen_a != best_a:
                self._policy_stable = False
            self._policy[s] = np.eye(self._env.nA)[best_a]

        self._steps += 1
        self._step_times.append(time.clock() - start_time)
        self._last_delta = delta

        return self._policy, V, self._steps, self._step_times[-1], reward, delta, self._policy_stable

    def reset(self):
        self._policy = np.ones([self._env.nS, self._env.nA]) / self._env.nA
        self._steps = 0
        self._step_times = []
        self._last_delta = 0
        self._policy_stable = False

    def has_converged(self):
        return self._policy_stable

    def get_convergence(self):
        return self._last_delta

    def run_until_converged(self):
        while not self.has_converged():
            self.step()

    def get_environment(self):
        return self._env

