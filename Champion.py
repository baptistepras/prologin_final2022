from api import *


# Fonction appelée au début de la partie.
def partie_init():
    # TODO

    # Enregistre tous les nids
    global nids
    nids = []
    trous = []
    for i in range(HAUTEUR):
        for j in range(LARGEUR):
            if info_case((i, j, 0)).contenu == type_case.NID:
                nids.append((i, j, 0))
            elif info_case((i, j, 0)).contenu == type_case.TROU:
                trous.append((i, j, 0))



# Fonction appelée à chaque tour.
def jouer_tour():
    # TODO

    k = -1
    for i in troupes_joueur(moi()):
        k += 1
        if tour_actuel() > 10 and tour_actuel() % 2 == 0 and i.taille < 12:
            grandir(i.id)


        pain = []
        for m in pains():
            if m not in pain:
                pain.append(m)
        if i.inventaire < inventaire(i.taille) and pain != []:
            chemin = False
            for j in pain:
                if chemin is False and len(trouver_chemin(i.maman, j)) > 0:
                    chemin = trouver_chemin(i.maman, j)
                else:
                    chemin_temp = trouver_chemin(i.maman, j)
                    if 0 < len(chemin_temp) < len(chemin):
                        chemin = chemin_temp
            while type(chemin) == list and len(chemin) >= 1 and troupes_joueur(moi())[k].pts_action > 0:
                avancer(i.id, chemin[0])
                chemin = chemin[1:]
            if troupes_joueur(moi())[k].pts_action >= 3:
                grandir(i.id)
            if 3 > troupes_joueur(moi())[k].pts_action > 0:
                if nids != []:
                    nid = []
                    for j in nids:
                        nid_info = str(info_nid(j))
                        if str(moi()) in nid_info or info_nid(j) == etat_nid.LIBRE:
                            nid.append(j)
                    if nid != []:
                        chemin = trouver_chemin(i.maman, nid[0])
                        for j in nid[1:]:
                            chemin_temp = trouver_chemin(i.maman, j)
                            if 0 < len(chemin_temp) < len(chemin):
                                chemin = chemin_temp
                        while len(chemin) >= 1:
                            avancer(i.id, chemin[0])
                            chemin = chemin[1:]
                        if 3 > troupes_joueur(moi())[k].pts_action > 0:
                            pain = []
                            for m in pains():
                                if m not in pain:
                                    pain.append(m)
                            if i.inventaire < inventaire(i.taille) and pain != []:
                                chemin = False
                                for j in pain:
                                    if chemin is False and len(trouver_chemin(i.maman, j)) > 0:
                                        chemin = trouver_chemin(i.maman, j)
                                    else:
                                        chemin_temp = trouver_chemin(i.maman, j)
                                        if 0 < len(chemin_temp) < len(chemin):
                                            chemin = chemin_temp
                            while type(chemin) == list and len(chemin) >= 1:
                                    avancer(i.id, chemin[0])
                                    chemin = chemin[1:]

        else:
            if nids != []:
                nid = []
                for j in nids:
                    nid_info = str(info_nid(j))
                    if str(moi()) in nid_info or info_nid(j) == etat_nid.LIBRE:
                        nid.append(j)
                if nid != []:
                    chemin = trouver_chemin(i.maman, nid[0])
                    for j in nid[1:]:
                        chemin_temp = trouver_chemin(i.maman, j)
                        if 0 < len(chemin_temp) < len(chemin):
                            chemin = chemin_temp
                    while len(chemin) >= 1 and troupes_joueur(moi())[k].pts_action > 0:
                        avancer(i.id, chemin[0])
                        chemin = chemin[1:]
                    if troupes_joueur(moi())[k].pts_action >= 3:
                        grandir(i.id)
                    if 3 > troupes_joueur(moi())[k].pts_action > 0:
                        pain = []
                        for m in pains():
                            if m not in pain:
                                pain.append(m)
                        if i.inventaire < inventaire(i.taille) and pain != []:
                            chemin = False
                            for j in pain:
                                if chemin is False and len(trouver_chemin(i.maman, j)) > 0:
                                    chemin = trouver_chemin(i.maman, j)
                                else:
                                    chemin_temp = trouver_chemin(i.maman, j)
                                    if 0 < len(chemin_temp) < len(chemin):
                                        chemin = chemin_temp
                        while type(chemin) == list and len(chemin) >= 1:
                            avancer(i.id, chemin[0])
                            chemin = chemin[1:]
                        if 3 > troupes_joueur(moi())[k].pts_action > 0:
                            if nids != []:
                                nid = []
                                for j in nids:
                                    nid_info = str(info_nid(j))
                                    if str(moi()) in nid_info or info_nid(j) == etat_nid.LIBRE:
                                        nid.append(j)
                                if nid != []:
                                    chemin = trouver_chemin(i.maman, nid[0])
                                    for j in nid[1:]:
                                        chemin_temp = trouver_chemin(i.maman, j)
                                        if 0 < len(chemin_temp) < len(chemin):
                                            chemin = chemin_temp
                                    while len(chemin) >= 1:
                                        avancer(i.id, chemin[0])
                                        chemin = chemin[1:]



# Fonction appelée à la fin de la partie.
def partie_fin():
    # TODO
    pass