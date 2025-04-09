import magic

def validate_file_type(file_path, allowed_file_types =None):
    if allowed_file_types is None:
        allowed_file_types = [
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
        
        if detected_type in allowed_file_types:
            return True
        else:
            return False
    except Exception:
        return False

file_path = input("Enter your file")

#validate_file_type(file_path)

if validate_file_type(file_path):
    print("valid file")
else:
    print("invalid file")
  