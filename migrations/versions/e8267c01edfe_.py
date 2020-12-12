"""empty message

Revision ID: e8267c01edfe
Revises: 
Create Date: 2020-12-12 15:22:07.371326

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8267c01edfe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pelajaran',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nama_pelajaran', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('siswa',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nis', sa.String(length=10), nullable=False),
    sa.Column('nama', sa.String(length=60), nullable=False),
    sa.Column('tempat_lahir', sa.String(length=30), nullable=False),
    sa.Column('tanggal_lahir', sa.Date(), nullable=False),
    sa.Column('alamat', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nis')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=50), nullable=False),
    sa.Column('passsword', sa.String(length=128), nullable=False),
    sa.Column('hak_akses', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_name')
    )
    op.create_table('nilai',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_siswa', sa.Integer(), nullable=False),
    sa.Column('id_pelajar', sa.Integer(), nullable=False),
    sa.Column('semester', sa.Integer(), nullable=False),
    sa.Column('nilai', sa.Float(precision=5, asdecimal=2), nullable=False),
    sa.ForeignKeyConstraint(['id_pelajar'], ['pelajaran.id'], ),
    sa.ForeignKeyConstraint(['id_siswa'], ['siswa.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('nilai')
    op.drop_table('user')
    op.drop_table('siswa')
    op.drop_table('pelajaran')
    # ### end Alembic commands ###
