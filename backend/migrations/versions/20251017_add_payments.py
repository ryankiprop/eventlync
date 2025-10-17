"""
add payments table

Revision ID: 20251017_add_payments
Revises: 
Create Date: 2025-10-17 11:59:00
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '20251017_add_payments'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        'payments',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('order_id', postgresql.UUID(as_uuid=True), nullable=False, index=True),
        sa.Column('provider', sa.String(length=50), nullable=False, server_default='mpesa'),
        sa.Column('amount', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('phone', sa.String(length=20), nullable=True),
        sa.Column('status', sa.String(length=20), nullable=False, server_default='initiated'),
        sa.Column('merchant_request_id', sa.String(length=100), nullable=True),
        sa.Column('checkout_request_id', sa.String(length=100), nullable=True),
        sa.Column('result_code', sa.String(length=20), nullable=True),
        sa.Column('result_desc', sa.String(length=255), nullable=True),
        sa.Column('raw_callback', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    )
    op.create_index('ix_payments_order_id', 'payments', ['order_id'])
    op.create_index('ix_payments_checkout_request_id', 'payments', ['checkout_request_id'])


def downgrade() -> None:
    op.drop_index('ix_payments_checkout_request_id', table_name='payments')
    op.drop_index('ix_payments_order_id', table_name='payments')
    op.drop_table('payments')
