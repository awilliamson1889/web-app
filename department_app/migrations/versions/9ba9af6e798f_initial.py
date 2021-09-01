"""Initial

Revision ID: 9ba9af6e798f
Revises: 
Create Date: 2021-08-03 18:29:24.554576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ba9af6e798f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('Department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('manager', sa.String(length=100), nullable=False),
    sa.Column('date_of_creation', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('Location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('Permission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('Skill',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('Employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('surname', sa.String(length=50), nullable=False),
    sa.Column('date_of_birth', sa.String(length=50), nullable=True),
    sa.Column('salary', sa.Float(), nullable=False),
    sa.Column('phone', sa.String(length=13), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('date_of_joining', sa.String(length=50), nullable=False),
    sa.Column('department', sa.Integer(), nullable=False),
    sa.Column('location', sa.Integer(), nullable=False),
    sa.Column('work_address', sa.Integer(), nullable=False),
    sa.Column('key_skill', sa.Integer(), nullable=False),
    sa.Column('permission', sa.Integer(), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['department'], ['Department.id'], ),
    sa.ForeignKeyConstraint(['key_skill'], ['Skill.id'], ),
    sa.ForeignKeyConstraint(['location'], ['Location.id'], ),
    sa.ForeignKeyConstraint(['permission'], ['Permission.id'], ),
    sa.ForeignKeyConstraint(['work_address'], ['Address.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Employee')
    op.drop_table('Skill')
    op.drop_table('Permission')
    op.drop_table('Location')
    op.drop_table('Department')
    op.drop_table('Address')
    # ### end Alembic commands ###
