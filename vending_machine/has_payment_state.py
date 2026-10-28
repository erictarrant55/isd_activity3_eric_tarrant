"""Defines the HasPaymentState class."""
__author__ = "Eric Tarrant"
__version__ = "1.0.0"

from state import State

class HasPaymentState(State):
    """
    Represents when the vending machine has receive a successful payment.
    """
    def receive_payment(self, machine) -> None:
        """
        Displays that the vending machine has received money.
        """
        machine.output_to_display("ALREADY PAYMENT ADDED")
        machine.state = HasPaymentState()    
        pass

    def select_item(self, machine) -> None:
        """
        Dispenses the item that was selected.
        """
        machine.output_to_display("DISPENSING...", False)
        machine.dispense_product()
        pass