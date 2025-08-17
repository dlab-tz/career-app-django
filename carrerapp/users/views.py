from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .models import UserProfile
from .forms import UserProfileForm


# -------------------------------
# Custom token generator
# -------------------------------
class EmailVerificationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return str(user.pk) + str(timestamp) + str(user.is_verified)

email_verification_token = EmailVerificationTokenGenerator()


# -------------------------------
# Save profile and send verification email
# -------------------------------
def save_profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.is_verified = False
            profile.save()

            # Generate verification token and link
            uid = urlsafe_base64_encode(force_bytes(profile.pk))
            token = email_verification_token.make_token(profile)
            domain = request.get_host()
            verification_link = f"https://9abd65b02ac1.ngrok-free.app/verify/{uid}/{token}/"



            # Send email
            subject = "Verify Your Carrier Portal Profile"
            message = f"Hi {profile.name},\n\nPlease verify your email by clicking the link below:\n{verification_link}\n\nThank you!"
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [profile.email], fail_silently=False)

            return render(request, "users/success.html", {"email": profile.email})
    else:
        form = UserProfileForm()

    return render(request, "users/form.html", {"form": form})


# -------------------------------
# Verify email
# -------------------------------
def verify_email(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        profile = UserProfile.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserProfile.DoesNotExist):
        profile = None

    if profile and email_verification_token.check_token(profile, token):
        profile.is_verified = True
        profile.save()
        return render(request, "users/verification_success.html", {"name": profile.name})
    else:
        return render(request, "users/verification_failed.html")
