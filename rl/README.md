<h1 align=center> RL </h1>

> “RL is the third camp and lays somewhere in between full supervision and a complete lack of predefined labels. On the one hand, it uses many well-established methods of supervised learning such as deep neural networks for function approximation, stochastic gradient descent, and back-propagation, to learn data representation. On the other hand, it usually applies them in a different way.”


## Notes:
  - The interaction between the agent and the environment involves a sequence of actions and observed rewards in time
    - >Thus the interaction sequence is fully described by one **episode** (also known as “trial” or “trajectory”).
  - one **transition** step, represented by a tuple (s, a, s’, r)
  - **Policy**, as the agent’s behavior function π, tells us which action to take in state s.
    - It is a mapping from state s to action a and can be either deterministic or stochastic
  - **Value function** measures the goodness of a state or how rewarding a state or an action is by a prediction of future reward
  - The discounting factor γ∈[0,1] penalize the rewards in the future
  - **Monte-Carlo, Temporal-Difference learning, and Dynamic Programming** for state value functions aim to learn the state/action value function and then to select actions accordingly.
  - **Policy Gradient** methods learn the policy directly with a parameterized function respect to θ, π(a|s;θ).

