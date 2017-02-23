"""added body_html

Revision ID: fe688b1caca2
Revises: f620460264b0
Create Date: 2017-02-22 15:47:10.633107

"""

# revision identifiers, used by Alembic.
revision = 'fe688b1caca2'
down_revision = 'f620460264b0'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    # ### end Alembic commands ###
