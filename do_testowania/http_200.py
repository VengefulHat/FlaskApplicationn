import requests
import time

base_url = 'http://127.0.0.1:5000/v1/first/api/'
alert_url = 'http://127.0.0.1:5000/v1/twice/api/'
niewiemcoto = '/<int:data>'

def infiniteDef():

    try:
        strony_do_klepania = ['https://praktycznafizjoterapia.pl', 'https://akademiastomatologa.pl/',
                              'https://charaktery.eu', 'https://forumginekologii.pl',
                              'https://psychologiawpraktyce.pl', 'https://food-forum.pl', 'https://monitorszkoly.pl',
                              'https://mieszkanie-i-wspolnota.pl', 'https://forumlogopedy.pl',
                              'https://glospedagogiczny.pl',
                              'https://animal-expert.pl', 'https://wychowaniewprzedszkolu.com.pl',
                              'https://praktycznastomatologia.pl',
                              'https://praktyczna-ortopedia.pl', 'https://bikeboard.pl',
                              'https://naturoterapiawpraktyce.pl', 'https://forumpediatrii.pl',
                              'https://monitorprzedszkola.pl', 'https://doradcawpomocyspolecznej.pl',
                              'https://naturoterapiawpraktyce.pl', 'https://forumpediatrii.pl',
                              'https://monitorprzedszkola.pl', 'https://doradcawpomocyspolecznej.pl',
                              'https://body-challenge.pl', 'https://monitor-zamowien.pl',
                              'https://zycieszkoly.com.pl', 'https://wychowaniefiz.pl', 'https://terapiaspecjalna.pl',
                              'https://wiadomoscidermatologiczne.pl', 'https://ksiegowego.pl',
                              'https://o-m.pl', 'https://hrbusinesspartner.pl', 'https://menedzer-produkcji.pl',
                              'https://doradcazarzadcy.pl', 'https://nowa-sprzedaz.pl',
                              'https://czasopismobiologia.pl', 'https://sm-manager.pl', 'https://realestatemagazine.pl',
                              'https://sluzby-ur.pl', 'https://czasopismopolonistyka.pl',
                              'https://malecharaktery.pl', 'https://magazyn-ecommerce.pl', 'https://mamy-czas.pl',
                              'https://magazynswiatseniora.pl', 'https://czasopismomatematyka.pl',
                              'https://kongres-forumpediatrii.pl', 'https://horyzontyanglistyki.pl',
                              'https://ksiegowego.pl', 'https://vettrends.pl', 'https://laj.pl',
                              'https://animalexpertplus.pl',
                              'https://kongres-dietoterapia.pl', 'https://kadry-i-place.com.pl',
                              'https://kongresbehawiorystyczny.pl', 'https://pastoralis.pl',
                              'https://czasopismokatecheza.pl',
                              'https://opieka-farmaceutyczna.eu', 'https://kongres-zaburzeniasi.pl',
                              'https://pr-manager.pl', 'https://kongres-arteterapia.pl', 'https://mojprzedszkolak.pl',
                              'https://pastoralis.pl', 'https://pediatriaplus.pl', 'https://forumpomocyspolecznej.pl',
                              'https://mspmag.pl', 'https://konferencja-reumatologiczna.pl',
                              'https://bikeboard.pl', 'https://miesiecznikfpn.pl', 'https://teczkaterapii.pl',
                              'https://biznes-hotel.pl', 'https://sur-bootcamp.pl', 'https://czasopismomindfulness.pl',
                              'https://barber-magazine.pl', 'https://teczkapsychologa.pl',
                              'https://regulacjebudowlane.pl', 'https://remmeeting.pl', 'https://doradcaksiegowego.pl',
                              'https://dochodowy.com.pl', 'https://mindfully.pl', 'https://magazynroweryelektryczne.pl',
                              'https://uczen-niepelnosprawny.pl',
                              'https://psychopatologiadlapsychologow.pl', 'https://forum-budownictwa.pl',
                              'https://tcmwpraktyce.pl', 'https://przewodnikporodo.pl',
                              'https://konferencja-neurologiczna.pl', 'https://kongresnaturoterapii.pl',
                              'https://kongresanglistow.pl', 'https://hrbusinessguide.pl',
                              'https://kadry-i-place.com.pl', 'https://terapiaprzedszkolaka.pl',
                              'https://teczkapedagoga.pl', 'https://kongrespolonistyczny.pl',
                              'https://kongrespolonistyczny.pl', 'https://kurs-logo.pl', 'https://kongresbhp.pl',
                              'https://trendywneurologii.pl', 'https://emocjewprzedszkolu.pl',
                              'https://zajeciawyrownawcze.pl', 'https://teczkanaturoterapii.pl',
                              'https://konferencjanowoczesnegohr.pl', 'https://kierownik-budowlany.pl',
                              'https://konferencja-logopedyczna.pl', 'https://www.nadzor-pedagogiczny.pl/',
                              'https://kongres-wf.pl', 'https://konferencjaneurodydaktyczna.pl',
                              'https://fizjoterapianajmlodszych.pl',
                              'https://doradztwowszkole.pl', 'https://kongreszarzadcy.pl',
                              'https://ekspertzamowienpublicznych.pl',
                              'https://kongresgeograficzny.pl', 'https://diagnostykaplodu.pl',
                              'https://ksiazka-obiektu.pl', 'https://fizjoterapiazwierzat.com.pl',
                              'https://kongresniepubliczne.pl',
                              'https://kongres-matematykow.pl', 'https://konferencja-cukrzyca.pl',
                              'https://kongresfizchem.pl', 'https://ocenazgodnoscimaszyn.pl', 'https://kurs-fizjo.pl',
                              'https://obrazowaniewortopedii.pl', 'https://hrimpactconference.pl',
                              'https://szefowie-produkcji.pl', 'https://konferencja-skoradziecka.pl',
                              'https://konferencja-onkologiczna.pl', 'https://strategie-ur.pl',
                              'https://dietywpediatrii.pl', 'https://kongresterapeutow.pl',
                              'https://fizjoterapia-sport.pl',
                              'https://fizjoterapia-covid.pl', 'https://pedodoncja-stepbystep.pl',
                              'https://kodowaniewprzedszkolu.pl', 'https://konferencja-dietetyczna.pl',
                              'https://procedurysanitarne.pl', 'https://kongres-edukacjawczesnoszkolna.pl',
                              'https://konferencja-stomatologiczna.pl', 'https://konferencja-ux.pl',
                              'https://atrakcyjnezajecia.pl', 'https://konferencja-zp.pl',
                              'https://kongresoswiatowy.pl', 'https://nowoczesnybibliotekarz.pl', 'https://pzp2021.pl',
                              'https://endodoncja-kurs.pl', 'https://kongresprofesjonalistowhr.pl',
                              'https://warsztaty-fizchem.pl', 'https://kongresbiologiczny.pl',
                              'https://aboutid.xyz', 'https://best1be.xyz', 'https://whereyougofor.xyz',
                              'https://konferencjabibliotekarzy.pl',
                              'https://flippingbook.ocenazgodnoscimaszyn.pl', 'https://teczkabhp.pl',
                              'https://flippingbook.ocenazgodnoscimaszyn.pl', 'https://customerservicemagazine.pl',
                              'https://kongresmindfulness.pl', 'https://charakteryplus.pl',
                              'https://konferencjazlobki.pl', 'https://ux-academy.pl',
                              'https://kongresliderekbiznesu.pl',
                              'https://flippingbook.zycieszkoly.com.pl', 'https://flippingbook.forumlogopedy.pl',
                              'https://cukrzyca-konferencja.pl', 'https://spotkaniaznaturoterapia.pl',
                              'https://teczkazarzadcy.pl', 'https://flippingbook.monitorprzedszkola.pl',
                              'https://kongresochronysrodowiska.pl', 'https://flippingbook.czasopismomatematyka.pl',
                              'https://receptury-roslinne.pl', 'https://prenumerata.eventmanagement.pl',
                              'https://cc.bingj.com', 'https://fotowoltaika-zrodla-energii-webinar.pl',
                              'https://cc.bingj.com',
                              'https://fotowoltaika-zrodla-energii-webinar.pl',
                              'https://flippingbook.praktycznastomatologia.pl', 'https://zdrowe-swieta.pl',
                              'https://flippingbook.kierownik-budowlany.pl',
                              'https://www-1animal-2expert-1pl-100117ful08dd.han.up.poznan.pl',
                              'https://www-1animal-2expert-1pl-100117ful08dd.han.up.poznan.pl',
                              'https://www-1animal-2expert-1pl-100117ful08dd.han.up.poznan.pl',
                              'https://flippingbook.procedurysanitarne.pl', 'https://ekurs.sigma.org.pl',
                              'https://flippingbook.terapiaprzedszkolaka.pl',
                              'https://flippingbook.emocjewprzedszkolu.pl',
                              'https://flippingbook.atlasrehabilitacji.pl',
                              'https://flippingbook.regulacjebudowlane.pl',
                              'https://flippingbook.wychowaniefiz.pl', 'https://flippingbook.wychowaniefiz.pl',
                              'https://flippingbook.atrakcyjnezajecia.pl', 'https://flippingbook.doradztwowszkole.pl',
                              'https://www.literkaprzedszkole.pl', 'https://www.charakteryplus.pl/',
                              'https://www.net-fiz.pl/',
                              'https://www.pediatriaplus.pl/', 'https://www.animalexpertplus.pl/',
                              'https://www.doradcaksiegowego.pl/', 'https://www.uniqskills.com/', 'https://www.mieszkanie-i-wspolnota.pl/']


        """
        WZÓR NA PUT/PATCH
        r = requests.put(url + "v1/first/api/1", {'url': 'cdsfs', 'status_code': '210', 'dataTime': '123223' ,'error': 'n123123ema'})
        """

        def status_check(status, strona, i, aa):
            if status == 200:
                data = {'url': str(strona), 'status_code': str(status), 'dataTime': str(time.ctime()), 'error': 'Nie ma'}
                requests.patch(base_url + str(i), timeout=10, data=data)
                requests.patch("http://212.32.248.106/v1/first/api/" + str(i), timeout=10, data=data)
                print("Jest dobrze z " + str(strona))
                return
            else:
                print(time.ctime())
                print("===================================================================")
                print("===================================================================")
                print("===================================================================")
                print("===================================================================")
                print("My tu tego nie znamy: " + str(status) + " dla strony " + str(strona))
                print("===================================================================")
                print("===================================================================")
                print("===================================================================")
                print("===================================================================")
                data = {'url': str(strona), 'status_code': str(status), 'dataTime': str(time.ctime()), 'error': 'Jest zonk'}
                requests.put(alert_url + str(aa), timeout=10, data=data)
                requests.put("http://212.32.248.106/v1/twice/api/" + str(aa), timeout=10, data=data)
                # http://127.0.0.1:5000/v1/twice/api/'
                aa += 1
                return

        if __name__ == '__main__':
            global aa
            print("Zaczynamy działanie programu")
            print("Wchodzimy w program pętli...")
            global i
            i = 1
            while True:
                print("Działamy w pętli")
                for strona in strony_do_klepania:
                    print("Strona jest sprawdzana, jest to strona numer: " + str(i))
                    print(time.ctime())
                    print(strona)
                    try:
                        r = requests.get(strona)
                        status_check(r.status_code, strona, i, aa)
                    except Exception as z:
                        aa = 1
                        data = {'url': str(strona), 'status_code': 'błąd', 'dataTime': str(time.ctime()),
                                'error': z}
                        requests.put(alert_url + str(aa), timeout=10, data=data)
                        requests.put("http://212.32.248.106/v1/twice/api/" + str(aa), timeout=10, data=data)
                        print(z)
                        aa += 1
                    i += 1
                print("\nowa kolejka ++++++++++++++++++++++===++==+===+=======\n")
                i = 1


    except Exception as e:
        print(e)
        infiniteDef()

infiniteDef()



# z = '/v1/first/api/<int:data>'
#
# dane = [{1: {'asd': 'assss', 'maka': 'koko'}, 3: {'eee': 'trdd'}, 4: {'eee': 'trdd'}, 5: {'eee': 'trdd'}, 6: {'eee': 'trdd'}}]
# print(dane)
# # print(dane[1])
#
# for item in dane:
#     print(item)