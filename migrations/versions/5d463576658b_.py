"""empty message

Revision ID: 5d463576658b
Revises: 3423d9819cc9
Create Date: 2020-12-13 11:24:22.653261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d463576658b'
down_revision = '3423d9819cc9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('id_siswa', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'user', 'siswa', ['id_siswa'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'id_siswa')
    # ### end Alembic commands ###