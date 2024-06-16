from django.shortcuts import render
from django.http import JsonResponse
from .onnx_model import get_similarity_score
from PIL import Image
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def verify_faces(request):
    if request.method == 'POST':
        if 'image1' not in request.FILES or 'image2' not in request.FILES:
            return JsonResponse({'error': 'Please provide both images.'}, status=400)

        try:
            image1 = request.FILES['image1']
            image2 = request.FILES['image2']

            img1 = Image.open(image1)
            img2 = Image.open(image2)

            similarity, is_similar = get_similarity_score(img1, img2)

            return JsonResponse({
                'similarity_score': similarity,
                'is_similar': is_similar
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)
