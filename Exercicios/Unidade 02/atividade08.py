""" 
Escreva uma função chamada password_check(), que recebe como entrada duas strings chamadas newpassword e oldpassword. Essa função aceita a nova senha (e retorna True) se newpassword for diferente de oldpassword e newpassword tiver pelo menos 6 caracteres. Se a senha nova não satisfizer essas condições, a função deve retornar Falso.
"""

def password_check(newpassword, oldpassword):
    if newpassword != oldpassword and len(newpassword) > 6:
        return True
    return False


print(password_check('E10-s2ff', 'E10.s2ff'))
print(password_check('E10sf', 'E10.s2ff'))
print(password_check('E10-s2ff', 'E10-s2ff'))