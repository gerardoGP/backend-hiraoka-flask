"""Initial migration

Revision ID: 04cabd9332d4
Revises: 
Create Date: 2022-08-19 20:32:28.477208

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04cabd9332d4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categorias',
    sa.Column('categoriaId', sa.Integer(), nullable=False),
    sa.Column('categoriaNombre', sa.String(length=255), nullable=False),
    sa.Column('categoriaDescripcion', sa.String(length=255), nullable=False),
    sa.Column('estado', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.PrimaryKeyConstraint('categoriaId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('categorias')
    # ### end Alembic commands ###
