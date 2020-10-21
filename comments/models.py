from django.db import models
class Comment(models.Model):
    text = models.TextField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    route = models.ForeignKey(
        'routes.Route',
        related_name="comments",
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f'Comment - {self.id} on Route - {self.route}'