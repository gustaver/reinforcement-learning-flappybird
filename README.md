# Machine Learning Flappy Bird
This is a supervised machine learning algorithm (support vector machine with a linear kernel) that I built into a Python version of Flappy Bird.

#Introduction
The game is currently in its infancy, and the interface for the user is perhaps
a bit clunky. However, it's pretty straightforward: you play, the bird learns,
the machine plays (don't worry, it's not smart enough to be a Terminator).

#How to play:
To run the game, simply type python flappy-auto-learn.py in the terminal. Make sure you have SciPy, Numpy and Scikit-learn installed ("pip install scipy", "pip install numpy", "pip install scikit-learn").

The game starts in training mode, where the player can play and the players choices will be recorded. After sufficient play, the player can press "t" to activate learning mode, where the algorithm will learn the training data (this can take signifcant time based on the size of the training data). Otherwise the game will automatically traing the algorithms at peiods when the dataset has 500*2^n n=1,2,3... datapoints. Once the training is done, the player can press "a" to initialize auto mode, where the algorithm will automatically make choices based on the game state. Keys "w" and "r" are used to write/read the training data respectively. Keys "s" and "f" are used to write/read the classifier algorithm respectively (a classifier is provided out of the box, but it's not great since it's only been training for 3 minutes). Key "p" can be used during play to print training information to the terminal.

#Enjoy!
