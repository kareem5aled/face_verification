import onnxruntime as ort
import numpy as np
from PIL import Image
import torchvision.transforms as transforms
import torch

# Load ONNX model
onnx_model_path = "onnxmodel/siamese_network.onnx"
ort_session = ort.InferenceSession(onnx_model_path)

# Define transformation
transform = transforms.Compose([
    transforms.Resize((160, 160)),
    transforms.ToTensor(),
])

def preprocess_image(image):
    image = transform(image)
    image = image.unsqueeze(0)  # Add batch dimension
    return image.numpy()

def get_similarity_score(img1, img2):
    img1 = preprocess_image(img1)
    img2 = preprocess_image(img2)
    
    inputs = {ort_session.get_inputs()[0].name: img1, ort_session.get_inputs()[1].name: img2}
    outputs = ort_session.run(None, inputs)
    
    embedding1, embedding2 = outputs
    cos = torch.nn.CosineSimilarity(dim=1, eps=1e-6)
    similarity = cos(torch.tensor(embedding1), torch.tensor(embedding2)).item()
    return similarity, similarity > 0.64
