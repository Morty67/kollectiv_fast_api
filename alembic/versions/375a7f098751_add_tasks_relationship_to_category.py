"""Add tasks relationship to Category

Revision ID: 375a7f098751
Revises: f060819b3a00
Create Date: 2024-01-20 14:19:15.166353

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '375a7f098751'
down_revision: Union[str, None] = 'f060819b3a00'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###