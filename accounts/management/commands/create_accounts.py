from typing import Any
from uuid import uuid4
from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from accounts.models import Account


class Command(BaseCommand):
    help = "Esse comando cria Contas aleatórios"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "-a",
            "--amount",
            help="Especifica o número de contas a serem criadas",
            type=int,
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        # Definimos o que queremos fazer:
        # Criação de um só produto
        # PEGAremos o valor dos argumentos através do option
        amount = options["amount"]
        if amount is None:
            return self.stdout.write("O argumento amount precisa ser obrigatório")
        for _ in range(amount):
            Account.objects.create(username=str(uuid4()), email=str(uuid4()))
        self.stdout.write("Contas adiconadas")
