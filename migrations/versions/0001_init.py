import sqlalchemy as sa
from alembic import op

revision = '0001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('scans',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('module', sa.String),
        sa.Column('target', sa.String),
        sa.Column('args_json', sa.JSON),
        sa.Column('status', sa.String),
        sa.Column('created_at', sa.DateTime),
        sa.Column('finished_at', sa.DateTime),
        sa.Column('returncode', sa.Integer),
        sa.Column('stdout_path', sa.String),
        sa.Column('stderr_path', sa.String),
        sa.Column('profile', sa.String),
    )
    op.create_table('scan_results',
        sa.Column('scan_id', sa.Integer, sa.ForeignKey('scans.id'), primary_key=True),
        sa.Column('result_json', sa.JSON),
    )

def downgrade():
    op.drop_table('scan_results')
    op.drop_table('scans')
