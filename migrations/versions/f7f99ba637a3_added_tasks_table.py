"""added tasks table

Revision ID: f7f99ba637a3
Revises: effefe4dac03
Create Date: 2021-10-16 19:56:42.660402

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7f99ba637a3'
down_revision = 'effefe4dac03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task_name', sa.String(length=64), nullable=True),
    sa.Column('task_details', sa.String(length=120), nullable=True),
    sa.Column('created_by', sa.String(length=64), nullable=True),
    sa.Column('subteam', sa.String(length=64), nullable=True),
    sa.Column('owner', sa.String(length=64), nullable=True),
    sa.Column('request', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['request'], ['request.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_task_task_details'), 'task', ['task_details'], unique=False)
    op.create_index(op.f('ix_task_task_name'), 'task', ['task_name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_task_task_name'), table_name='task')
    op.drop_index(op.f('ix_task_task_details'), table_name='task')
    op.drop_table('task')
    # ### end Alembic commands ###