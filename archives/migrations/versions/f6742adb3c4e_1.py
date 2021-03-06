"""1

Revision ID: f6742adb3c4e
Revises: 
Create Date: 2018-04-11 19:32:24.408803

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6742adb3c4e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_address_hash', sa.String(length=256), nullable=True),
    sa.Column('sender_address_hash', sa.String(length=256), nullable=True),
    sa.Column('time', sa.String(length=60), nullable=True),
    sa.Column('read', sa.Boolean(), nullable=True),
    sa.Column('text', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('notifications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_address_hash', sa.String(length=256), nullable=True),
    sa.Column('time', sa.String(length=60), nullable=True),
    sa.Column('read', sa.Boolean(), nullable=True),
    sa.Column('headline', sa.String(length=60), nullable=True),
    sa.Column('text', sa.String(length=240), nullable=True),
    sa.Column('property_token', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('property',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=120), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('body', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_property_token'), 'property', ['token'], unique=True)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('role', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_property_token'), table_name='property')
    op.drop_table('property')
    op.drop_table('notifications')
    op.drop_table('messages')
    # ### end Alembic commands ###
