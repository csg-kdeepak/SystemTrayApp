import wx
import wx.adv
import login_sv
from read_ini import get_login_data
from pywinauto import application

TRAY_TOOLTIP = 'Singleview Launcher'
TRAY_ICON = 'launch.png'


class TaskBarIcon(wx.adv.TaskBarIcon):

    # Class member variables
    env_dict = {}  # List of SV environments
    sv_app = ''  # Location of SV billing application

    def __init__(self):
        super(TaskBarIcon, self).__init__()
        self.set_icon(TRAY_ICON)
        self.set_app_parm()

    def CreatePopupMenu(self):
        menu = wx.Menu()
        """
        Loop through the menu_names and add each button
        """
        x = 1
        for names in self.env_dict.keys():
            menu.Append(x, names, 'status entry')
            self.Bind(wx.EVT_MENU_RANGE, lambda event=x: self.call_sv_app(event),
                      id=1, id2=len(self.env_dict.keys()))
            x += 1

        item = wx.MenuItem(menu, -1, 'Exit')
        menu.Bind(wx.EVT_MENU, self.on_exit, id=item.GetId())
        menu.AppendItem(item)
        return menu

    def call_sv_app(self, event):
        try:
            login_sv.init_sv_login(event, self.sv_app, self.env_dict)
        except application.AppStartError as err:
            show_msg_box("Singview Application Start Failure : {}".format(err))

    def set_icon(self, path):
        icon = wx.EmptyIcon()
        icon.CopyFromBitmap(wx.Bitmap(TRAY_ICON, wx.BITMAP_TYPE_PNG))
        # icon = wx.Icon(TRAY_ICON, wx.BITMAP_TYPE_PNG, 16, 16)
        self.SetIcon(icon, TRAY_TOOLTIP)

    def set_app_parm(self):
        try:
            (env_list, self.sv_app) = get_login_data()
            # have environment list as dict.
            for entry in env_list:
                self.env_dict[entry[0]] = entry[1:]
        except IOError as err:
            show_msg_box("OS error: {0}".format(err))

    def on_exit(self, event):
        wx.CallAfter(self.Destroy)


def show_msg_box(msg):
    wx.MessageBox(msg, 'ERROR:', wx.OK | wx.ICON_ERROR)


def main():
    app = wx.App()
    tb = TaskBarIcon()
    app.MainLoop()


if __name__ == '__main__':
    main()
