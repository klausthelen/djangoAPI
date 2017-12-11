from rest_framework import serializers
from post.models import Post

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ('id_blog', 'author', 'title')

	def create(self, validated_data):
		id_blog = validated_data.get('id_blog', None)
		user = self.context.get("user")
		title = validated_data.get('title', None)
		return Post.objects.create(id_blog=id_blog, author=user, title=title)

		