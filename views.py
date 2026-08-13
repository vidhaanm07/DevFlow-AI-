class PasswordResetView(View):
    def get(self, request, *args, **kwargs):
        form = PasswordResetForm()
        return render(request, "password_reset.html", {"form": form})