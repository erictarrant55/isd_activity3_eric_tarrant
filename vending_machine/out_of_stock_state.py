"""Defines the OutOfStockState class."""
__author__ = "Eric Tarrant"
__version__ = "1.0.0"

from .state import State

class OutOfStockState(State):
    """Represents when the vending machine is out of stock."""
    def receive_payment(self, machine) -> None:
        """
        Displays that the item is OUT OF STOCK when the vending machine
        receives payment.
        """
        machine.output_to_display("OUT OF STOCK")
        machine.state = OutOfStockState
        pass

    def select_item(self, machine) -> None: 
        """
        No item gets selected or dispensed.
        """
        pass