# Dado o seguinte objeto:
objeto = [{
"message_tag": "TEMPERATURE_MIN",
"element_dictionary": "INMET",
"element": "MIN_AIR_TEMP_2M_C"
}, {
"message_tag": "RELATIVE_HUMIDITY_MIN",
"element_dictionary": "INMET",
"element": "MIN_REL_HUMIDITY_2M_PCT"
}, {
"message_tag": "temperature",
"element": "AVG_AIR_TEMP_2M_C",
"element_dictionary": "METAR"
}, {
"message_tag": "PrecMin",
"element_dictionary": "SIMEPAR_MET",
"element": "DISCARDED",
}, {
"message_tag": "Prec",
"element_dictionary": "SIMEPAR_MET",
"element": "ACCUM_PRECIP_2M_MM",
}]
""" Crie uma função que receba o objeto acima e retorne no seguinte formato:
[{
'INMET': ['MIN_AIR_TEMP_2M_C', 'MIN_REL_HUMIDITY_2M_PCT'],
'METAR': ['AVG_AIR_TEMP_2M_C'],
'SIMEPAR_MET': ['DISCARDED', 'ACCUM_PRECIP_2M_MM']
}]

"""

lista = []
def return_obj_formatter(objeto):
    for i in objet



return_obj_formatter(objeto)