from django.db import models
from model_utils.models import TimeStampedModel
from taggit.managers import TaggableManager
from users.models import User
from tags.models import SkillTaggedItem, CauseTaggedItem


class BaseProfile(TimeStampedModel):
    """Base user profile"""
    # user
    user = models.ForeignKey(User)

    # location
    location = models.CharField(max_length=200)

    # causes
    causes = TaggableManager(through=CauseTaggedItem, verbose_name='causes')

    # about, aka description/bio
    about = models.TextField()

    class Meta:
        abstract = True


class GigSeeker(BaseProfile):
    """Profile for a user seeking gigs"""
    # skills
    skills = TaggableManager(through=SkillTaggedItem, verbose_name='skills')


class GigPoster(BaseProfile):
    """Profile for an org posting gigs"""
    # org name
    org_name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.org_name
