from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import URL
import re
import time
while True:
    try:
        base_url = 'http://127.0.0.1:5000/v2/first/api/'
        alert_url = 'http://127.0.0.1:5000/v2/twice/api/'
        niewiemcoto = '/<int:data>'


        baza = []  # tu będziemy zapisywać wszystkie URL ze wszystkich okrażeń (zapisywane co niej - których nie ma - zawsze)
        list1 = []  # pierwszy url, gdzie trzymamy pierwsze hrefy, jest nam to potrzebne do drugiego okrążenia
        list2 = []  # tutaj są zapisywane URL z 'for lista1', sprawdzane jest czy nie ma tych samych w list1
        list3 = []  #

        #  trzecie okrążenie: sprawdzanie URL z listy2, porównywanie ich z bazą, zapis nie figurujących w list1

        while True:
            a = 1
            for x in URL.strony:

                def api(a, b, c, d, e):

                    data = {'url': a, 'status_code': b, 'dataTime': c, 'error': d}
                    """
                    WZÓR NA PUT/PATCH
                    r = requests.put(url + "v1/first/api/1", {'url': 'cdsfs', 'status_code': '210', 'dataTime': '123223' ,'error': 'n123123ema'})
                    a = url
                    b = status_code
                    c = dataTime
                    d = error
                    """
                    if b == 200:
                        requests.patch(base_url + str(e), data=data)
                        requests.patch("http://212.32.248.106/v2/first/api/" + str(e), data=data)
                        return
                    else:
                        requests.put(alert_url + str(e), data=data)
                        requests.put('http://212.32.248.106/v2/twice/api/' + str(e), data=data)
                        return

                def pobierz_url_dla_zrodla(url_act, a):
                    try:
                        raz = requests.get(url_act)
                    except Exception as error:
                        api(url_act, raz.status_code, time.ctime(), error, a)
                    api(url_act, raz.status_code, time.ctime(), 'nie ma', a)
                    dwa = BeautifulSoup(raz.text, 'lxml')
                    trzy = dwa.html.find_all('a')
                    for data_2 in trzy:
                        absolute_link = urljoin(url_act, data_2.get('href'))

                        if str("\\") in absolute_link:
                            print(absolute_link)
                            print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
                            print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
                            print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
                            print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
                            print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
                            print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
                            aaaa = absolute_link.replace('\\', '')
                            print(aaaa)
                            print(aaaa)
                            print(aaaa)
                            print(aaaa)
                            print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
                            print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
                            print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
                            absolute_link = aaaa
                            print("Nowy aboslute_link to: " + absolute_link)

                        if url_act in str(absolute_link):
                            if str(absolute_link) in list1:
                                continue
                            else:
                                api(absolute_link, raz.status_code, time.ctime(), 'nie ma', a)
                                baza.append(absolute_link)
                                list1.append(absolute_link)
                                print("Dodane do listy " + absolute_link)

                        else:
                            print("wykluczono URL", absolute_link)
                        print("Loop number ", str(a))
                        a += 1
                    return a

                def pobierz_infinite(x, a): # to jest zrobione na literkę
                    for url in list1:
                        try:
                            raz = requests.get(url)
                        except Exception as ads:
                            api(url, raz.status_code, time.ctime(), ads, a)
                        api(url, raz.status_code, time.ctime(), 'nie ma', a)
                        dwa = BeautifulSoup(raz.text, 'lxml')
                        trzy = dwa.html.find_all('a')

                        for data_1 in trzy:
                            absolute_link = urljoin(url, data_1.get('href'))

                            if str("\\") in absolute_link:
                                print(absolute_link)
                                print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
                                print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
                                print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
                                print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
                                print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
                                print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
                                aaaa = absolute_link.replace('\\', '')
                                print(aaaa)
                                print(aaaa)
                                print(aaaa)
                                print(aaaa)
                                print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
                                print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
                                print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
                                absolute_link = aaaa
                                print("Nowy aboslute_link to: " + absolute_link)
                            # patrz poniżej
                            #if URL.literkaprzedszkole_url in str(absolute_link):
                            if x in str(absolute_link):
                                if str(absolute_link) in baza or str(absolute_link) in list1:
                                    continue
                                else:
                                    baza.append(absolute_link)
                                    list2.append(absolute_link)
                                    print("Dodane do listy " + absolute_link)
                            else:
                                print("wykluczono URL", absolute_link)
                            print("Loop number ", str(a))
                            a += 1
                    del list1[:]
                    for x in list2:
                        list1.append(x)
                    del list2[:]

                def pobierz_infinite_while(): # to jest na charaktery zrobione
                    while True:
                        for url in list1:
                            raz = requests.get(url)
                            dwa = BeautifulSoup(raz.text, 'lxml')
                            trzy = dwa.html.find_all('a')
                            a = 0
                            for data_1 in trzy:
                                absolute_link = urljoin(url, data_1.get('href'))
                                # patrz poniżej
                                if URL.charakteryplus_url in str(absolute_link):
                                    if str(absolute_link) in baza or str(absolute_link) in list1:
                                        continue
                                    else:
                                        baza.append(absolute_link)
                                        list2.append(absolute_link)
                                else:
                                    print("wykluczono URL", absolute_link)
                                print("Loop number ", str(a))
                                a += 1
                        if len(list2) < 1:
                            break
                        del list1[:]
                        for x in list2:
                            list1.append(x)
                        del list2[:]


                baza = []  # tu będziemy zapisywać wszystkie URL ze wszystkich okrażeń (zapisywane co niej - których nie ma - zawsze)
                list1 = []  # pierwszy url, gdzie trzymamy pierwsze hrefy, jest nam to potrzebne do drugiego okrążenia
                list2 = []  # tutaj są zapisywane URL z 'for lista1', sprawdzane jest czy nie ma tych samych w list1
                list3 = []
                try:
                    pobierz_url_dla_zrodla(x, a)
                except Exception as ero:
                    print(ero)
                pobierz_infinite(x, a)

            #name = re.compile(r'.+?.', x)
            # name = re.findall('^.+?.', x)
            # name = x[8:-3]
            # # print(x)
            # # print(name)
            # file = open(name, "w")
            #
            # c = 1
            # for xcv in baza:
            #     file.write(str(xcv) + "\n")
            #     print("|== ", c, " ==| ", xcv)
            #     c += 1
            #
            # file.close()


            # c = 1
            # for xcv in baza:
            #     print("|== ", c, " ==| ", xcv)
            #     c += 1



        # pobierz_infinite()
        # pobierz_infinite()
        # pobierz_infinite()

        # file = open("Charakteryplus.txt", "w")
        #
        # c = 1
        # for xcv in baza:
        #     file.write(str(xcv) + "\n")
        #     print("|== ", c, " ==| ", xcv)
        #     c += 1
        #
        # file.close()

        # if __name__ == '__main__':
        #
        #     # a = "https//charakteryplus.pl"
        #     a = URL.literkaprzedszkole_url
        #
        #     z = 0
        #     num = 0
        #     while z == len(URL.strony):
        #         url_act = URL.strony[num]
        #
        #         pobierz_url_dla_zrodla(url_act)
        #
        #         pobierz_infinite_while()
        #
        #         file = open("Charakteryplus.txt", "w")
        #
        #         c = 1
        #         for xcv in baza:
        #             file.write(str(xcv) + "\n")
        #             print("|== ", c, " ==| ", xcv)
        #             c += 1
        #         z += 1
        #         num += 1
        #         file.close()




        # def pobierz_url_dla_tablicy():
        #     for next_url in list1:
        #         raz = requests.get(next_url)
        #         dwa = BeautifulSoup(raz.text, 'lxml')
        #         trzy = dwa.html.find_all('a')
        #         for data_2 in trzy:
        #             absolute_link = urljoin(URL.literkaprzedszkole_url, data_2.get('href'))
        #             if URL.literkaprzedszkole_url in str(absolute_link):
        #                 if str(absolute_link) in _2_tablica:
        #                     continue
        #                 else:
        #                     _2_tablica.append(absolute_link)
        #             else:
        #                 print("wykluczono URL")
        #                 print(data_2)
        #             print("2")
        #
        #

        #
        # def perfect_list():
        #     # perfect, wywalamy jedne elementy z drugiej i dajemy do skanu raz jeszcze żeby nie skanować dodatkowo już przeszkanowanych uerlów
        #
        #     pass




        # pobierz_url_dla_zrodla()
        #
        # pobierz_url_dla_tablicy()
        #
        # for x in list_of_adrdes:
        #     print(x)
        #
        #
        # print("\n\n\n +++++++++++++++++++++ \n\n")
        #
        # for xc in _2_tablica:
        #     print(xc)
    except Exception as hhe:
        print(hhe)
