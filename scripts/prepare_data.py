from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]

INPUT_PATH = ROOT / "data" / "raw" / "classified_abstracts.json"
OUTPUT_PATH = ROOT / "data" / "processed" / "dataset.csv"


def main() -> None:
    df = pd.read_json(INPUT_PATH)

    required_columns = ["DOI", "Abstract", "Label"]
    missing = set(required_columns) - set(df.columns)

    if missing:
        raise ValueError(f"Faltan columnas requeridas: {sorted(missing)}")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(OUTPUT_PATH, index=False)

    print(f"Archivo original: {INPUT_PATH}")
    print(f"Archivo generado: {OUTPUT_PATH}")
    print(f"Filas y columnas: {df.shape}")
    print(f"Columnas: {list(df.columns)}")


if __name__ == "__main__":
    main()
    