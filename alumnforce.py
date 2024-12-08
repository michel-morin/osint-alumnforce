#!/usr/bin/env python

## Looking for people across websites that are using Alumnforce SaaS solution (a directory solution for organizations)

## Parameters to fill below hardcoded before the launch of that script:

# firstname: string
## in case of compound first name, use the following character: -

# lastname: string
## in case of compound last name, use the following character: -

# To execute: $ python3 alumnforce.py >> output.txt

## Please use the bash command grep with the following parameters in your result output:
# "Graduated from"
# "Pending validation of"
# "Diplômé(e) de"
# "En attente de validation"

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (ecko/20100101 Firefox/133.0',
    'Accept': '*/*',
    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
    'X-Accept-Timezone': 'Europe/Paris',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'DNT': '1',
    'Connection': 'keep-alive',
}

data = {
    'firstname': 'john', # not case sensitive
    'lastname': 'doe', # not case sensitive
}

urls = [
'https://alumni.ism-iae.uvsq.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.paris-valdeseine.archi.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.esfam.auf.org/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.ecole-ipssi.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.monalumni.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.em-strasbourg.eu/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.engie.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://ouitalents-sncf.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.bdo.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.esccialumni.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni-ism.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.groupe-adecco.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://reseau-institut.compagnonsdutourdefrance.org/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.isosteo.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://community.ecv.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://reseau.lisaa.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://reseau.ecole-multimedia.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.emic-paris.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://network.ensai.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni-iaemetz.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://hub.ynov.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni-iae.unilim.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.univ-fcomte.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.serviralumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.inextenso.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://bsb-alumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.groupe-gema.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://btpreseau33.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.u-bordeaux-montaigne.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://42alumni.org/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://aakb.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://aen3s.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://ain7.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://airbus-flight-academy-alumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni-docteurs.univ-toulouse.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.ecole-de-savignac.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.edhec.edu/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni-ehess.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.ens-lyon.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.ephe.psl.eu/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.esaip.org/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni-esdes.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.grenoble-em.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.groupe-adecco.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.ifgexecutive.inseec.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.inalco.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni-itech.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.monaco.edu/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.pasteur.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.polyvia-formation.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.pwc.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni-sciencespoaix.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.sciencespo-lille.eu/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni-supdeluxe.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni-supdesrh.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.tse-fr.eu/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.unistra.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.univ-amu.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.univ-gustave-eiffel.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.univ-paris13.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.univ-pau.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.univ-reunion.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://alumni.uvsq.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://ambassadrices.becomtech.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://association.centralesupelec-alumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://ax.polytechnique.org/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://campuslangues-alumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://evrytalents.univ-evry.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://connect.ehl.edu/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://enass-alumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://escealumni.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://esgnetwork.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://esix.alumni.unicaen.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://exalumnos.colegioarturosoria.org/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://floraison.ch/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://hbsclubfrance.org/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://iaecaenalumni.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://iaetoursalumni.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://ich-cnam-alumni.org/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://ifm-alumni.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://ingeconnect.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://ipag-alumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://ipoline.univ-angers.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://iscg-alumni.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://iscparis-alumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://istomalumni.org/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://membres.cercle-suisse-administratrices.ch/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://network.ieqt.org/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://network.nyfa.edu/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://nextgen.espub.org/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://phdalumni-uga.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://pigier-alumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://reseau.la-joliverie.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://reseau-mpi.sorbonne-nouvelle.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://reseau.sciencespobordeaux.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://reseau.union-ihedn.org/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://rethinkandlead.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://rpro.univ-tours.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://sciencespo-alumni.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://upto-numerique.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://wedesign.lecolededesign.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://wilders.co/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.aaeea.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.adae-oniris.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.adi-inseec.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.aea.asso.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.aiesme.org/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.alumniae-montpellier.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.alumnicn.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.alumni.elte.hu/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.alumni.grenoble-inp.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.alumni-ifpass.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.alumni-plm.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.alumni-psbedu.paris/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.alumni-sciencespolyon.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.alumnisteli.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.alumni.utc.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.ampac.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.amsalumni.org/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.anciensdestan.org/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.astonjob.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.atuge.org/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.axion.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.campus-afd-alumni.org/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.cefam-alumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.centrale-carrieres.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.centraliens-lille.org/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.centraliens-mediterranee.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.centraliens-nantes.org/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.chartreuxalumni.net/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.ciffop-alumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.clubvie.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.com-ent.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.devincialumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.ens-alumni.org/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.eppalumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.esc-amiens-alumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.esc-clermont-alumni.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.eseo-alumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.esmod-alumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.espi-alumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.essecalumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.femmes-immobilier.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.ferrandialumni.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.grenoble-iae-community.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.gsefr.org/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.happychandara-alumni.org/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.hecalumni.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.iaenantes-alumni.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.idrac-network.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.ifag-alumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.ihest-connect.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.ileri-alumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.iml-alumni.org/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.ipi-alumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.isolink.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.latoilesepr.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.lesingenieurs.net/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.letreflegend.org/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.makeupforeveracademytribe.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.mbway-alumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.mygcr.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.neoma-alumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.reseaudesjournalistesducelsa.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.reseauesjlille.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.reseau-euridis.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.reseau-istec.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.reseau-lycee-cfa-hotelier-marseille.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.reseau-pro-nextgroup.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.resopro-hotellerietourisme.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.saint-cyr.org/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.stratealumni.org/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.supdecom-network.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.supoptique-alumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.tsm-connect.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.utt-alumni.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.wats4u.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.yschools-alumni.fr/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.iscpa-alumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.igs-rh-alumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.imsi-alumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.igs-rh-alumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://www.icd-alumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://atout-dsi.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://esam-alumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
'https://absparis-alumni.com/taglib/sectionupdate/update?updatelist=content:action://addressbook/public-search/search',
]

i = 0
y = 0
for url in urls:
    try:
        print("//////////////////////// log: begin URL request /////")
        i+=1
        print(i)
        print(url)
        response = requests.post(
            url,
            headers=headers,
            data=data,
        )
        json = response.json()
        print(json['content'])
        y+=1
        print(y)
        print(url)
        print("//////////////////////// log: next URL request /////")
    except:
        continue