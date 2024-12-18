"""Add sources table

Revision ID: 25ef04fa2b8e
Revises: 
Create Date: 2024-12-18 19:21:27.609135

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '25ef04fa2b8e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_metadata_key', table_name='log_metadata')
    op.drop_table('log_metadata')
    op.alter_column('logs', 'id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
    op.alter_column('logs', 'source_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('logs', 'timestamp',
               existing_type=sa.TIMESTAMP(),
               type_=sa.DateTime(),
               existing_nullable=False)
    op.alter_column('logs', 'level',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               existing_nullable=True)
    op.alter_column('logs', 'message',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               existing_nullable=False)
    op.drop_index('idx_logs_level', table_name='logs')
    op.drop_index('idx_logs_timestamp', table_name='logs')
    op.add_column('sources', sa.Column('configuration', sa.String(), nullable=True))
    op.alter_column('sources', 'id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
    op.alter_column('sources', 'name',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               existing_nullable=False)
    op.alter_column('sources', 'type',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               existing_nullable=False)
    op.drop_column('sources', 'created_at')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sources', sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
    op.alter_column('sources', 'type',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=False)
    op.alter_column('sources', 'name',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=False)
    op.alter_column('sources', 'id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)
    op.drop_column('sources', 'configuration')
    op.create_index('idx_logs_timestamp', 'logs', ['timestamp'], unique=False)
    op.create_index('idx_logs_level', 'logs', ['level'], unique=False)
    op.alter_column('logs', 'message',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=False)
    op.alter_column('logs', 'level',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=True)
    op.alter_column('logs', 'timestamp',
               existing_type=sa.DateTime(),
               type_=sa.TIMESTAMP(),
               existing_nullable=False)
    op.alter_column('logs', 'source_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('logs', 'id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)
    op.create_table('log_metadata',
    sa.Column('log_id', sa.INTEGER(), nullable=False),
    sa.Column('key', sa.TEXT(), nullable=False),
    sa.Column('value', sa.TEXT(), nullable=False),
    sa.ForeignKeyConstraint(['log_id'], ['logs.id'], ),
    sa.PrimaryKeyConstraint('log_id', 'key')
    )
    op.create_index('idx_metadata_key', 'log_metadata', ['key'], unique=False)
    # ### end Alembic commands ###
