
# Copyright (C) 2013 - Oscar Campos <oscar.campos@member.fsf.org>
# This program is Free Software see LICENSE file for details

import sublime_plugin

from ..anaconda_lib.linting.sublime import ANACONDA, erase_lint_marks


class AnacondaDisableLinting(sublime_plugin.WindowCommand):
    """Disable the linting for the current buffer
    """

    def run(self):
        if self.window.active_view().file_name() is not None:
            ANACONDA['DISABLED'].append(self.window.active_view().file_name())

        erase_lint_marks(self.window.active_view())

    def is_enabled(self):
        """Determines if the command is enabled
        """

        view = self.window.active_view()
        if view.file_name() in ANACONDA['DISABLED']:
            return False

        location = view.sel()[0].begin()
        matcher = 'source.python'
        return view.match_selector(location, matcher)
