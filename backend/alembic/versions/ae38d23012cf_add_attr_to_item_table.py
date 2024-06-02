"""add attr to Item table

Revision ID: ae38d23012cf
Revises: 3939e4f35238
Create Date: 2024-04-13 01:59:56.945796

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ae38d23012cf'
down_revision: Union[str, None] = '3939e4f35238'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('contact_phone_number', sa.String(length=20), nullable=True))
    op.add_column('items', sa.Column('contact_address', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('items', 'contact_address')
    op.drop_column('items', 'contact_phone_number')
    # ### end Alembic commands ###