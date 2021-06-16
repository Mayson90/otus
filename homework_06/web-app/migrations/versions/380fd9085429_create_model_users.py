"""Create model Users

Revision ID: 380fd9085429
Revises: 
Create Date: 2021-06-16 12:51:02.677337

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '380fd9085429'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
