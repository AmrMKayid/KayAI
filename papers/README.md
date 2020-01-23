<h1 align=center> Papers </h1>

## Learning by cheating:
### Summary:
  - decomposing learning problem into two stages
    - train an agent that has access to privileged information. (Learning to ACT)
    - the privileged agent acts as a teacher that trains a purely vision-based sensorimotor agent. (Learning to SEE)
  - The approach achieves 
    - 100% success rate on all tasks in the original CARLA benchmark using (**CARLA ≤0.9.5**)
    - sets a new record on the NoCrash benchmark
      - achieving 100% success rate in the _Empty_ condition 
      - and reaching 85% success rate or higher in other conditions.

### Notes:
  - A recent study argues that even with tens of millions of examples, direct imitation learning does not yield satisfactory driving policies 
  - the representation we use (a bird’s-eye view) enables **simple and effective data augmentation** that facilitates _generalization_.

### Questions:
  - Can we convert the imitation-learning dataset to match the (bird's-eye view)? (Semantic Segmentation, GANs, ...!?)
  - What kind of methods we can use for effective data augmentation on the existing imitation learning dataset? (IMPORTANT)
  - Can we get rid of the (privileged agent or AutoPilot) and replace it with RL agent?!
  - Is it possible to generate the **map M** of the privileged agent?
  - What will happen if we add trajectory noise by shifting and rotating imitation-learning dataset and propagating the same geometric transformations? 
    - will it me similar to the noise applied to the ground-truth map M?
  - Why the accuracy of LBC _decreased_ when using **CARLA 0.9.6** on the _**NoCrash benchmark**_ in the test town?