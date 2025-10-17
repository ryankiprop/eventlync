"""Add missing indexes and constraints

Revision ID: 20241017_add_missing_indexes
Revises: merge_heads_20241017
Create Date: 2024-10-17 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic
revision = '20241017_add_missing_indexes'
down_revision = 'merge_heads_20241017'
branch_labels = None
depends_on = None

def upgrade():
    # Add index to payments.order_id
    op.create_index(op.f('ix_payments_order_id'), 'payments', ['order_id'], unique=False)
    
    # Add index to payments.checkout_request_id
    op.create_index(op.f('ix_payments_checkout_request_id'), 'payments', ['checkout_request_id'], unique=True)
    
    # Add NOT NULL constraint to payments.phone
    op.alter_column('payments', 'phone', existing_type=sa.VARCHAR(length=20), nullable=False)
    
    # Add index to orders.user_id
    op.create_index(op.f('ix_orders_user_id'), 'orders', ['user_id'], unique=False)
    
    # Add index to orders.event_id
    op.create_index(op.f('ix_orders_event_id'), 'orders', ['event_id'], unique=False)
    
    # Add index to order_items.order_id
    op.create_index(op.f('ix_order_items_order_id'), 'order_items', ['order_id'], unique=False)
    
    # Add index to order_items.ticket_type_id
    op.create_index(op.f('ix_order_items_ticket_type_id'), 'order_items', ['ticket_type_id'], unique=False)

def downgrade():
    # Drop indexes in reverse order
    op.drop_index(op.f('ix_order_items_ticket_type_id'), table_name='order_items')
    op.drop_index(op.f('ix_order_items_order_id'), table_name='order_items')
    op.drop_index(op.f('ix_orders_event_id'), table_name='orders')
    op.drop_index(op.f('ix_orders_user_id'), table_name='orders')
    op.alter_column('payments', 'phone', existing_type=sa.VARCHAR(length=20), nullable=True)
    op.drop_index(op.f('ix_payments_checkout_request_id'), table_name='payments')
    op.drop_index(op.f('ix_payments_order_id'), table_name='payments')
