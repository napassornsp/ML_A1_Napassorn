# ML_A1_Napassorn-  Car Price Prediction Web Application

This repository hosts a web-based system to predict car prices using machine learning. The system uses various car features to estimate prices. Below is a quick guide on how to set up and use the application.

## Table of Contents

- [Project Setup Instructions](#Project-Setup-Instructions)
- [Visual Guide to Using the Car Price Predictor](#Visual-Guide-to-Using-the-Car-Price-Predictor)


## Project Setup Instructions

To set up and deploy the project on your local machine, please follow these steps:

1. Install docker and Git
    - Docker: [Install Docker](https://docs.docker.com/get-docker/)
    - Git: [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)


2. Clone the repository:
    ```bash
    git clone https://github.com/napassornsp/ML_A1_Napassorn.git
    ```

3. Navigate to the project directory:

    ```bash
    cd ./ML_A1_Napassorn/
    ```

4.  Deploy the website:
Run docker-compose up to build and start the Docker containers as per the docker-compose.yml file.

    ```bash
    docker-compose up
    ```

5. Access the website:

    Open http://localhost:600 in your web browser to view the locally hosted website.



## Visual Guide to Using the Car Price Predictor

1. **Homepage :**
   Start by opening your web browser and navigating to http://127.0.0.1:600 to access our Car Price Predictor.
   
   You will then see a form that requires you to input details about your car:
   - Manufacturing Year
   - Kilometer Driven (km)
   - Mileage (kmpl)
   - Engine Capacity (cc)
   - Max power (bhp)
   
    Once you've filled in all the necessary information, click the "Predict Price" button.
   ![homepage](https://github.com/user-attachments/assets/12c0c2c9-043e-44e6-96c0-1ceaa740eb63)   

2. **View the reult:**
    The web app will process the information you've provided and display the predicted price of your car.
   ![result](https://github.com/user-attachments/assets/3cc9e562-61da-4282-8e8f-a566ec14a140)


   
   
