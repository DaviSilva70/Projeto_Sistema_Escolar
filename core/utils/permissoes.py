# utils/permissoes.py

from functools import wraps
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


def perfil_requerido(*perfis):
    """
    Decorator que verifica se o usuário tem o perfil adequado.
    Uso: @perfil_requerido('professor', 'admin')
    """
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def _wrapped(request, *args, **kwargs):
            if request.user.tipo in perfis:
                return view_func(request, *args, **kwargs)
            raise PermissionDenied
        return _wrapped
    return decorator


class PerfilMixin(LoginRequiredMixin):
    """Mixin para Class-Based Views que verifica perfil"""
    perfis_permitidos = []

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if request.user.tipo not in self.perfis_permitidos:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
