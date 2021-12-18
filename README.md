# RDMolReader
An expansion for RDKit to read all types of files in one line

# How to use?
Add this single .py file to your project and import MolFromFile() from this file.

**input:** molecule file name

**output:** a list of molecules (always returns a list, even if you have one molecule)

*example:*
```
from RDMolReader import MolFromFile
mol_list = MolFromFile('mymol.mol')  # this returns a list with length 1
mols_list = MolFromFile('mymols.sdf')  # this returns a list of molecules from mymols.sdf file
```
