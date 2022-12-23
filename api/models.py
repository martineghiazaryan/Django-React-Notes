from django.db import models

class Note(models.Model):
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    

    # class Meta:
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    def __str__(self):
        return self.body[0:50]

#     def get_absolute_url(self):
#         return reverse("_detail", kwargs={"pk": self.pk})
