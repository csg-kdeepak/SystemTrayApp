from pywinauto import Application


def init_sv_login(event, sv_app, menu_names):
    """
    function to get the label that is clicked
    and launch the sv application
    """
    # Launch the application
    evt_id = event.GetId() - 1
    app = Application(backend='uia').start(sv_app)

    # get the Dialogue Handler
    dlg = app.window(title_re='Singleview Convergent Billing.*')

    db_pane = dlg.child_window(title="Database", control_type="Pane")

    # set variables from the clicked menu
    keys_list = list(menu_names.keys())
    db = menu_names[keys_list[evt_id]][0]
    uname = menu_names[keys_list[evt_id]][1]
    passwd = menu_names[keys_list[evt_id]][2]
    # set database name
    db_edit = db_pane.Edit0
    db_edit.set_text(db)

    # set user name
    uname_edit = db_pane.Edit3
    uname_edit.set_text(uname)

    # set password name
    pass_edit = db_pane.Edit2
    pass_edit.set_text(passwd)

    dlg.Ok.click()
