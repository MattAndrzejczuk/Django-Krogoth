from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
import json
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import datetime

from rest_framework.permissions import IsAuthenticated, AllowAny

from DatabaseSandbox.models import VisitorLogSB, LazarusCommanderAccountSB, \
    LazarusModProjectSB, BasicUploadTrackerSB, TotalAnnihilationUploadedFile
from django.template import loader
import subprocess



# Create your views here.
class BasicUploadExample(APIView):
    # serializer_class = SuperBasicModelSerializer
    permission_classes = (AllowAny,)  # IsAuthenticated

    def get(self, request, format=None):
        allmodels = Car.objects.all()
        print(allmodels)
        return Response(allmodels)

    def post(self, request, *args, **kwargs):
        file_obj = request.FILES['file']
        # f = open('/usr/src/app/static/uploaded_file', 'w')
        # print('preparing to write file to /usr/src/app/static/uploaded_file')
        # myfile = File(f)
        # myfile.write(ContentFile(file_obj.read()))


        path = default_storage.save(request.user.username.strip() + '/' + str(file_obj), ContentFile(file_obj.read()))

        tmp_file = os.path.join(settings.MEDIA_ROOT, path)

        response = {'result': 'everything is finished ! ! ! ' + str(tmp_file)}

        file_name_regular = str(path).replace(request.user.username.strip()+'/','')
        but_DB = BasicUploadTrackerSB(file_name=file_name_regular,
                                      download_url='/media/'+path,
                                      system_path=str(tmp_file),
                                      author=request.user.username
                                      )
        but_DB.save()
        print('PROCESS COMPLETED!!!')
        return Response(response)



class UploadDataTA(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        template = loader.get_template('upload_iframe.html')
        server_msg = 'Lazarus will automatically parse the data to help make it avaliable to the Lazarus community.'
        alert = 'info'
        try:
            alert = request.GET['upload_result']
            if alert == "success":
                more_info = request.GET['msg']
                server_msg = 'Upload successful! ' + more_info
            elif alert == "danger":
                more_info = request.GET['msg']
                server_msg = 'Upload failed! ' + more_info
        except:
            print('first time visitor.')
        context = {
            "server_msg": server_msg,
            "alert": alert
        }
        return HttpResponse(template.render(context, request))


    def post(self, request, *args, **kwargs):
        import sys

        try:
            print('✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪')
            print(request.FILES.getlist('file'))
            print('✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪')


            for file_obj in request.FILES.getlist('file'):
                print(file_obj)

                parseName1 = str(file_obj).replace(' ', '_')
                parseName2 = parseName1.replace('-', '').lower()
                parseName3 = parseName2.replace('+', '__')
                # parseName4 = parseName3.replace('.', '')

                server_msg = ''

                path = default_storage.save('ta_data/' + parseName3, ContentFile(file_obj.read()))
                print('path: %s' % path)

                tmp_file = os.path.join(settings.MEDIA_ROOT, path)

                file_name_regular = str(path).replace('ta_data/', '').strip()

                response = {'result': 'everything is finished ! ! ! ' + str(tmp_file)}

                file_type_parsed = file_name_regular[-3:]

                extraction_point_directory = file_name_regular.replace(file_name_regular[-4:],'')
                os.system('mkdir '+ '/usr/src/persistent/media/ta_data/'+extraction_point_directory)

                ufo_path = '/usr/src/persistent/media/'+path
                output_path = '/usr/src/persistent/media/ta_data/'+extraction_point_directory


                bash_cmd = ['sh', 'extractTA_Mod.sh', ufo_path, output_path]
                run_extraction_bash = str(subprocess.check_output(bash_cmd))

                print(run_extraction_bash)

                rename_files_bash = "bash bashRenameStuffToLowerInDirectory_public.sh " + extraction_point_directory
                os.system(rename_files_bash)

                but_DB = TotalAnnihilationUploadedFile(file_name=file_name_regular,
                                            download_url=ufo_path,
                                            system_path=output_path,
                                            author=request.user.username,
                                            file_type=file_type_parsed,
                                            HPI_Extractor_Log=run_extraction_bash
                                            )
                try:
                    but_DB.uploader = request.user.username
                except:
                    print('failed to get uploader username')
                but_DB.save()
                server_msg = 'Upload successful! ' + str(file_obj)

            template = loader.get_template('upload_iframe.html')
            server_msg = 'Upload successful! ' + str(file_obj)
            alert = 'success'
            context = {
                "server_msg": server_msg,
                "alert": alert
            }
            return HttpResponse(template.render(context, request))

        except:
            template = loader.get_template('upload_iframe.html')
            server_msg = 'The upload seems to have failed: ' + str(sys.exc_info())
            alert = 'danger'
            context = {
                "server_msg": server_msg,
                "alert": alert
            }
            return HttpResponse(template.render(context, request))





class UserAgentTracker(APIView):
    def get(self, request, format=None):
        _1 = str(request.META['REMOTE_ADDR'])
        _2 = str(request.META['HTTP_USER_AGENT'])
        _3 = str(request.META['HTTP_ACCEPT_LANGUAGE'])
        _date = datetime.date
        newRecord = VisitorLogSB(remote_addr=_1, http_usr=_2, http_accept=_3)
        newRecord.save()

        html = '<div>' + \
               '<h1> User Visitor Tracking </h1>' + \
               '<h3> REMOTE_ADDR </h3>' + \
               '<p>' + str(_1) + '</p>' + \
               '<h3> HTTP_USER_AGENT </h3>' + \
               '<p>' + str(_2) + '</p>' + \
               '<h3> HTTP_ACCEPT_LANGUAGE </h3>' + \
               '<p>' + str(_3) + '</p>' + \
               '<h4> date </h4>' + \
               '<p>' + str(_date.today()) + '</p>' + \
               '<h5> username </h5>' + \
               '<p>' + str(request.user) + '</p>' + \
               '</div>'
        return HttpResponse(html)