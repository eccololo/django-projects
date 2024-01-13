from django.db import models


class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.__get_item_title()

    def __get_item_title(self):
        completed = "[Unknown]"
        if self.completed:
            completed = "[Done]"
        else:
            completed = "[Undone]"

        return f"{self.item} {completed}"
