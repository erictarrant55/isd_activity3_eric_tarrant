"""Defines the NoPaymentState class."""
__author__ = "Eric Tarrant"
__version__ = "1.0.0"

from state import State
from vending_machine import VendingMachine


class NoPaymentState(State):

    def receive_payment(self, machine) -> None:
        machine.output_to_display("PAYMENT ADDED")
        machine.state = NoPaymentState()
        pass

    def select_item(self, machine) -> None:
        machine.output_to_display(
            "INSUFFICIENT FUNDS - ADD PAYMENT"
        )
        pass
