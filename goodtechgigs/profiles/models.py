from django.db import models
from taggit.managers import TaggableManager
from users.models import User
from tags.models import SkillTaggedItem, CauseTaggedItem


class BaseProfile(models.Model):
    """Base user profile"""
    # TODO created and updated

    # user
    user = models.ForeignKey(User)

    # location
    location = models.CharField(max_length=200)

    # causes
    causes = TaggableManager(through=CauseTaggedItem)

    # about, aka description/bio
    about = models.TextField()

    class Meta:
        abstract = True


class GigSeeker(BaseProfile):
    """Profile for a user seeking gigs"""
    # skills
    skills = TaggableManager(through=SkillTaggedItem)


class GigPoster(BaseProfile):
    """Profile for an org posting gigs"""
    pass
