import gzip
from rdkit import Chem

MOL_FROM_FILE_TYPES = {
    'mol': Chem.MolFromMolFile,
}
SUPPLIER_FROM_FILE_TYPES = {
    'sdf': Chem.SDMolSupplier,
}
GZ_SUPPLIER_FROM_FILE_TYPES = {
    'sdf.gz': Chem.ForwardSDMolSupplier,
}


def MolFromFile(mol_file):
    file_name, file_type = mol_file.rsplit('.')

    mol_list = []
    if file_type in MOL_FROM_FILE_TYPES.keys():  # single mol files
        mol_list.append(MOL_FROM_FILE_TYPES[file_type](mol_file))
    else:  # nultiple mol files
        if file_type == 'gz':  # compressed files
            file_name, file_type2 = file_name.rsplit('.')
            file_type = f'{file_type2}.{file_type}'
            inf = gzip.open(mol_file)
            supplier = GZ_SUPPLIER_FROM_FILE_TYPES[file_type](inf)
        else:  # non-compressed files
            supplier = SUPPLIER_FROM_FILE_TYPES[file_type](mol_file)
        for mol in supplier:
            if mol is None:
                continue
            mol_list.append(mol)
    return mol_list


if __name__ == "__main__":
    pass
