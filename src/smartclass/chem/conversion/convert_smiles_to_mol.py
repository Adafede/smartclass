"""Convert a structure SMILES to MOL."""

from __future__ import annotations

from rdkit.Chem import Mol, MolFromSmiles

__all__ = [
    "convert_smiles_to_mol",
]


def convert_smiles_to_mol(smiles: str) -> Mol | None:
    """
    Convert a structure SMILES to MOL.

    :param smiles: A SMILES.
    :type smiles: str

    :returns: A MOL.
    :rtype: Union[Mol, None]
    """
    return MolFromSmiles(smiles)


if __name__ == "__main__":
    smiles_to_test = ["N[C@@H](CCCNC(N)=N)C(O)=O"]

    for smiles in smiles_to_test:
        convert_smiles_to_mol(smiles)
