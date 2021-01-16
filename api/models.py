from django.db import models


class TimestampedModel(models.Model):
    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(auto_now_add=True)

    # A timestamp reprensenting when this object was last updated.
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

        # By default, any model that inherits from `TimestampedModel` should
        # be ordered in reverse-chronological order. We can override this on a
        # per-model basis as needed, but reverse-chronological is a good
        # default ordering for most models.
        ordering = ['-created_at', '-updated_at']


# Create your models here.
class Github(TimestampedModel):
    repository = models.CharField(max_length=99)


class Language(TimestampedModel):
    github = models.ForeignKey(
        'api.Github', related_name='languages', on_delete=models.CASCADE
    )
    javascript = models.IntegerField()
    java = models.IntegerField()
    python = models.IntegerField()
    php = models.IntegerField()
    type = models.CharField(max_length=20)
    date = models.DateField()


class Media(TimestampedModel):
    github = models.ForeignKey(
        'api.Github', related_name='medias', on_delete=models.CASCADE
    )
    file = models.IntegerField()
    folder = models.IntegerField()
    date = models.DateField()
