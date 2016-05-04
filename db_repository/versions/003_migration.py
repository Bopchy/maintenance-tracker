from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
RequestsLog = Table('RequestsLog', pre_meta,
    Column('request_id', INTEGER, primary_key=True, nullable=False),
    Column('request_summ', VARCHAR(length=200)),
    Column('body', VARCHAR(length=2000)),
    Column('timestamp', DATETIME),
    Column('client_id', INTEGER),
    Column('staff_id', INTEGER),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['RequestsLog'].columns['client_id'].drop()
    pre_meta.tables['RequestsLog'].columns['staff_id'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['RequestsLog'].columns['client_id'].create()
    pre_meta.tables['RequestsLog'].columns['staff_id'].create()
