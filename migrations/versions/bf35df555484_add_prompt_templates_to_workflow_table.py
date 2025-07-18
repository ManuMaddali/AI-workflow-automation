"""Add prompt_templates to Workflow table

Revision ID: bf35df555484
Revises: 69b3f9544a99
Create Date: 2025-01-27 23:07:23.554093

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf35df555484'
down_revision = '69b3f9544a99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('workflow', schema=None) as batch_op:
        batch_op.add_column(sa.Column('prompt_templates', sa.JSON(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('workflow', schema=None) as batch_op:
        batch_op.drop_column('prompt_templates')

    # ### end Alembic commands ###
