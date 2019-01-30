# Machine Learning Flappy Bird

## Overview 
Flappy Bird game which has functionality for machine learning through [Supervised Learning](https://en.wikipedia.org/wiki/Supervised_learning) as well as [Reinforcement Learning](https://en.wikipedia.org/wiki/Reinforcement_learning). The agent makes decisions using an [Artificial Neural Network](https://en.wikipedia.org/wiki/Artificial_neural_network). The neural network should be initially trained by simply playing the game properly until a reasonable amount of data has been collected (≈2000 datapoints should work, use the **p** key to print data collection progress). Once a neural network has been trained, the agent can play autonomously by using the **a** key, and can further speed up data collection by pressing the **r** key. 

## How to run 

### Conda 
It is highly recommended that you use conda for simply installing all of the Python requirements to a virtual environment. Conda installation instructions can be found [here](https://conda.io/docs/user-guide/install/index.html). Once you have installed conda, follow the instructions below.

### Conda Environment 

1. From the root directory, create the conda environment using the bash command: 

```bash
conda env create -f environment.yml -n <ENVIRONMENT NAME> 
```

2. Activate the conda environment: 

```bash
source activate <ENVIRONMENT NAME> 
```

3. Start the game:

```bash
python flappy.py
```

## How to play
The agent will gather data appropriately from the player, then the following commands can be used to execute different procedures: 

```
p: Print the current state of the gathered training data to the terminal. 
t: Train the neural network on the collected data so far.
a: Switch autonomous mode on/off.  
r: Switch reinforcement learning speed-up on/off. 
```
