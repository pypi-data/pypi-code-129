from django.template.loader import render_to_string
from django.conf import settings

BODEGAS = (
    ("SER01626", "SANTA FE"),
    ("SER01626", "PLANTA XOCHIMILCO"),
    ("SER01626", "TLAHUAC"),
)



CAMPOS_ENCABEZADOS = (
    ("orden_compra", BODEGAS),
    ("folio", "str"),
    ("serie", "str"),
    ("tipo_prov", "str"),
)


def generar_addenda(diccionario):
    return render_to_string("cfdi/addendas/asofarma.xml", diccionario)
