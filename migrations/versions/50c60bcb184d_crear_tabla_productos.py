"""crear tabla productos

Revision ID: 50c60bcb184d
Revises: fb2844051e50
Create Date: 2022-08-19 22:39:28.266225

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50c60bcb184d'
down_revision = 'fb2844051e50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('productos',
    sa.Column('productoId', sa.Integer(), nullable=False),
    sa.Column('productoNombre', sa.String(length=255), nullable=False),
    sa.Column('productoDescripcion', sa.String(length=255), nullable=False),
    sa.Column('productoPrecio', sa.Float(), nullable=False),
    sa.Column('productoImagen', sa.Text(), nullable=False),
    sa.Column('estado', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('categoriaId', sa.Integer(), nullable=True),
    sa.Column('preferenciaId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['categoriaId'], ['categorias.categoriaId'], ),
    sa.ForeignKeyConstraint(['preferenciaId'], ['preferencias.preferenciaId'], ),
    sa.PrimaryKeyConstraint('productoId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('productos')
    # ### end Alembic commands ###
