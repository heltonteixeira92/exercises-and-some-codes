def update_completeuser_pbuser(user, field, value, field2=None, value2=None, **others):

    query = f"""UPDATE usuario_usuariocompleto SET {field} = '{value}'"""

    if field2:
        query += f""", {field2} = '{value2}'"""

    if others:
        for f, v in others.items():
            query += f""", {f} = '{v}'"""

    query += f""" WHERE id = '{user}'"""

    print(query)


update_completeuser_pbuser(10, field='logradouro', value='noranda',
                           field2='numero', value2='numero', field3='bairro', value3='district',
                           field4='state', value4='state')
