from django.db import models

# Create your models here.

class Puns(models.Model):
    """
    Model representing a pun entry.

    Attributes:
        puns_text (CharField): The text of the pun (max 250 characters).
        pub_date (DateField): The date the pun was published.
    """

    puns_text = models.CharField(max_length=250)
    pub_date = models.DateField('date published')

    def __str__(self):
        """
        Returns a string representation of the pun text.

        Returns:
            str: The text of the pun.
        """
        return str(self.puns_text)


class Thoughts(models.Model):
    """
    Model representing a thought entry.

    Attributes:
        thoughts_text (CharField): The content of the thought (max 250 characters).
        pub_date (DateField): The date the thought was published.
    """

    thoughts_text = models.CharField(max_length=250)
    pub_date = models.DateField('date published')

    def __str__(self):
        """
        Returns a string representation of the thought text.

        Returns:
            str: The text of the thought.
        """
        return str(self.thoughts_text)


class DiaryEntry(models.Model):
    """
    Model representing a diary entry.

    Attributes:
        diary_entry (CharField): The content of the diary entry (max 500 characters).
        pub_date (DateField): The date the diary entry was published.
    """

    diary_entry = models.CharField(max_length=500)
    pub_date = models.DateField('date published')

    def __str__(self):
        """
        Returns a string representation of the diary entry.

        Returns:
            str: The content of the diary entry.
        """
        return str(self.diary_entry)

