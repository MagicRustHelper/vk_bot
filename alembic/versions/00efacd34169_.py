"""empty message

Revision ID: 00efacd34169
Revises: 
Create Date: 2022-12-09 12:04:25.154659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00efacd34169'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('checks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('steamid', sa.BigInteger(), nullable=False),
    sa.Column('moder_vk', sa.BigInteger(), nullable=False),
    sa.Column('start_time', sa.DateTime(timezone='Europe/Moscow'), nullable=False),
    sa.Column('end_time', sa.DateTime(timezone='Europe/Moscow'), nullable=True),
    sa.Column('server_number', sa.Integer(), nullable=True),
    sa.Column('is_ban', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_checks_id'), 'checks', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_checks_id'), table_name='checks')
    op.drop_table('checks')
    # ### end Alembic commands ###