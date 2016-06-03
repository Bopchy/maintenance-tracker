"""empty message

Revision ID: 4f46cb846237
Revises: None
Create Date: 2016-06-03 12:11:38.502000

"""

# revision identifiers, used by Alembic.
revision = '4f46cb846237'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('Password_hash', sa.String(length=128), nullable=True))
    op.drop_column('user', 'Password')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('Password', sa.VARCHAR(length=15), nullable=False))
    op.drop_column('user', 'Password_hash')
    ### end Alembic commands ###
