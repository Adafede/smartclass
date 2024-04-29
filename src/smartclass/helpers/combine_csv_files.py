"""Combine multiple CSV files into a single CSV file."""

from __future__ import annotations

import polars

__all__ = [
    "combine_csv_files",
]


def combine_csv_files(input_files: list[str] | str, output_file: str, separator="\t") -> None:
    """
    Combine multiple CSV files into a single CSV file.

    :param input_files: List of input CSV file paths or a single input CSV file path.
    :type input_files: Union[list[str], str]

    :param output_file: Output CSV file path where the combined data will be saved.
    :type output_file: str

    :param separator: Separator used in the CSV files (default is 'tab').
    :type separator: str
    """
    if isinstance(input_files, str):
        input_files = [input_files]  # Ensure input_files is a list

    # Create an empty list to store DataFrames
    dfs = []

    # Read each CSV file and store it in the list
    for file_path in input_files:
        df = polars.read_csv(file_path, separator=separator)
        dfs.append(df)

    # Merge all DataFrames using a common set of columns
    common_columns = set(dfs[0].columns)

    for df in dfs[1:]:
        common_columns &= set(df.columns)

    # Create a merged DataFrame by joining on common columns
    merged_df = dfs[0]
    for df in dfs[1:]:
        merged_df = merged_df.join(df, on=list(common_columns), how="outer")

    # Export the merged DataFrame as a CSV file
    merged_df.write_csv(output_file, separator=separator)


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)

    input_files = [
        "scratch/wikidata_classes_cxsmiles.tsv",
        "scratch/wikidata_classes_smarts.tsv",
        "scratch/wikidata_classes_smiles.tsv",
        "scratch/wikidata_classes_smiles_isomeric.tsv",
        "scratch/wikidata_classes_taxonomy.tsv",
    ]
    output_file = "scratch/wikidata_classes_full.tsv"

    combine_csv_files(input_files, output_file)
    logging.info(output_file)
