"""add check-in fields to order_items

Revision ID: 387cc944c2dd
Revises: 8940252818ac
Create Date: 2025-10-16 11:07:26.614541

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '387cc944c2dd'
down_revision = '8940252818ac'
branch_labels = None
depends_on = None


def upgrade():
    # SQLite does not support many ALTER operations; only add the new columns.
    op.add_column('order_items', sa.Column('checked_in', sa.Boolean(), nullable=False, server_default=sa.text('false')))
    op.add_column('order_items', sa.Column('checked_in_at', sa.DateTime(), nullable=True))
    # Store UUID as TEXT/BLOB depending on your SQLAlchemy UUID setup; keep as String for SQLite compatibility.
    op.add_column('order_items', sa.Column('checked_in_by', sa.String(length=36), nullable=True))


def downgrade():
    op.drop_column('order_items', 'checked_in_by')
    op.drop_column('order_items', 'checked_in_at')
    op.drop_column('order_items', 'checked_in')
