db = DAL('sqlite://storage.sqlite',
        pool_size=1, check_reserved=['all'],
        migrate_enabled=True, lazy_tables=True)

from gluon.tools import Auth
auth = Auth(db)

auth.define_tables(username=False, signature=False)

auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

db.define_table('chat',
        Field('me_from'),
        Field('me_body', 'text'),
        Field('me_html', 'text'),
        )

STORE_TYPE = ['Department store', 'Discount store', 'Warehouse store', 'Hardware store', 'Boutique']
db.define_table('employee',
                Field('first_name'),
                Field('last_name'),
                Field('store_name'),
                Field('store_type', requires=IS_IN_SET(STORE_TYPE)),
                Field('zip_code'),
                auth.signature)

db.employee.first_name.requires = IS_NOT_EMPTY()
db.employee.last_name.requires = IS_NOT_EMPTY()
db.employee.store_name.requires = IS_NOT_EMPTY()
db.employee.store_type.requires = IS_NOT_EMPTY()
db.employee.zip_code.requires = IS_NOT_EMPTY()
