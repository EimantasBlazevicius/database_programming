from model import eng, Directors
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=eng)
session = Session()
""" Kaip įrašyti duomenis į lentelę:
 (Crud) """

new_director = Directors({'name': 'Frank', 'surname': 'Darabont', 'rating': 7})
session.add(new_director)
session.commit()

""" Kaip gauti duomenis iš lentelės:
 (cRud) """
pirmas_direktorius = session.query(Directors).get(1)
print(pirmas_direktorius.name)

pirmas_direktorius_tokiu_vardu = session.query(Directors).filter_by(name="Frank").one()
visi_direktoriai = session.query(Directors).all()

for direktorius in visi_direktoriai:
    print(direktorius.name, direktorius.surname)

# Kaip ieškoti duomenų pagal sąlygą ar šabloną:

search2 = session.query(Directors).filter(Directors.price > 1000)
search3 = session.query(Directors).filter(
    Directors.price > 1000,
    Directors.name.ilike("2%"))

print([i for i in search2])
print([i for i in search3])

""" Kaip pakeisti duomenis lentelėje:
 (crUd) """
pirmas_direktorius_2 = session.query(Directors).get(1)
pirmas_direktorius_2.rating = 22000
session.commit()
direktorius_neteisingu_vardu = session.query(Directors).filter_by(name="Frank").one()
direktorius_neteisingu_vardu.name = "Eimantas"
session.commit()

""" Kaip ištrinti duomenis lentelėje: 
(cruD)
"""
atleidziamas_direktorius = session.query(Directors).filter_by(name="Eimantas").one()

session.delete(atleidziamas_direktorius)
session.commit()
