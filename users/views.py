import random
from typing import Any

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from users.forms import UserRegisterForm
from users.models import User
from django.conf import settings
from django.core.mail import send_mail


class RegisterUserView(CreateView):
    model = User
    form_class = UserRegisterForm

    def get_success_url(self):
        return reverse_lazy("catalog:product_list")

    def get_context_data(self, *args, **kwargs: Any) -> dict[str, Any]:
        context_data = super().get_context_data(*args, **kwargs)
        context_data["title"] = "Создать пользователя"

        return context_data

    def form_valid(self, form):
        user = form.save()
        user.is_active = False

        current_site = self.request.get_host()
        subjet = 'Подтверждение регистрации'

        verification_code = ''.join(str(random.randint(0, 9)) for _ in range(8))
        user.verification_code = verification_code

        message = (f'Вы успешно зарегистрировались. '
                   f'Для завершения процесса перейдите по ссылке http://{current_site}/users/confirm/'
                   f'и введите код верификации {verification_code}')
        user.save()

        send_mail(
            subject=subjet,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email,]
        )
        user.save()
        
        return super().form_valid(form)


class ConfirmRegisterView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'users/confirm_registration.html')

    def get_context_data(self, *args, **kwargs: Any) -> dict[str, Any]:
        context_data = super().get_context_data(*args, **kwargs)
        context_data["title"] = "Подтверждение регистрации"

        return context_data

    def post(self, request, *args, **kwargs):
        verification_code = request.POST.get('verification_code')
        user = get_object_or_404(User, verification_code=verification_code)

        if user:
            user.is_activ = True
            user.save()
            return redirect('users:login')
        return redirect('catalog:product_list')
