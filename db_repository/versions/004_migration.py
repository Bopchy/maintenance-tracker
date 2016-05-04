from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
Admin = Table('Admin', pre_meta,
    Column('admin_id', INTEGER, primary_key=True, nullable=False),
)

Admin = Table('Admin', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
)

RequestsLog = Table('RequestsLog', pre_meta,
    Column('request_id', INTEGER, primary_key=True, nullable=False),
    Column('request_summ', VARCHAR(length=200)),
    Column('body', VARCHAR(length=2000)),
    Column('timestamp', DATETIME),
)

RequestsLog = Table('RequestsLog', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('request_summ', String(length=200)),
    Column('body', String(length=2000)),
    Column('timestamp', DateTime),
    Column('client_id', Integer),
    Column('staff_id', Integer),
)

StaffMemberProfile = Table('StaffMemberProfile', pre_meta,
    Column('staff_id', INTEGER, primary_key=True, nullable=False),
    Column('first_name', VARCHAR(length=80)),
    Column('last_name', VARCHAR(length=80)),
    Column('phone_no', INTEGER),
    Column('email', VARCHAR(length=100)),
)

StaffMemberProfile = Table('StaffMemberProfile', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('first_name', String(length=80)),
    Column('last_name', String(length=80)),
    Column('phone_no', Integer),
    Column('email', String(length=100)),
)

ClientProfile = Table('ClientProfile', pre_meta,
    Column('client_id', INTEGER, primary_key=True, nullable=False),
    Column('client_name', VARCHAR),
    Column('phone_no', INTEGER),
    Column('email', VARCHAR),
)

ClientProfile = Table('ClientProfile', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('client_name', String),
    Column('phone_no', Integer),
    Column('email', String),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['Admin'].columns['admin_id'].drop()
    post_meta.tables['Admin'].columns['id'].create()
    pre_meta.tables['RequestsLog'].columns['request_id'].drop()
    post_meta.tables['RequestsLog'].columns['client_id'].create()
    post_meta.tables['RequestsLog'].columns['id'].create()
    post_meta.tables['RequestsLog'].columns['staff_id'].create()
    pre_meta.tables['StaffMemberProfile'].columns['staff_id'].drop()
    post_meta.tables['StaffMemberProfile'].columns['id'].create()
    pre_meta.tables['ClientProfile'].columns['client_id'].drop()
    post_meta.tables['ClientProfile'].columns['id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['Admin'].columns['admin_id'].create()
    post_meta.tables['Admin'].columns['id'].drop()
    pre_meta.tables['RequestsLog'].columns['request_id'].create()
    post_meta.tables['RequestsLog'].columns['client_id'].drop()
    post_meta.tables['RequestsLog'].columns['id'].drop()
    post_meta.tables['RequestsLog'].columns['staff_id'].drop()
    pre_meta.tables['StaffMemberProfile'].columns['staff_id'].create()
    post_meta.tables['StaffMemberProfile'].columns['id'].drop()
    pre_meta.tables['ClientProfile'].columns['client_id'].create()
    post_meta.tables['ClientProfile'].columns['id'].drop()
