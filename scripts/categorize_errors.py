from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
ERROR_FILE = ROOT / "reports" / "error_analysis.csv"


def main() -> None:
    df = pd.read_csv(ERROR_FILE)

    categories = [
        "ML poco explicito",
        "etiqueta discutible",
        "ML explicito pero minoritario",
        "prediccion estadistica confundida con ML",
        "terminologia tecnica ambigua",
        "prediccion estadistica confundida con ML",
        "prediccion estadistica confundida con ML",
        "terminologia tecnica ambigua",
        "etiqueta discutible",
        "terminologia tecnica ambigua",
        "ML diluido en texto largo",
        "etiqueta discutible",
        "etiqueta discutible",
        "terminologia tecnica ambigua",
        "ML explicito pero minoritario",
        "prediccion estadistica confundida con ML",
        "etiqueta discutible",
        "terminologia tecnica ambigua",
        "etiqueta discutible",
        "texto insuficiente",
    ]

    df.loc[df.index[:20], "category"] = categories

    df.to_csv(ERROR_FILE, index=False)

    print("Primeros 20 errores categorizados.")
    print()
    print(df[["real", "predicted", "category"]].head(20).to_string(index=True))


if __name__ == "__main__":
    main()
    