"""empty message

Revision ID: 39d73b791c9a
Revises: fd950e79635
Create Date: 2014-06-25 18:16:11.922339

"""

# revision identifiers, used by Alembic.
revision = '39d73b791c9a'
down_revision = 'fd950e79635'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    #op.drop_column('Street', 'street_id')
    pass
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Street', sa.Column('street_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    ### end Alembic commands ###
