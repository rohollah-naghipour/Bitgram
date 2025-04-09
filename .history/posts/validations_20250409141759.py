  
from django.core.exceptions import ValidationError
import magic

def validate_file_type(file):
    allowed_mime_types = ['image/jpeg', 'video/mp4']  
  
    mime = magic.Magic(mime=True)
    detected_type = mime.from_buffer(file.read(1024))
    file.seek(0)
    
    if detected_type not in allowed_mime_types:
        raise ValidationError("The file must be an image or video.")


