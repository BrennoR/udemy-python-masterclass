import os
import fnmatch
import id3reader_p3 as id3reader


def find_music(start, extension):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            absolute_path = os.path.abspath(path)   # create absolute path
            yield os.path.join(absolute_path, file)


my_music_files = find_music('music', 'emp3')

id3r_failed = []

for f in my_music_files:
    try:
        id3r = id3reader.Reader(f)
        print("Artist: {}, Album: {}, Track: {}, Song: {}".format(
            id3r.get_value('performer'),
            id3r.get_value('album'),
            id3r.get_value('track'),
            id3r.get_value('title')
        ))
    except:
        id3r_failed.append(f)

for j in id3r_failed:
    print(j)
