from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'Accounts'

    # ISSUE: https://stackoverflow.com/questions/59435187/django-signals-not-working-when-placed-outside-models-py ( signals.py not working so i put below line insted of above line )
    def ready(self):
        import Accounts.signals
