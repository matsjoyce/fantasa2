"""head

Revision ID: 8fa531e987ed
Revises: f9d9d821799a
Create Date: 2023-08-12 15:23:01.419394

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "8fa531e987ed"
down_revision = "f9d9d821799a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("track") as batch_op:
        batch_op.add_column(
            sa.Column("listenings", sa.Integer(), nullable=False, server_default="0")
        )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("track") as batch_op:
        batch_op.drop_column("listenings")
    # ### end Alembic commands ###
