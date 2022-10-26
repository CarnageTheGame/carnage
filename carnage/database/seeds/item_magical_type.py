from typing import Type

from carnage.database.repository.item_magical_type import (
    ItemMagicalTypeRepository,
)
from carnage.database.seeds.base import BaseSeed


class ItemMagicalTypeSeed(BaseSeed):
    name: str = "item-magical-type"
    data: list[dict[str, str]] = [
        {
            "name": "Wondrous Item",
            "description": "",
        },
        {
            "name": "Rod",
            "description": "",
        },
        {"name": "Scroll", "description": ""},
        {"name": "Staff", "description": ""},
        {"name": "Wand", "description": ""},
        {"name": "Ring", "description": ""},
        {"name": "Potion", "description": ""},
        {"name": "Amulet", "description": ""},
    ]

    def __init__(
        self,
        repository: Type[
            ItemMagicalTypeRepository
        ] = ItemMagicalTypeRepository,
    ) -> None:
        super().__init__(repository=repository)
