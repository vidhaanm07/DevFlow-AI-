class PasswordResetToken(models.Model):
    token = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)