from model import eng, Directors
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=eng)
session = Session()

""" Kaip įrašyti duomenis į lentelę:
 (Crud) """

new_director = Directors(name='Frankas7', surname='Darabontas2', rating=9)
session.add(new_director)
session.commit()

""" Kaip gauti duomenis iš lentelės:
 (cRud) """
pirmas_direktorius = session.query(Directors).get(3)
print(pirmas_direktorius.name)
print("------------------------------")

pirmas_direktorius_tokiu_vardu = session.query(Directors).filter_by(name="Frank").one()
print(pirmas_direktorius_tokiu_vardu)
print("------------------------------")
visi_direktoriai = session.query(Directors).all()
for direktorius in visi_direktoriai:
    print(direktorius.name, direktorius.surname)
print("------------------------------")

# Kaip ieškoti duomenų pagal sąlygą ar šabloną:

search2 = session.query(Directors).filter(Directors.rating > 4)
search3 = session.query(Directors).filter(
    Directors.rating > 4,
    Directors.name.ilike("D%"))

print([i for i in search2])
print("------------------------------")
print([i for i in search3])

""" Kaip pakeisti duomenis lentelėje:
 (crUd) """
pirmas_direktorius_2 = session.query(Directors).get(1)
pirmas_direktorius_2.rating = 22
session.commit()

direktorius_neteisingu_vardu = session.query(Directors).filter_by(name="Eimantas").one()
print(direktorius_neteisingu_vardu)
direktorius_neteisingu_vardu.name = "Quentin"
session.commit()

""" Kaip ištrinti duomenis lentelėje: 
(cruD)
"""
atleidziamas_direktorius = session.query(Directors).filter_by(name="Christopher").one()

session.delete(atleidziamas_direktorius)
session.commit()
