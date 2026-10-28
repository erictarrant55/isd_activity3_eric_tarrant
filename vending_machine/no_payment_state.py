"""Defines the NoPaymentState class."""
__author__ = "Eric Tarrant"
__version__ = "1.0.0"

from vending_machine.state import State
from vending_machine.vending_machine import VendingMachine


class NoPaymentState(State):
    """
    Represents when the vending machine does not receive sufficient funds.
    """
    def receive_payment(self, machine) -> None:
        """
        Displays that payment has been added.
        """
        machine.output_to_display("PAYMENT ADDED")
        machine.state = NoPaymentState()
        pass

    def select_item(self, machine) -> None:
        """
        Displays that there insufficient funds does not dispense any items.
        """
        machine.output_to_display(
            "INSUFFICIENT FUNDS - ADD PAYMENT"
        )
        pass
