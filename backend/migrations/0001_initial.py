# Generated by Django 4.2.5 on 2023-11-25 20:13

import django.contrib.auth.validators
import django.utils.timezone
import shortuuid.django_fields
from django.conf import settings
from django.db import migrations, models

import backend.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(blank=True, null=True, verbose_name="last login"),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={"unique": "A user with that username already exists."},
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(blank=True, max_length=150, verbose_name="first name"),
                ),
                (
                    "last_name",
                    models.CharField(blank=True, max_length=150, verbose_name="last name"),
                ),
                (
                    "email",
                    models.EmailField(blank=True, max_length=254, verbose_name="email address"),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(default=django.utils.timezone.now, verbose_name="date joined"),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", backend.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("active", models.BooleanField(default=True)),
                ("name", models.CharField(max_length=64)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("address", models.CharField(blank=True, max_length=100, null=True)),
                ("city", models.CharField(blank=True, max_length=100, null=True)),
                ("country", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Invoice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("invoice_id", models.IntegerField(blank=True, null=True, unique=True)),
                (
                    "client_name",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "client_company",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "client_address",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "client_city",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "client_county",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "client_country",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("self_name", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "self_company",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "self_address",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("self_city", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "self_county",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "self_country",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("sort_code", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "account_holder_name",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "account_number",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("reference", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "invoice_number",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("vat_number", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "logo",
                    models.ImageField(blank=True, null=True, upload_to="invoice_logos"),
                ),
                ("notes", models.TextField(blank=True, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_due", models.DateField()),
                ("date_issued", models.DateField(blank=True, null=True)),
                (
                    "payment_status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("paid", "Paid"),
                            ("overdue", "Overdue"),
                        ],
                        default="pending",
                        max_length=10,
                    ),
                ),
                (
                    "client_to",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="backend.client",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="InvoiceItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=100)),
                ("is_service", models.BooleanField(default=True)),
                (
                    "hours",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
                ),
                (
                    "price_per_hour",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
                ),
                (
                    "price",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "leader",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "members",
                    models.ManyToManyField(related_name="teams_joined", to=settings.AUTH_USER_MODEL),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserSettings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dark_mode", models.BooleanField(default=True)),
                (
                    "currency",
                    models.CharField(
                        choices=[
                            ("GBP", "British Pound Sterling"),
                            ("EUR", "Euro"),
                            ("USD", "United States Dollar"),
                            ("JPY", "Japanese Yen"),
                            ("INR", "Indian Rupee"),
                            ("AUD", "Australian Dollar"),
                            ("CAD", "Canadian Dollar"),
                        ],
                        default="GBP",
                        max_length=3,
                    ),
                ),
                (
                    "profile_picture",
                    models.ImageField(blank=True, null=True, upload_to="profile_pictures/"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "User Settings",
                "verbose_name_plural": "User Settings",
            },
        ),
        migrations.CreateModel(
            name="TracebackError",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("error", models.CharField(max_length=5000, null=True)),
                ("date", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TeamInvitation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=10)),
                ("expires", models.DateTimeField(blank=True, null=True)),
                ("active", models.BooleanField(default=True)),
                (
                    "invited_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="team_invitations",
                        to="backend.team",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="team_invitations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Team Invitation",
                "verbose_name_plural": "Team Invitations",
            },
        ),
        migrations.CreateModel(
            name="Receipt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="receipts")),
                ("total_price", models.FloatField(blank=True, null=True)),
                ("date", models.DateField(blank=True, null=True)),
                ("date_uploaded", models.DateTimeField(auto_now=True)),
                ("receipt_parsed", models.JSONField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PasswordSecret",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("secret", models.TextField(max_length=300)),
                ("expires", models.DateTimeField(blank=True, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="password_secrets",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", models.CharField(max_length=100)),
                (
                    "action",
                    models.CharField(
                        choices=[
                            ("normal", "Normal"),
                            ("modal", "Modal"),
                            ("redirect", "Redirect"),
                        ],
                        default="normal",
                        max_length=10,
                    ),
                ),
                (
                    "action_value",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LoginLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="InvoiceURL",
            fields=[
                (
                    "uuid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet=None,
                        length=8,
                        max_length=8,
                        prefix="",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("expires", models.DateTimeField(blank=True, null=True)),
                ("active", models.BooleanField(default=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "invoice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="invoice_urls",
                        to="backend.invoice",
                    ),
                ),
            ],
            options={
                "verbose_name": "Invoice URL",
                "verbose_name_plural": "Invoice URLs",
            },
        ),
        migrations.AddField(
            model_name="invoice",
            name="items",
            field=models.ManyToManyField(to="backend.invoiceitem"),
        ),
        migrations.AddField(
            model_name="invoice",
            name="user",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name="Error",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("error", models.CharField(max_length=250, null=True)),
                ("error_code", models.CharField(max_length=100, null=True)),
                ("error_colour", models.CharField(default="danger", max_length=25)),
                ("date", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AuditLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("action", models.CharField(max_length=100)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]