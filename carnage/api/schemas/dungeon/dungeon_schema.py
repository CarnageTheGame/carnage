# MIT License
#
# Copyright (c) 2022, Rodolfo Olivieri
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Module to represent an Dungeon Schema schema."""

from pydantic import Field
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.dungeon import DungeonSchemaModel


class ListDungeonSchemaSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        DungeonSchemaModel,
        exclude=("schema",),
    ),
):
    """Class that represents a listing of elements."""

    dungeon_schema: str = Field(alias="schema")


class UpdateDungeonSchemaSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        DungeonSchemaModel,
        config=None,
        exclude=("schema",),
    ),
):
    """Class that represents an update of elements."""

    dungeon_schema: str = Field(alias="schema")


class CreateDungeonSchemaSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        DungeonSchemaModel,
        config=None,
        exclude=("schema",),
    ),
):
    """Class that represents an creation of elements."""

    dungeon_schema: str = Field(alias="schema")
