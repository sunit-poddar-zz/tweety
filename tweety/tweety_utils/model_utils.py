from django.db import models


class RowInformation(models.Model):
    """
    Abstract class which contains row information columns AUTOMATICALLY
    Most of the legacy models were attached to RowInformation as we needed to migrate the data
    """

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def get_created_at(self):
        return self.created_at.strftime("%I:%M %p")

    def get_modified_at(self):
        return self.modified_at.strftime("%I:%M %p")