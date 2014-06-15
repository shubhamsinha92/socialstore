# -*- coding: utf-8 -*-
#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
# coding: utf-8
import chats


@auth.requires_login()
def index():
    return chats.index(db)


@auth.requires_signature()
def message_new():
    return chats.message_new(db)


@auth.requires_signature()
def message_updates():
    # need to unlock the session when using
    # session file, should not be need it when
    # using session in db, or in a cookie
    session._unlock(response)
    return chats.message_updates(db)


def user():
    return dict(form=auth())


'''
import chats
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    form = SQLFORM.factory(Field('user_or_employee', requires = IS_IN_SET(['user', 'employee']))).process()
    if form.accepted:
        if form.vars.user_or_employee == 'user':
            redirect(URL('user'))
        elif form.vars.user_or_employee == 'employee':
            redirect(URL('employee_register'))
    return dict(form=form)

def employee_register():
    form = SQLFORM(db.employee)
    if form.process().accepted:
        redirect(URL('welcome')) # or whatever function
    return dict(form=form)

def welcome():
    return "Welcome employee"

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
'''
