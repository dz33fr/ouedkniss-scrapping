# Abdelhafid BOUSLAHI
# wacim.bf@gmail.com
import os
file_cars= open("data_pretraitment.csv", "w", encoding="utf-8")
file_cars.write("Id,Papiers,Couleur,Boite,Energie,Moteur,Finition,Modèle,Marque,Kilométrage,Année,Prix\n")
data_brute= open("data_brute_2.txt" ,'r', encoding="utf-8")
infos = []
text = data_brute.read()
annonces = text.split('Automobiles\n')
annonces.pop(0)
i = 0
for annonce in annonces:
    annonce_list = annonce.splitlines()
    print(annonce_list)
    for ele in annonce_list:
        
        if ele == "Couleur":
            idx = annonce_list.index(ele)
            couleur = annonce_list[idx+1]
            print(f'idx : {idx}  Couleur : {couleur}')
        if ele == 'Energie':
            idx = annonce_list.index(ele)
            energie = annonce_list[idx+1]
            print(f'idx : {idx}  Energie : {energie}')
        if ele == 'Numéro':
            idx = annonce_list.index(ele)
            numero = annonce_list[idx+1]
            print(f'idx : {idx}  Numero : {numero}')
        if ele == 'Boite':
            idx = annonce_list.index(ele)
            boite = annonce_list[idx+1]
            print(f'idx : {idx}  Boite : {boite}')
        if ele == 'Moteur':
            idx = annonce_list.index(ele)
            moteur = annonce_list[idx+1]
            print(f'idx : {idx}  Moteur : {moteur}')
        if ele == 'Finition':
            idx = annonce_list.index(ele)
            finition = annonce_list[idx+1]
            print(f'idx : {idx}  Finition : {finition}')
        if ele == 'Modèle':
            idx = annonce_list.index(ele)
            modele = annonce_list[idx+1]
            print(f'idx : {idx}  Modèle : {modele}')
        if ele == 'Marque':
            idx = annonce_list.index(ele)
            marque = annonce_list[idx+1]
            print(f'idx : {idx}  Marque : {marque}')
        if ele == 'Kilométrage':
            idx = annonce_list.index(ele)
            kilometrage = annonce_list[idx+1]
            print(f'idx : {idx}  Kilométrage : {kilometrage}')
        if 'Millions' in ele:
            idx = annonce_list.index(ele)
            prix = annonce_list[idx]
            print(f'idx : {idx}  prix : {prix}')
        if ele == 'Année':
            idx = annonce_list.index(ele)
            annee = annonce_list[idx+1]
            print(f'idx : {idx}  Année : {annee}')
        if ele == 'Papiers':
            idx = annonce_list.index(ele)
            papiers = annonce_list[idx+1]
            print(f'idx : {idx}  Papiers : {papiers}')
    info=f'{numero},{papiers},{couleur},{boite},{energie},{moteur},{finition},{modele},{marque},{kilometrage},{annee},{prix}\n'
    infos.append(info)
    print("#"*50)
file_cars.writelines(infos)
file_cars.close()
