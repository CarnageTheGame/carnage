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
"""Module to represent an Aligment schema."""

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.aligment import AligmentModel


class ListAligmentSchema(
    sqlalchemy_to_pydantic(AligmentModel),  # type: ignore
):
    """Class that represents a listing of elements."""


class UpdateAligmentSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        AligmentModel,
        config=None,
    ),
):
    """Class that represents an update of elements."""


class CreateAligmentSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        AligmentModel,
        config=None,
    ),
):
    """Class that represents an creation of elements."""
