import magic

def validate_file_type(file_path, allowed_mime_types=None):
    if allowed_mime_types is None:
        allowed_mime_types = [
            'image/jpeg', 
            'image/png',  
            'image/gif',  
            'video/mp4',   
            'video/x-msvideo', 
            'video/x-matroska', 
            'video/quicktime'
        ]
    
    try:
        mime = magic.Magic(mime=True)
        detected_type = mime.from_file(file_path)
        
        if detected_type in allowed_mime_types:
            return True
        else:
            print(f"Invalid file type: {detected_type}")
            return False
    except Exception as e:
        print(f"Error checking file: {e}")
        return False

# تست تابع
file_path = input("Enter your file")
if validate_file_type(file_path):
    print("valid file")
else:
    print("invalid file")
  