from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
staff_member = Table('staff_member', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('first_name', VARCHAR(length=80)),
    Column('last_name', VARCHAR(length=80)),
    Column('phone_no', INTEGER),
    Column('email', VARCHAR(length=100)),
)

Admin = Table('Admin', post_meta,
    Column('admin_id', Integer, primary_key=True, nullable=False),
)

ClientProfile = Table('ClientProfile', post_meta,
    Column('client_id', Integer, primary_key=True, nullable=False),
    Column('client_name', String),
    Column('phone_no', Integer),
    Column('email', String),
)

RequestsLog = Table('RequestsLog', post_meta,
    Column('request_id', Integer, primary_key=True, nullable=False),
    Column('request_summ', String(length=200)),
    Column('body', String(length=2000)),
    Column('timestamp', DateTime),
    Column('client_id', Integer),
    Column('staff_id', Integer),
)

StaffMemberProfile = Table('StaffMemberProfile', post_meta,
    Column('staff_id', Integer, primary_key=True, nullable=False),
    Column('first_name', String(length=80)),
    Column('last_name', String(length=80)),
    Column('phone_no', Integer),
    Column('email', String(length=100)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['staff_member'].drop()
    post_meta.tables['Admin'].create()
    post_meta.tables['ClientProfile'].create()
    post_meta.tables['RequestsLog'].create()
    post_meta.tables['StaffMemberProfile'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['staff_member'].create()
    post_meta.tables['Admin'].drop()
    post_meta.tables['ClientProfile'].drop()
    post_meta.tables['RequestsLog'].drop()
    post_meta.tables['StaffMemberProfile'].drop()
