from typing import Type

from carnage.database.models.spell_duration_type import SpellDurationTypeModel
from carnage.database.repository.base import BaseRepository


class SpellDurationTypeRepository(BaseRepository):
    def __init__(
        self,
        model: Type[SpellDurationTypeModel] = SpellDurationTypeModel,
    ) -> None:
        super().__init__(model)
