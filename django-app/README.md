# Face Verification Project

This project implements a face verification system using Django and ONNX.

## Description

The project includes an API that accepts two images, computes their similarity using a pre-trained ONNX model, and returns a similarity score and a similarity status.

## Installation Instructions

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/kareem5aled/face_verification.git
   cd face_verification

1. **Build the Docker Image:**

   ```
   sh
   Copy code
   docker build -t face_verification .
   ```

2. **Run the Docker Container:**

   ```
   sh
   Copy code
   docker run -p 8000:8000 face_verification
   ```

## Usage

To test the API, you can use the following `curl` command:

```
sh
Copy code
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