"""Added comment

Revision ID: 249426fc8a24
Revises: 3ab03f7fb806
Create Date: 2017-02-23 10:37:19.949070

"""

# revision identifiers, used by Alembic.
revision = '249426fc8a24'
down_revision = '3ab03f7fb806'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('commnents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('body_html', sa.DateTime(), nullable=True),
    sa.Column('disabled', sa.Boolean(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_commnents_body_html'), 'commnents', ['body_html'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_commnents_body_html'), table_name='commnents')
    op.drop_table('commnents')
    # ### end Alembic commands ###
