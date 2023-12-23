"""seed

Revision ID: baa85a0fe553
Revises: 442394fdb505
Create Date: 2023-12-23 13:04:27.493635

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "baa85a0fe553"
down_revision: Union[str, None] = "442394fdb505"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.bulk_insert(
        sa.table(
            "product",
            sa.column("name", sa.String),
            sa.column("description", sa.Text),
            sa.column("price", sa.Integer),
            sa.column("image_url", sa.String),
            sa.column("stock", sa.Integer),
        ),
        [
            {
                "name": "Sepatu Sneakers Hitam",
                "description": "Sepatu sneakers warna hitam dengan desain modern.",
                "price": 350000,
                "image_url": "https://example.com/images/sepatu-sneakers-hitam.jpg",
                "stock": 50,
            },
            {
                "name": "Tas Ransel Kulit",
                "description": "Tas ransel berbahan kulit asli dengan banyak kantong.",
                "price": 550000,
                "image_url": "https://example.com/images/tas-ransel-kulit.jpg",
                "stock": 30,
            },
            {
                "name": "Jam Tangan Digital Sport",
                "description": "Jam tangan digital dengan fitur tahan air.",
                "price": 250000,
                "image_url": "https://example.com/images/jam-tangan-digital.jpg",
                "stock": 70,
            },
            {
                "name": "Baju Kaos Cotton",
                "description": "Baju kaos casual berbahan katun yang nyaman dipakai.",
                "price": 150000,
                "image_url": "https://example.com/images/baju-kaos-cotton.jpg",
                "stock": 80,
            },
            {
                "name": "Celana Jeans Slim Fit",
                "description": "Celana jeans dengan potongan slim fit untuk penampilan modern.",
                "price": 450000,
                "image_url": "https://example.com/images/celana-jeans-slim-fit.jpg",
                "stock": 40,
            },
            {
                "name": "Kemeja Flanel",
                "description": "Kemeja flanel dengan motif kotak-kotak yang stylish.",
                "price": 280000,
                "image_url": "https://example.com/images/kemeja-flanel.jpg",
                "stock": 60,
            },
            {
                "name": "Headphone Bluetooth",
                "description": "Headphone nirkabel dengan kualitas suara premium.",
                "price": 400000,
                "image_url": "https://example.com/images/headphone-bluetooth.jpg",
                "stock": 25,
            },
            {
                "name": "Pakaian Renang Anak",
                "description": "Pakaian renang anak-anak dengan motif kartun lucu.",
                "price": 120000,
                "image_url": "https://example.com/images/pakaian-renang-anak.jpg",
                "stock": 55,
            },
            {
                "name": "Laptop 15 inci",
                "description": "Laptop dengan layar 15 inci, RAM 8GB, dan prosesor cepat.",
                "price": 7000000,
                "image_url": "https://example.com/images/laptop-15-inci.jpg",
                "stock": 10,
            },
            {
                "name": "Kacamata Hitam Retro",
                "description": "Kacamata hitam dengan desain retro yang klasik.",
                "price": 180000,
                "image_url": "https://example.com/images/kacamata-hitam-retro.jpg",
                "stock": 45,
            },
        ],
    )


def downgrade() -> None:
    op.execute("DELETE FROM product")
