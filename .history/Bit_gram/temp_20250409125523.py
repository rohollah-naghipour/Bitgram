import magic


def validate_file_type(file_path, allowed_types):
    try:
        mime = magic.Magic(mime=True)
        detected_type = mime.from_file(file_path)
        
        if detected_type in allowed_types:
            return True
        else:
            print(f"Invalid file type: {detected_type}")
            return False
    except Exception as e:
        print(f"Error checking file: {e}")
        return False


file  = input("Enter your file: ")
validate_file_type(file_path = file, allowed_types='.jpg')
