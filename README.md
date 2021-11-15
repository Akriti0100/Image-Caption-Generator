  <h1 align="center">
  <br>
<!--   <img src="https://github.com/Akriti0100/Human-Action-Recognition/blob/main/images/Jogging.gif" alt="Action" width="200"> -->
  <br>
  IMAGE CAPTION GENERATOR
  <br>
</h1>
<!-- 
<h3 align="center">Visit YouTube for Detailed Working: <a href="https://youtu.be/a7N-8x5jXFI" target="_blank"> human-actions.com </a></h3> -->

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-3.8.1-blue)
![Version](https://img.shields.io/badge/version-1.0.0-orange)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
[![License](https://img.shields.io/badge/license-%20GPL--3.0%20-blue)](https://github.com/Akriti0100/Antidote/blob/main/LICENSE.md)

<div align="justify">
<!-- # ?? Project overview -->

> As humans, we can easily interpret using the brain what an image is about, but is the computer able to recognize what the image represents? However, with the advances in the field of Deep Learning techniques and the availability of huge datasets one can build models which deal with understanding and language description of the image. It is a challenging task since generating well-formed sentences requires both syntatic and semantic understanding of the language. This task is significantly harder than image classification or the object recognition tasks which have been well-reasearched.
</div>

<p align="center">
  <a href="#project-scope">Project Scope</a> •
  <a href="#data-analysis">Data Analysis</a> •
  <a href="#model-used">Model Used</a> •
  <a href="#input-output-screenshots">I/O Screenshots</a> •
  <a href="#methodology-flowchart">Methodology Flowchart</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#license">License</a>
</p>

<div align="justify">
  
## PROJECT SCOPE

There are potentially a lot of applications of caption generation :

* It could have a great impact by helping visually impaired people to better understand the content of images. 
* It would also be useful in generating subtitles in a video, frame-by-frame.
* It would be of great help to the social-media platforms to infer the place, what one is wearing or interpret the human activity involved.
* It can also be used in editing application and image indexing.

</div>

<div align="justify">
  
## DATA ANALYSIS

* The image dataset used here is the Flickr_8K dataset which contains 8091 images.
* It also contains Flickr_8k_text folder which comprises of the text files and captions of images.
  - Flickr8k.token.txt :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contains the image id along with the 5 captions
  - Flickr8k.trainImages.txt :&nbsp;&nbsp;Contains the training image ids
  - Flickr8k.testImages.txt :&nbsp;&nbsp;&nbsp;Contains the test image ids
* Each image is associated with five different captions that describe the entities and events depicted in the image collected.
* Associating each image with multiple, independently produced sentences, the dataset captures some of the linguistic variety that can be used to describe the same image.
  
</div>

<div align="justify">

## MODEL USED

<!-- * Convolutional Neural Network [Refer: <a href="https://github.com/Akriti0100/Human-Action-Recognition/blob/main/ActionRec/actions/model.json">`model.json`</a> for implementation and <a href="https://drive.google.com/file/d/1-9qVHM-f3FWYir2KCwPUUE0Tar5Ll_mi/view?usp=sharing">`Model.weights.best.hdf5` </a> for weights of the model] -->
* Convolutional Neural Network [Image-Based Model]
  - CNNs are best suited for the task of `image classification` and `identification` purposes. It can process the input data in the shape of 2D matrix and images can be easily represented in the 2D shape.
  - It scans images from left to right and top to bottom to pull out important features from the image and combines the feature to classify images.
  - It can also handle the images that have been translated, rotated, scaled and changes in perspective.

* Long Short Term Memory Model (LSTM) [Language-Based Model]
  - It is a type of RNN (recurrent neural network) which is well suited for `sequence prediction problems`.
  - It has proven itself effective from the traditional RNN by overcoming the limitations of RNN which had short term memory.
  - It helps in the prediction of what next word will be, based on the previous text.
  - LSTM can carry out relevant information throughout the processing of inputs and with a forget gate, it discards non-relevant information.

```
  - The model used here is an encoder-decoder model. Here, the encoded form of the image and the text is fed to the decoder.
  - To encode the image features we make use of the Xception Model (a type of CNN model), pre-trained on ImageNet dataset
    (Transfer Learning Technique).
  - Further, the encoding of the text sequence is done in a separate layer after the input layer which is referred to as 
    the embedding layer.
  - This type of model is referred to as the merge architecture where vectors resulting from both the encodings are merged 
    and processed by a Dense layer to make a final prediction.
```
<!-- <img src="https://github.com/Akriti0100/Human-Action-Recognition/blob/main/images/cnn_model.png" alt="Model" width="500" height="600">
<br><br>
<p>The training and validation loss graph of the above sequential CNN model is as shown below:</p>
<img src="https://github.com/Akriti0100/Human-Action-Recognition/blob/main/images/modelLoss.png" alt="Loss" width="500"> -->
 
</div>

<!--<div align="justify">-->
 
<!-- # ?? Project overview -->
<!--## Project Scope

> Everything today is moving towards digitalization. This platform designed will increase the efficiency of the hospitals and bring the specialists from the nooks and corners of the country available at a single platform. 
>
> It will help overcome the challenge of increased drop rate in the regular patient visits and also help patients to consult the doctors in case of emergency situations by fixing an appointment without the need to visit the hospital. 
>
> This would also help to overcome the problem of deficiency of human resources in the health sector which is prevalent at several levels such as between regions, between rural and urban areas and between private and public sectors. It's a platform to consult the health care specialists in the respective fields thus, bridging the gap between different sections of the society. 
>
> Apart from these, it aims to reduce the challenges faced by people who are looking online for health information regarding diseases, diagnosis and different treatments.
 
</div>-->

<!-- <div align="justify">
 
## Input-Output Screenshots
 
![screenshot](https://github.com/Akriti0100/Human-Action-Recognition/blob/main/images/Input-Output%20Screenshots.gif)
  
For details, you may also refer the <a href="https://github.com/Akriti0100/Human-Action-Recognition/tree/main/Input-Output%20Screenshots">`Input - Output Screenshots`</a> folder.

</div>

<div align="justify">
 
## Methodology Flowchart
 
<img src="https://github.com/Akriti0100/Human-Action-Recognition/blob/main/images/WorkFlow.jpg" alt="Flowchart">

</div> -->

<div align="justify">
 
## How To Use

To clone and run this application, you’ll need `Git` and `Django` installed on your computer. <br>
From your command line:

```
# Clone this repository
$ git clone https://github.com/Akriti0100/Image-Caption-Generator.git

# Install dependencies
$ pip3 install tensorflow keras numpy pillow tqdm

# Go into the repository
$ cd captionGenerator

# Run the app
$ python manage.py runserver
```

</div>

<div align="justify">
 
## License
 
This project is free and open-source software licensed under the `GPL-3.0 License`.

</div>
