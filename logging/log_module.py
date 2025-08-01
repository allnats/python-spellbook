"""Demo of a class using the `logging` module."""

import logging

class InventoryTracker:
    """A simple Inventory tracker application."""

    def __init__(self, log_filename: str = "app.log",
                 log_filemode: str = "w",
                 log_format: str = "%(asctime)s - %(levelname)s - %(message)s"
                 ) -> None:
      """Initialize the logging module of the class."""
      logging.basicConfig(
         level=logging.INFO,
         filename=log_filename,
         filemode=log_filemode,
         format=log_format,
      )

      self.logger = logging.getLogger(__name__)


    def track_item(self, item_name: str, item_quantity: int) -> None:
      try:
         item_quantity = int(item_quantity)

         self.logger.info(
            f"Quantity for item '{item_name}' is {item_quantity}"
          )

      except ValueError:
         self.logger.exception(
            f"Quantity for item '{item_name}' " +
            f"is not numeric: '{item_quantity}'"
          )

inventory: InventoryTracker = InventoryTracker()
user_input_item: str = ""
user_input_quantity: str = ""

while True:
   user_input_item = input("Enter the item name: ")
   if user_input_item.strip().upper() == "Q":
      break
   user_input_quantity = input(f"Enter the quantity for {user_input_item}: ")
   inventory.track_item(user_input_item, user_input_quantity)
