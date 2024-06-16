# Face Verification Project

This project implements a face verification system using Django and ONNX.

## Description

The project includes an API that accepts two images, computes their similarity using a pre-trained ONNX model, and returns a similarity score and a similarity status.

## Installation Instructions

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/kareem5aled/face_verification.git
   cd face_verification
   ```

2. **Build the Docker Image:**

   ```
   docker build -t face_verification .
   ```

3. **Run the Docker Container:**

   ```
   docker run -p 8000:8000 face_verification
   ```

## Usage

First, make sure to download the ONNX model from [google drive](https://drive.google.com/file/d/1v1zunrvi-dIuP87HCUwEqkWInxkfNr8A/view?usp=sharing) and add it to the following path `django-app/onnxmodel`

To test the API, start the django server:
```
python manage.py runserver
```

You can use tools like `curl`, Postman, or write a simple script to test the endpoint. Here's an example using `curl`:
```
curl -X POST http://127.0.0.1:8000/api/verify/ -F "image1=@path/to/image1.jpg" -F "image2=@path/to/image2.jpg"
```

## Endpoints

- **POST /api/verify/**: Accepts two images and returns their similarity score and similarity status.

## Docker Usage

To containerize the Django project and ensure a consistent runtime environment, Docker was used to create an image of the project. Here are the steps that were followed:

1. **Dockerfile Creation**: A `Dockerfile` was created in the root directory of the project. This file contains instructions on how to build the Docker image.
2. **Building the Docker Image**: The Docker image was built using the `docker build` command.
3. **Running the Docker Container**: Once the image was built, a container was started using the `docker run` command.

## Author

Karim Elezabawy  karim.elezabawy@gmail.com
