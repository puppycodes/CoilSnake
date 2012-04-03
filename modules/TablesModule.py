import GenericModule
from modules.Table import Table

import yaml

# For encoding/decoding text entries
# Note: this assumes only 1-character replacements
#class TextTable:
#    def __init__(self, decDict):
#        self._decDict = decDict
#        self._encDict = dict((v,k) for k, v in decDict.iteritems())
#    def decode(self, rom, addr, terminator=None):

class TablesModule(GenericModule.GenericModule):
    _name = "Generic Tables"
    def __init__(self, TableClass, tableIDs):
        self._tables = map(lambda x: TableClass(x), tableIDs)
    def readFromRom(self, rom):
        for t in self._tables:
            t.readFromRom(rom)
    def writeToRom(self, rom):
        for t in self._tables:
            t.writeToRom(rom)
    def writeToProject(self, resourceOpener):
        for t in self._tables:
            f = resourceOpener(t.name(), 'yml')
            f.write(t.dump())
            f.close()
    def readFromProject(self, resourceOpener):
        for t in self._tables:
            f = resourceOpener(t.name(), 'yml')
            contents = f.read()
            f.close()
            t.load(contents)