# Artificial Neural Networks
- Class of machine learning techniques loosely inspired by the human nervous system
- They are analogous to support vector machines and other learning techniques
- The first type of neural network is a perceptron which is basically a binary classifier, used in handwriting analysis and computer vision.

## Perceptron
---
- Conceptionally very similar to support vector machine classification
- Support vector machine is a binary classifiers, they will be given a set of points and will put them into one of 2 categories 
- A support vector machine finds a ‘Hyperplane’ to neatly separate the two categories, and will be used to classify them
- Perceptrons are a specific algoritrhm to determine some hyperplane that separates the data, it looks for a way to seperate the point but doesn’t care about the hyperplane.
- Its said to learn online learning as it consumes one datapoint at a time, the training data is taken one datapoint at a time
- A new datapoint may come in and the hyperplane is moved accordingly . Th plane is moved in a way such that the iteration error is reduced
- It will converge to a particular solution in a finite number of steps only if the data is linearly separated
# Computer Vision
- Science of teaching a computer how to see, identify and extract information from images and videos and take decisions based on this info
## Handwritten Digit Recognition
---
- Handwritten digit recognition is what is started with normally, as the applications can be quite security heavy so high accuracy is needed
- These can be seen as classification problems, given a digit you need to classify it into a category 
- MNIST is a standard database of hand-written digit images and is used to train a classifier, images come with a label. There is also 10,000 images used to test the classifier
1. First the images need to be represented as a feature vector (a tuple of numbers)
2. Then you feed these feature vectors along with their labels, so the classification algorithm will learn
### Representing Images as Tuples
- The images are made of pixels, a pixel can be represented as a tuple, it will be (x-coor, y-coor, colour) , the colour can be represented as a tuple again (red, blue, green) , 3 for RGB and 1 for greyscale is the amount of numbers needed to represent the colour (channels)
- A greyscale image can be represented by a 2D array where the position is determined by the co-ordinates and the colour is on the array, this can be used directly as a feature vector
- If the image is full colour it will contain many redundant pixels, you could blur this and still reach a good conclusion (Dimensionality reduction)
- Using feature extraction techniques a small number of features can be used here, some may look for the edges and some may blur the image, recently unsupervised feature learning has been used to allow the learning algorithm to identify the relevant features without human intervention
- A simple method will be divide the image into a number of zones, count the number of black pixels and this will reduce the number of pixels. 
### Classification Algorithms
- There are many different choices for the classifictaion algorithms: Support vector machines, Logistic Regression, Random forrests for example. They are seen to perfom well
- One versus all classificaion is used to allow binary classifiers to be used. It finds many hyperplanes in combinations fo figure out which digit it is
- These days a popular algorithm to use is a deep learning network. They are hard to use as they need a large amount of computational power
# Deep Lerning Networks
- Network - Artificial Neural Networks
- The basic idea is that there is an input, it is fed through a network and an output isd produced. 
- In the network there are layers, the output of one layer is the input to the next. 
- Deep refers to the fact there are many layers.
- A perceptron can be represented as a network
- Feature vector is the input that has n numbers in the tuple, each represented by a node. Each input is multiplied by some weight and fed into an output node. The ouptut node processes these and produces an output
- The perceptron will take the form
```
if W1*X1 +W2*X2 +.... >R
    Then Output = 1
Else Output = 0
```
- The first line with >R replaced with = R is the equation of the hyperplane
- When you train a perceptron the aim is to find the weights W1, W2 ,... This is done by online learning
- To deal with more than 2 classes, as before all input nodes are multiplied by a weight and fed into a ndoe which processes them, however more than one node is added, each node will perform similarly, the weights are different and so the outputs will be different
- These nodes are then combined and fed into another node to give some final output. They could be cobined differntly again with a different node which could give anther output
- Each set of nodes is a layer. Input nodes are called input layer and simmilarly outout nodes are called output layers. The intermediate layers are called the hidden layer
- This type of netwrok is called a feed-forward neural network
- If every node in the pervious layer is connected to the layer it is called a dense layer
- To prevernt overfitting you can feed not all of the inputs from one layer to the next, this is called dropout
## Complete Training Process
---
1. Initialise some random weights
2. Find the Output
3. Evaluate some error function 
4. Adjust the weights by small incramnet
5. Repeat steps 2-4 until the error is minimized

