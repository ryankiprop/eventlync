"""Merge heads

Revision ID: merge_heads_20241017
Revises: 20251017_add_payments, 387cc944c2dd
Create Date: 2024-10-17 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic
revision = 'merge_heads_20241017'
down_revision = ('20251017_add_payments', '387cc944c2dd')
branch_labels = None
depends_on = None

def upgrade():
    # This is a merge migration - no schema changes needed
    pass

def downgrade():
    # This is a merge migration - no schema changes to undo
    pass
