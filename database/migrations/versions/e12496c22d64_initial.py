"""Initial

Revision ID: e12496c22d64
Revises: 
Create Date: 2022-04-03 22:38:11.755511

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'e12496c22d64'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('card',
                    sa.Column('number', sa.Integer(), nullable=False),
                    sa.Column('filename', sa.String(), nullable=False),
                    sa.Column('type', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('filename', 'type')
                    )
    op.create_table('game',
                    sa.Column('id', sa.String(), nullable=False),
                    sa.Column('round', sa.Integer(), nullable=False),
                    sa.Column('start_date', sa.String(), nullable=False),
                    sa.Column('notes', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('player',
                    sa.Column('id', sa.String(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('damage', sa.Integer(), nullable=False),
                    sa.Column('life', sa.Integer(), nullable=False),
                    sa.Column('powered_down', sa.Boolean(), nullable=False),
                    sa.Column('will_power_down', sa.Boolean(), nullable=False, default=0),
                    sa.Column('avatar_filename', sa.String(), nullable=False),
                    sa.Column('instructions', sa.String(), nullable=True),
                    sa.Column('active', sa.Boolean(), nullable=False, default=1),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('board_state',
                    sa.Column('parent_id', sa.String(), nullable=False),
                    sa.Column('filename', sa.String(), nullable=False),
                    sa.ForeignKeyConstraint(['parent_id'], ['game.id'], ),
                    sa.PrimaryKeyConstraint('filename')
                    )
    op.create_table('deck',
                    sa.Column('parent_id', sa.String(), nullable=False),
                    sa.Column('type', sa.String(), nullable=False),
                    sa.Column('card_order', sa.Integer(), nullable=False),
                    sa.Column('card_type', sa.String(), nullable=False),
                    sa.Column('card_num', sa.Integer(), nullable=False),
                    sa.Column('card_filename', sa.String(), nullable=False),
                    sa.ForeignKeyConstraint(['parent_id'], ['game.id'], ),
                    sa.ForeignKeyConstraint(['parent_id'], ['player.id'], ),
                    sa.PrimaryKeyConstraint('parent_id', 'type', 'card_order')
                    )
    op.create_table('registers',
                    sa.Column('parent_id', sa.String(), nullable=False),
                    sa.Column('register_num', sa.Integer(), nullable=False),
                    sa.Column('card_num', sa.Integer(), nullable=False),
                    sa.Column('card_filename', sa.String(), nullable=False),
                    sa.Column('locked', sa.Boolean(), nullable=False),
                    sa.Column('throw', sa.Boolean(), nullable=False, default=0),
                    sa.ForeignKeyConstraint(['parent_id'], ['player.id'], ),
                    sa.PrimaryKeyConstraint('parent_id', 'register_num')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('registers')
    op.drop_table('deck')
    op.drop_table('board_state')
    op.drop_table('player')
    op.drop_table('game')
    op.drop_table('card')
    # ### end Alembic commands ###