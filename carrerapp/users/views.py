from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
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

            # Always local development (no ngrok)
            domain = request.get_host()   # should be 127.0.0.1:8000
            protocol = "http"             # local dev runs on http
            verification_link = f"{protocol}://{domain}/verify/{uid}/{token}/"

            # -----------------------------
            # Send email with HTML + text
            # -----------------------------
            subject = "Verify Your Carrier Portal Profile"
            from_email = settings.DEFAULT_FROM_EMAIL
            to = [profile.email]

            text_content = (
                f"Hi {profile.name},\n\n"
                f"Please verify your email by clicking the link below:\n"
                f"{verification_link}\n\nThank you!"
            )

            html_content = f"""
            <html>
              <body style="font-family: Arial, sans-serif; line-height: 1.6;">
                <h2 style="color:#2c3e50;">Hi {profile.name},</h2>
                <p>Please verify your email by clicking the button below:</p>
                <p style="text-align:center;">
                  <a href="{verification_link}" 
                     style="background-color:#3498db; color:#fff; padding:12px 20px; 
                            text-decoration:none; border-radius:5px; font-weight:bold;">
                    Verify My Email
                  </a>
                </p>
                <p>If the button doesn’t work, copy and paste this link into your browser:</p>
                <p><a href="{verification_link}">{verification_link}</a></p>
                <br>
                <p>Thank you,<br>The Carrier Portal Team</p>
              </body>
            </html>
            """

            msg = EmailMultiAlternatives(subject, text_content, from_email, to)
            msg.attach_alternative(html_content, "text/html")
            msg.send()

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
