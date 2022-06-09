from os import listdir, remove, makedirs
from os.path import isfile, join, exists
from pydoc import doc
from shutil import move
import sys

path = sys.argv[1]
#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

dirs = ['Downloaded_images', 'Downloaded_compressed', 'Downloaded_text',
        'Downloaded_pdfs', 'Downloaded_torrents', 'Downloaded_data', 'Downloaded_videos']

for dir in dirs:
    if not exists(join(path, dir)):
        makedirs(join(path, dir))
        print('Created: ', join(dir))


for f in listdir(path):
    if isfile(join(path, f)):
        splited = f.split('.')
        extension = splited[len(splited)-1]
        match extension:
            case 'exe' | 'png' | 'crdownload' | 'log' | 'msi' | 'parts' | 'apk' | 'jar' | 'iso' | 'MSI':
                remove(join(path, f))
                print('Removed file: ' + f)
            case 'png' | 'jpg' | 'svg' | 'webp' | 'jpeg' | 'jfif' | 'pjpeg' | 'gif' | 'bmp' | 'ico' | 'tiff' | 'tif' | 'PNG':
                move(join(path, f), join(path, 'Downloaded_images', f))
                print('moved ' + f + ' to Downloaded_images')
            case 'zip' | '7z' | 'rar' | 'tar.gz':
                move(join(path, f), join(path, 'Downloaded_compressed', f))
                print('moved ' + f + ' to Downloaded_compressed')
            case 'docx' | 'doc' | 'odt' | 'txt' | 'xml' | 'csv' | 'xlsx' | 'ppt' | 'ppsx' | 'pptx' | 'ods':
                move(join(path, f), join(path, 'Downloaded_text', f))
                print('moved ' + f + ' to Downloaded_text')
            case 'pdf' | 'epubs' | 'mobi' | 'epub':
                move(join(path, f), join(path, 'Downloaded_pdfs', f))
                print('moved ' + f + ' to Downloaded_pdfs')
            case 'torrent':
                move(join(path, f), join(path, 'Downloaded_torrents', f))
                print('moved ' + f + ' to Downloaded_torrent')
            case 'json' | 'js' | 'cpp' | 'gpx' | 'bat' | 'ged' | 'py' | 'h' | 'sql':
                move(join(path, f), join(path, 'Downloaded_data', f))
                print('moved ' + f + ' to Downloaded_data')
            case 'webm':
                move(join(path, f), join(path, 'Downloaded_videos', f))
                print('moved ' + f + ' to Downloaded_videos')
