import face_recognition

def verify_face(reference_path, test_path):
    try:
        ref_image = face_recognition.load_image_file(reference_path)
        ref_encoding = face_recognition.face_encodings(ref_image)[0]

        test_image = face_recognition.load_image_file(test_path)
        test_encoding = face_recognition.face_encodings(test_image)[0]

        result = face_recognition.compare_faces([ref_encoding], test_encoding)[0]
        return result
    except Exception as e:
        return f"Error: {str(e)}"
