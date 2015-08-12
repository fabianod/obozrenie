#!/usr/bin/python
# This source file is part of Obozrenie
# Copyright 2015 Artem Vorotnikov

# For more information, see https://github.com/skybon/obozrenie

# Obozrenie is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3, as
# published by the Free Software Foundation.

# Obozrenie is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Obozrenie.  If not, see <http://www.gnu.org/licenses/>.

"""Contains templates for insertion into GUI body"""

from gi.repository import Gtk


def get_option_widget(option_dict):
    name = option_dict["name"]
    description = option_dict["description"]
    widget_type = option_dict["gtk_type"]
    if widget_type == "CheckButton":
        widget = get_checkbutton(label_text=name+":",
                                 tooltip_text=description)
    if widget_type == "Entry with Label":
        widget = get_entry_with_label(label_text=name+":",
                                      tooltip_text=description)
    else:
        print("No widget generated for type " + widget_type)
        widget = None

    return widget


def get_checkbutton(label_text="", tooltip_text=""):
    checkbutton = Gtk.CheckButton.new()

    checkbutton.set_label(label_text)
    checkbutton.set_tooltip_text(tooltip_text)

    return checkbutton, checkbutton


def get_entry_with_label(label_text="", tooltip_text=""):
    grid = Gtk.Grid()
    entry = Gtk.Entry()
    label = Gtk.Label()

    label.set_text(label_text)
    label.set_halign(Gtk.Align.START)

    entry.set_tooltip_text(tooltip_text)
    entry.set_halign(Gtk.Align.END)

    grid.add(label)
    grid.add(entry)

    grid.set_column_homogeneous(True)
    grid.set_column_spacing(5)

    return grid, entry


class PreferencesDialog(Gtk.Dialog):
    def __init__(self, parent, game, game_table, dynamic_settings_table, callback_start=None, callback_close=None):
        Gtk.Dialog.__init__(self, None, parent)

        self.callback_close = None

        if callback_close is not None:
            self.callback_close = callback_close

        self.game = game

        preferences_grid, self.widget_option_mapping = get_preferences_grid(game, game_table, dynamic_settings_table)

        if callback_start is not None:
            callback_start(self.game, self.widget_option_mapping)

        self.set_title(game_table[game]["info"]["name"] + " preferences")
        self.get_content_area().pack_start(preferences_grid, True, True, 0)

        button = self.add_button("Close", Gtk.ResponseType.CLOSE)
        button.connect("clicked", self.cb_close_button_clicked)

        self.show_all()

    def cb_close_button_clicked(self, widget):
        if self.callback_close is not None:
            self.callback_close(self.game, self.widget_option_mapping)
        self.destroy()


def get_preferences_grid(game, game_table, dynamic_settings_table):
    grid = Gtk.Grid()

    grid.set_orientation(Gtk.Orientation.VERTICAL)
    grid.set_row_spacing(5)

    widget_option_mapping = {}

    for option in game_table[game]["settings"]:
        widget = get_option_widget(dynamic_settings_table[option])

        widget_grid = widget[0]
        widget_main = widget[1]

        grid.add(widget_grid)

        widget_option_mapping[option] = widget_main

    return grid, widget_option_mapping