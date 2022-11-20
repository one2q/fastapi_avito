"""second migrat

Revision ID: 08aee1458f75
Revises: 5ce0fc9cf103
Create Date: 2022-11-20 17:21:29.341279

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08aee1458f75'
down_revision = '5ce0fc9cf103'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('advert',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('main_foto', sa.String(), nullable=False),
    sa.Column('describe', sa.String(length=1000), nullable=True),
    sa.Column('foto', sa.String(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('advert')
    # ### end Alembic commands ###