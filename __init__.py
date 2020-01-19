from aqt import mw
from aqt.editor import Editor
from anki.hooks import addHook
import re

expr1 = re.compile(r"(\\[a-z]+{)?{{c[0-9]+::")
expr2 = re.compile(r"}}}?")

def purgeClozes(self):
    for name, val in list(self.note.items()):
        val1 = re.sub(expr1, '', val)
        val2 = re.sub(expr2, '', val1)
        self.note.__setitem__(name, val2)

    self.note.flush()
    mw.reset()

def onAlert(self):
    self.web.eval("wrap('\\\\alert\{', '\}');")

def onSetupShortcuts(cuts, self):
    cuts += [("Ctrl+J", self.purgeClozes),
             ("Ctrl+W", self.onAlert)]

Editor.purgeClozes = purgeClozes
Editor.onAlert = onAlert
addHook("setupEditorShortcuts", onSetupShortcuts)
