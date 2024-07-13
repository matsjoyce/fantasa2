"""head

Revision ID: 88395175f4cf
Revises: 0a1d983d0f37
Create Date: 2024-07-04 17:17:07.817714

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "88395175f4cf"
down_revision = "0a1d983d0f37"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "cover",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("album_id", sa.Integer(), nullable=True),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("folder", sa.String(length=256), nullable=False),
        sa.Column("extension", sa.String(length=100), nullable=False),
        sa.ForeignKeyConstraint(["album_id"], ["album.id"], name="fk_track_album"),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("cover")
    # ### end Alembic commands ###
