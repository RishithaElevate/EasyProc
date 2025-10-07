from deepface import DeepFace

def verify_face(img1_path, img2_path):
    try:
        result = DeepFace.verify(img1_path, img2_path)
        return result["verified"]
    except Exception as e:
        return str(e)
