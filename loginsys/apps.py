from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class LoginsysConfig(AppConfig):
    name = 'loginsys'
    verbose_name = _('profiles')

    def ready(self):
        import loginsys.signals  # noqa
