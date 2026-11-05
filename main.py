from procesado import procesar_excel

def main():
    archivo_entrada = "input/Datos de entrada simple.xlsx"
    archivo_salida = "output/Resultadoxlsx"

    try:
        df = procesar_excel(archivo_entrada)
        df.to_excel(archivo_salida, index=False)

        print("Archivo procesado correctamente.")
        print(f"Resultado guardado en: {archivo_salida}")

    except FileNotFoundError:
        print("Error: No se encontró el archivo de entrada.")

    except ValueError as e:
        print(f"Error en los datos: {e}")

    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()