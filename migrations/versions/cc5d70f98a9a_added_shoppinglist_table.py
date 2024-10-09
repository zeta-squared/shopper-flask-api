"""added ShoppingList table

Revision ID: cc5d70f98a9a
Revises: 90f6906e123c
Create Date: 2024-10-09 12:08:00.058432

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc5d70f98a9a'
down_revision = '90f6906e123c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shopping_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('items', sa.PickleType(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_shopping_list_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_shopping_list'))
    )
    with op.batch_alter_table('shopping_list', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_shopping_list_user_id'), ['user_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('shopping_list', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_shopping_list_user_id'))

    op.drop_table('shopping_list')
    # ### end Alembic commands ###
