"""fix status col to UserDocs

Revision ID: 1a3ab2eccd16
Revises: 52ff64425730
Create Date: 2024-04-16 21:04:03.962179

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a3ab2eccd16'
down_revision: Union[str, None] = '52ff64425730'
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