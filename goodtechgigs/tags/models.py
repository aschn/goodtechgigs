from django.db import models
from taggit.models import GenericTaggedItemBase, TagBase


class SkillTag(TagBase):
    pass

class SkillTaggedItem(GenericTaggedItemBase):
    tag = models.ForeignKey(SkillTag, related_name="%(app_label)s_%(class)s_skills")

class CauseTag(TagBase):
    pass

class CauseTaggedItem(GenericTaggedItemBase):
    tag = models.ForeignKey(CauseTag, related_name="%(app_label)s_%(class)s_causes")
