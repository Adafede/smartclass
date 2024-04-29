"""Transform InChI to SMILES."""

from __future__ import annotations

from smartclass.chem.conversion.inchi_to_smiles import inchi_to_smiles
from smartclass.chem.helpers.fix_inchi_tautomerization import fix_inchi_tautomerization


def transform_inchi_to_smiles_isomeric(result: dict) -> dict | None:
    """
    Transform InChI to SMILES.

    :param result: A single query result (dictionary).
    :type result: dict

    :returns: Transformed query result.
    :rtype: Union[dict, None]
    """
    smiles = inchi_to_smiles(result.get("inchi", ""))
    if smiles is not None:
        smiles = fix_inchi_tautomerization(smiles)
        if "@" in smiles or "\\" in smiles or "/" in smiles:
            transformed_result = {
                "qid": result.get("structure", "").replace("http://www.wikidata.org/entity/", ""),
                "P2017": '"' + smiles + '"',
                "S887": "Q123137214",
            }
            return transformed_result
        else:
            return None
    else:
        return None
