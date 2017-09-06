# coding:utf-8
from rest_framework import serializers
from article.models import Article
from article.serializers import ArticleSerializer
class ComentRelatedField(serializers.RelatedField):
    """
    A custom field to use for the `tagged_object` generic relationship.
    """

    def to_representation(self, value):
        """
        Serialize bookmark instances using a bookmark serializer,
        and note instances using a note serializer.
        """
        if isinstance(value, Article):
            serializer = ArticleSerializer(value)
        else:
            raise Exception('Unexpected type of object')

        return serializer.data