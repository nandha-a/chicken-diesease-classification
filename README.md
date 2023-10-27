## Chicken Disease Classification

### Overview
The annotated dataset of poultry disease diagnostics for small to medium-scale poultry farmers consists of poultry fecal images. The poultry fecal images were taken in Arusha and Kilimanjaro regions in Tanzania between September 2020 and February 2021 using Open Data Kit (ODK) app on mobile phones. The classes are "Coccidiosis" ,"Healthy", "New Castle Disease" ,"Salmonella". The images are resized to 224px by 224px.

### Dataset
Contains 8067 unique fecal images of chickens under 4 categories as follows:
- Salmonella (2625 Images)
- Coccidiosis (2476 Images)
- Healthy (2404 Images)
- New Castle Disease (562 Images)

### Tools Required
- GitHub Account
- Visual Studio Code IDE
- GitCli
- Jupyter Notebook or Google Colab

### Packages Required
- Python 3.10.11
- Tensorflow
- Flask
- Numpy
- Pandas
- dvc
- matplotlib
- seaborn
- python-box 6.0.2
- pyYAML
- tqdm
- ensure 1.0.2
- joblib
- types-pyYAML
- scipy
- Flask
- Flask-Cors

### Model Selection
Xception pre-trained model is used in this project, it gives better accuracy and smaller loss compared to other pre-trained model. Xception is a deep convolutional neural network architecture that involves Depthwise Separable Convolutions. This network was introduced Francois Chollet who works at Google, Inc. Xception is also known as “extreme” version of an Inception module.

### Params used 
- Batch size = 32
- Image size = (224,224,3)
- xception.preprocess_input as preprocessor. Dumped it using pickle then reused it.
- Adam is the optimizer with the learning rate of 0.0001
- Relu is the activation function for dense layers
- Softmax is the activation function for output layer
- Categorical Cross Entropy used to calculate the loss of each epoch.

### Best Metrics
- Loss: 0.0244 
- Accuracy: 0.9971 
- Validation loss: 0.2569 
- Validation accuracy: 0.9231

### How to run?
### STEPS:

Clone the repository

```bash
https://github.com/nandha-a/Chicken-Disease-Classification--Project
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n cnncls python=3.8 -y
```

```bash
conda activate cnncls
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```


### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app




# AZURE-CICD-Deployment-with-Github-Actions

## Save pass:

s3cEZKH5yytiVnJ3h+eI3qhhzf9q1vNwEi6+q+WGdd+ACRCZ7JD6


## Run from terminal:

docker build -t chickenapp.azurecr.io/chicken:latest .

docker login chickenapp.azurecr.io

docker push chickenapp.azurecr.io/chicken:latest


## Deployment Steps:

1. Build the Docker image of the Source Code
2. Push the Docker image to Container Registry
3. Launch the Web App Server in Azure 
4. Pull the Docker image from the container registry to Web App server and run 