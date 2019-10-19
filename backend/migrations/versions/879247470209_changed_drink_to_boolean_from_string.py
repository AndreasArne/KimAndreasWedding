"""Changed drink to boolean from string

Revision ID: 879247470209
Revises: 0045aa4bea13
Create Date: 2019-10-15 17:41:05.964034

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '879247470209'
down_revision = '0045aa4bea13'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('party',
    sa.Column('id', sa.String(length=10), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.Column('osa', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('email'),
    sa.UniqueConstraint('id')
    )
    op.create_table('guest',
    sa.Column('name', sa.String(length=140), nullable=False),
    sa.Column('coming', sa.Boolean(), nullable=True),
    sa.Column('food', sa.String(length=140), nullable=True),
    sa.Column('drink', sa.Boolean(), nullable=True),
    sa.Column('allergy', sa.String(length=255), nullable=True),
    sa.Column('party_id', sa.String(length=10), nullable=False),
    sa.ForeignKeyConstraint(['party_id'], ['party.id'], ),
    sa.PrimaryKeyConstraint('name', 'party_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('guest')
    op.drop_table('party')
    # ### end Alembic commands ###