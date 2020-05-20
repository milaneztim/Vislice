import model


def izpis_igre(igra):
    tekst = (
        '====================================================\n\n'
        "Stevilo preostalih poskusov: {stevilo_preostalih_poskusov} \n\n"
        "       {pravilni_del_gesla}\n\n"
        "Neuspeli poskusi: {neuspeli_poskusi}\n\n"
        '====================================================\n\n'
    ).format(
        stevilo_preostalih_poskusov=model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak(),
        pravilni_del_gesla=igra.pravilni_del_gesla(),
        neuspeli_poskusi=igra.nepravilni_ugibi()
    )
    return tekst


def izpis_zmage(igra):
    tekst = (
        "Zmagali ste! Geslo je bilo: {geslo} \n\n"
    ).format(
        geslo=igra.geslo
    )
    return tekst
    

def izpis_poraza(igra):
    tekst = (
        "Poraz! Geslo je bilo: {geslo}\n\n"
    ).format(
        geslo=igra.geslo
    )
    return tekst

def izpis_napake():
    return '\nUgiba se tocno ena crka naenkrat\n'

def izpis_napake_znak():
    return '\nUgib naj ne vsebuje posebnih znakov\n'


def zahtevaj_vnos():
    return input('Crka: ')


def pozeni_vmesnik():
    
    igra = model.nova_igra()

    while True:
        print(izpis_igre(igra))
        poskus = zahtevaj_vnos()
        rezultat_ugiba = igra.ugibaj(poskus)
        if rezultat_ugiba == model.VEC_KOT_CRKA:
            print(izpis_napake())
        elif rezultat_ugiba == model.POSEBEN_ZNAK:
            print(izpis_napake_znak())
        elif rezultat_ugiba == model.ZMAGA:
            print(izpis_zmage(igra))
            ponovni_zagon = input('Za ponovni zagon vpisite 1\n').strip()
            if ponovni_zagon == '1':
                igra = model.nova_igra()
            else:
                break
        elif rezultat_ugiba == model.PORAZ:
            print(izpis_poraza(igra))
            ponovni_zagon = input('Za ponovni zagon vpisite 1\n').strip()
            if ponovni_zagon == '1':
                igra = model.nova_igra()
            else:
                break
    return

#Zazeni igro#
pozeni_vmesnik()