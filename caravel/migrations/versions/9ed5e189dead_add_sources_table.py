"""Add sources table

Revision ID: 9ed5e189dead
Revises: 41f6a59a61f2
Create Date: 2016-09-07 14:30:32.175919

"""

# revision identifiers, used by Alembic.
revision = '9ed5e189dead'
down_revision = '41f6a59a61f2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('sources',
    	sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('datasource_id',  sa.Integer(), nullable=False),
        sa.Column('datasource_type', sa.String(length=200), nullable=False),
    )


def downgrade():
    op.drop_table('sources')
