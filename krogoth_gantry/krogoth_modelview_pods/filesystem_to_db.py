import codecs
from datetime import datetime
import os

from .kg_publicstatic_text import KPubStaticInterfaceText, KPublicStaticInterfaceText_UncommittedSQL


class KSI_Processor(object):

    @classmethod
    def run_task_saveall_filesystem_to_sql(cls) -> {str: str}:
        paths_in_root = os.listdir(os.path.join('static', 'web', 'krogoth_static_interface'))
        list_of_work = []
        for listed_item in paths_in_root:
            if os.path.isdir(os.path.join('static', 'web', 'krogoth_static_interface', listed_item)):
                static_files = os.listdir(os.path.join('static', 'web', 'krogoth_static_interface', listed_item))

                for file_name in static_files:
                    print(os.path.join('static', 'web', 'krogoth_static_interface', listed_item, file_name))
                    document_sql: KPubStaticInterfaceText
                    try:
                        document_sql = KPubStaticInterfaceText.objects.get(file_name=file_name)
                    except:
                        split_file = file_name.split('.')
                        doc_ext = str(split_file[len(split_file) - 1]).upper()
                        path_to_file = os.path.join('static', 'web', 'krogoth_static_interface', doc_ext, file_name)
                        f = codecs.open(path_to_file, 'r').read()
                        new = KPubStaticInterfaceText(
                            unique_id=file_name.replace("." + doc_ext, ""),
                            file_name=file_name,
                            file_kind=str(doc_ext).upper(),
                            content=f,
                            pub_date=datetime.now()
                        )
                        new.save()

                        completed_work: {str: str} = {
                            "new.unique_id": new.unique_id,
                            "new.file_kind": new.file_kind,
                            "path_to_file": path_to_file,
                            'result': 'ADDED TO SQL FROM FILESYSTEM',
                        }
                        list_of_work.append(completed_work)
                        continue
                    name_path: str = file_name
                    path_to_doc = os.path.join('static', 'web', 'krogoth_static_interface', document_sql.file_kind,
                                               name_path)
                    unsaved_work = KPublicStaticInterfaceText_UncommittedSQL.objects.filter(document=document_sql)
                    if len(unsaved_work) > 1:
                        return {
                            "error": "YOU HAVE UNSAVED WORK ON SQL FOR " + file_name,
                            "completed_work": "failed"
                        }
                    else:
                        document_sql.content = codecs.open(path_to_doc, 'r').read()
                        document_sql.save()
                        completed_work: {str: str} = {
                            "document_sql.unique_id": document_sql.unique_id,
                            "document_sql.file_kind": document_sql.file_kind,
                            "path_to_doc": path_to_doc,
                            'result': 'Database copy saved into filesystem.'
                        }
                        list_of_work.append(completed_work)
        return {"completed_work": list_of_work}