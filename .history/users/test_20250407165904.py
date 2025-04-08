from datetime import datetime
from rest_framework import serializers

class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

comment = Comment(email='leila@example.com', content='foo bar')
class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

#print(comment)
#print(comment.email)
#print(comment.created)
#print(comment.content)

serializer = CommentSerializer(comment)


print(serializer.data)