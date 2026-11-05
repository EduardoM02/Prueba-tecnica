# Prueba-tecnica

## Requisitos

- Python 3.10 o superior.
- Pandas.
- OpenPyXL.

## Instalación

1. Clonar o descargar el repositorio.
2. Instalar las dependencias:

```bash
pip install pandas openpyxl
```

## Estructura del proyecto

```text
proyecto/
├── input/
│   └── Datos de entrada simple.xlsx
├── output/
├── main.py
├── procesado.py
└── validaciones.py
```

## Ejecución

Colocar el archivo Excel que se desea procesar dentro de la carpeta `input/`.

Ejecutar el programa desde la raíz del proyecto:

```bash
python main.py
```

El archivo procesado se generará en la carpeta `output/`.

## Validaciones implementadas

- **Beneficiario:** verifica que el nombre no esté vacío.
- **CLABE:** verifica que contenga exactamente 18 dígitos numéricos y no tenga espacios.
- **Importe:** verifica que sea un valor numérico positivo y que no exceda los 2 decimales permitidos.

Los registros se conservan independientemente de su validez. El archivo resultante incluye dos columnas adicionales:

- `Estado`: indica si el registro es válido o inválido.
- `motivo_error`: describe los errores encontrados en cada registro.

Cuando un registro presenta varios errores, todos sus motivos se incluyen en la misma celda.

## ¿Qué fue lo más difícil del reto y cómo lo resolviste?

Lo más desafiante fue manejar correctamente las validaciones y proporcionar mensajes de error específicos para cada registro, especialmente cuando un mismo registro podía presentar varios errores.

Para resolverlo, separé las responsabilidades en dos módulos: uno para las validaciones individuales y otro para el procesamiento del archivo de Excel.

También utilicé Decimal para validar los importes y evitar problemas de precisión asociados a los números de punto flotante. Para las CLABE, opté por tratarlas como texto, evitando problemas relacionados con la interpretación numérica de Excel.
