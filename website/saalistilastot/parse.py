from django.shortcuts import redirect
from pyexcel_xls import get_data as xls_get
from pyexcel_xlsx import get_data as xlsx_get
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files import File
import xlrd
from models import Saalis
import urllib2

class ParseExcel(APIView)

    def post(self, request),format = None:

        try:

            excel_file = request.FILES['parse.xlsx']
            except MultiValueDictKeyError:
            return redirect(<your_upload_file_failed_url>)

            
        data = xls_get(excel_file, column_limit=4)
        elif (str(excel_file).split(‘.’)[-1] == “xlsx”):
        data = xlsx_get(excel_file, column_limit=4)
        else:
        return redirect(<your_upload_file_fail_url>)

        saaliit = data['Summary']

        if(len(saaliit) > 1):

            for saalis in saaliit:
                if (saalis[2] == 'lohi' | saalis[2] =='Lohi' | saalis[2] =='lohi CR')
                    excel_date = saalis[0]
                    python_date = datetime(*xlrd.xldate_as_tuple(excel_date, 0))

                    kuva = saalis[0]
                    
                    if kuva == "":
                        kuva = None
                    else:
                        kuva = urllib.urlretrieve(kuva.replace('href="',''))
                        



                    saalis[1]


                    # image to file

                    
                    sp = saalis[3]
                    if(sp == 'U'):
                    else if( sp == 'N'):
                    else:
                        sp = '-'
                    
                    paino = saalis[4]
                    if paino == "":  
                        paino = None
                    if pituus == "":
                        pituus = None
                    paikka = saalis[6]
                    #if paikka != "":
                    viehe = saalis[7]
                    #if viehe != "":
                    kalastaja = saalis[8]
                    #if kalastaja != "":

                    Saalis.object.create(
                        saaja = kalastaja,
                        paikka = paikka,
                        paino = paino,
                        pituus = pituus,
                        viehe = viehe,
                        email = None,
                        saantipaiva = python_date,
                        kuva = kuva,
                        public = True,
                        sukupuoli = sp
                    )

            return redirect('done')