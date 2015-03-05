from django.db import models
from model_utils.models import StatusModel, TimeStampedModel
from model_utils import Choices
from taggit.managers import TaggableManager
from profiles.models import GigPoster
from tags.models import SkillTaggedItem


class Gig(StatusModel, TimeStampedModel):
    """Gig posting"""
    # status of post
    # TODO change behavior based on status
    STATUS = Choices('draft', 'published', 'expired', 'removed')

    # poster
    poster = models.ForeignKey(GigPoster)

    # job title of gig
    title = models.CharField(max_length=200)

    # description of gig
    description = models.TextField()

    # skills
    skills_desired = TaggableManager(through=SkillTaggedItem, verbose_name='desired skills')

    def __unicode__(self):
        return self.title
