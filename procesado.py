import pandas as pd
from validaciones import (
    validar_importe,
    validar_clabe,
    validar_beneficiario
)


def procesar_excel(input_file):

    df = pd.read_excel(input_file, dtype={"CLABE": str})

    columnas_requeridas = ["Beneficiario", "CLABE", "Importe"]

    columnas_faltantes = [
        col for col in columnas_requeridas
        if col not in df.columns
    ]

    if columnas_faltantes:
        raise ValueError(f"Faltan columnas: {columnas_faltantes}")

    df["Estado"] = "Válido"
    df["motivo_error"] = ""

    validaciones = {
        "Beneficiario": df["Beneficiario"].apply(validar_beneficiario),
        "CLABE": df["CLABE"].apply(validar_clabe),
        "Importe": df["Importe"].apply(validar_importe)
    }

    for columna, errores in validaciones.items():
        registros_invalidos = errores.notna()

        df.loc[registros_invalidos, "Estado"] = "Inválido"

        df.loc[registros_invalidos, "motivo_error"] += (
                errores[registros_invalidos] + "; "
        )

    df["motivo_error"] = df["motivo_error"].str.rstrip("; ")

    return df
