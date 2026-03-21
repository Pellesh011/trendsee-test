"""Initial schema: users, posts

Revision ID: 73fc5e9c14f6
Revises: 
Create Date: 2026-03-21 11:36:10.542183

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '73fc5e9c14f6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Create extension if not exists
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')

    # Create users table
    op.create_table('users',
        sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    # Trigger for users updated_at
    op.execute('''
        CREATE OR REPLACE FUNCTION update_updated_at_column()
        RETURNS TRIGGER AS $$
        BEGIN
            NEW.updated_at = CURRENT_TIMESTAMP;
            RETURN NEW;
        END;
        $$ language 'plpgsql';
    ''')
    op.execute('CREATE TRIGGER update_users_updated_at BEFORE UPDATE ON users FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();')

    # Create posts table
    op.create_table('posts',
        sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
        sa.Column('user_id', sa.UUID(), nullable=False),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('text', sa.Text(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    # Trigger for posts updated_at
    op.execute('CREATE TRIGGER update_posts_updated_at BEFORE UPDATE ON posts FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();')

    # Create indexes
    op.create_index('idx_posts_user_id', 'posts', ['user_id'], unique=False)
    op.create_index('idx_posts_created_at', 'posts', ['created_at'], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index('idx_posts_created_at', table_name='posts')
    op.drop_index('idx_posts_user_id', table_name='posts')
    op.drop_table('posts')
    op.execute('DROP TRIGGER IF EXISTS update_users_updated_at ON users;')
    op.drop_table('users')
    op.execute('DROP FUNCTION IF EXISTS update_updated_at_column();')
    op.execute('DROP EXTENSION IF EXISTS "uuid-ossp";')
