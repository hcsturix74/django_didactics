from django.db import models



class PublicManager(models.Manager):
    """
    This manager implements the get_query_set() method
    and  filters only the public 'contents'
    """

    def get_queryset(self):
        """
        This is the get_query_set method override.
        Here only public stuff is retrieved; this filter is on
        is_public field.
        """
        return super(PublicManager, self).get_query_set().filter(is_public=True)
