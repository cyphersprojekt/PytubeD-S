import sys, argparse, os
import cv2 as cv
from pytube import YouTube


def download():
    url = input('Youtube URL: ')
    yt = YouTube(url)

    print(f'Title: {yt.title}')
    print(f'Views: {yt.views}')
    print(f'Length: {yt.length}')
    print(f'Description: {yt.description}')
    print('-'*40)
    
    for i, stream in enumerate(yt.streams.filter(file_extension='mp4')):
        try:
            print(f'Stream #{i}: itag: {stream.itag} {"-"*20}> {stream.mime_type}, {stream.fps}, {stream.bitrate}, {stream._filesize}, {stream.resolution}, {stream.codecs}')
        except AttributeError:
            print(f'Stream #{i}: itag {stream.itag} {"-"*20}> {stream.mime_type}, {stream.codecs}')

    dw = int(input('Itag to download: '))
    filename = os.listdir(os.path.curdir+'Downloads').__len__()    
    yt.streams.get_by_itag(dw).download(str(os.path.curdir+'Downloads'), f'{filename}.mp4')
    print(f'{os.path.curdir}/.Downloads/{filename}.mp4')
    return f'{os.path.curdir}/.Downloads/{filename}.mp4'

def extractImages():
    vidcap = cv.VideoCapture(download())
    success,image = vidcap.read()
    count = 0
    while success:
        cv.imwrite(".Frames/frame%d.jpg" % count, image)     # save frame as JPEG file      
        #cv.imwrite(".Frames/"+str(os.listdir(os.path.curdir+'Frames').__len__())+"/frame%d.jpg"% count, image)
        success,image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1

def main():
    extractImages()
    return

if __name__ == '__main__':
    main()