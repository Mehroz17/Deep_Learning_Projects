# MNIST GEN AI Model

## Two Methods Used

* Tensorflow 🧠
* Using simple Numpy 🧮


### Tensorflow
##### Generator 🌀 
    o It will generate images using Conv2D, Dense, Up sampling layer using Random Noise
    o Its goal is to produce data that closely resembles real examples.
##### Discriminator 🔍
    o The discriminator acts as a judge or critic.
    o It evaluates the authenticity of generated data compared to real data.
    o Given an input (either real or generated), the discriminator predicts whether it is real or fake.
##### Training Loop 🔄
    o We have to make balance between discriminator and generator
    o The learning rate of generator will be higher then discriminator

![image](https://github.com/Mehroz17/Deep_Learning_Projects/assets/166553028/a62f0982-1fc9-4dac-9e78-59417d4b2b79)


### To Run the TensorFlow Model  🚀
#### Pre-req 📋

* Install the Following
  * Python  🐍
  * Numpy 🧮
  * Tensoflow
  * Gradio
  * Matplotlib
    
* Open GENAI_USING_TENSORFLOW.ipynb File  📂
* Run the first cell ▶️<br>
  ![image](https://github.com/Mehroz17/Deep_Learning_Projects/assets/166553028/b6dab129-a720-4b53-bb64-33562ce0f449)
* Initialize the Random Noise 🎲<br>
 ![image](https://github.com/Mehroz17/Deep_Learning_Projects/assets/166553028/4c63cf9a-de1c-49f4-aeae-e91c87c05852)
* Import the saved models using tensorflow LoadModel
* Function to generate the images
* Then Launch the Gradio UI
 ![image](https://github.com/Mehroz17/Deep_Learning_Projects/assets/166553028/59bcee99-e374-4e67-9ebb-79b923c9b8c9)
![image](https://github.com/Mehroz17/Deep_Learning_Projects/assets/166553028/641b93d2-91fb-4327-a1ac-f41a117d58bb)



  
