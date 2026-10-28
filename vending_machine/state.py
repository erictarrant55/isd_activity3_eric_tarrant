"""Defines the State interface.

A common interface for all vending machine states.
"""
from vending_machine.vending_machine import VendingMachine
from abc import ABC, abstractmethod

__author__ = "Eric Tarrant"
__version__ = "1.0.0"

class State(ABC):
    """Represents the state of the vending machine."""

    @abstractmethod
    def receive_payment(self, machine: VendingMachine) -> None:
        """
        Receives the payment of the vending machine
        """
        pass

    @abstractmethod
    def select_item(self, machine: VendingMachine) -> None:
        """
        Selects the item from the vending machine

        """
        pass