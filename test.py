import argparse
import urllib2
import os
import re
import urllib
def grub(link,dest,dir):
    webm_filter = 'href="([^"]*(?:webm))'
    picture_filter = 'href="([^"]*(?:jpg|jpeg|png)'
    gif_filter = 'href="([^"]*(?:gif))'
    all_filter = 'href="([^"]*(?:jpg|gif|png|webm|jpeg)'
     
    URL = urllib2.urlopen(link)
    args=dest.parse_args()
    print(dir) 
    try:
        #Filtering args 
        if args.all_switch: 
            print('All download')
            filter = all_filter
        elif args.webm_switch:
            print('Only webm will downloaded')
            filter = webm_filter
        elif args.picture_switch:
            print('Only pictures will downloaded')
            filter = picture_filter
        elif args.gif_switch:
            print('Only gifs will downloaded')
            filter = gif_filter
        
        #Write board downloader 

        #create directory
        if not os.path.isdir(dir): 
            os.makedirs(dir)
        
        #Main download script
        for m in re.findall(webm_filter, URL.read().decode('utf-8')):
            print('Downloading '+ m)
            #urllib.urlretrieve('https://2ch.hk/' + m)

    except urllib2.HTTPError:
        print("Thread not found")
        exit()
   
  
if __name__ == '__main__':
    ar = argparse.ArgumentParser("python abuscript.py https://2ch.hk/b/res/123405664.html",epilog="Easy-to-Use download webm's, pictures or gifs \n Files will downloaded in dir with abuscript")
    ar.add_argument('--version',action='version', version='version 1.0')
    ar.add_argument('link', metavar='link',type=str,help="Thread link")
    ar.add_argument("-w","--webm",action="store_true",dest='webm_switch',default=False,help="Only webm's")
    ar.add_argument("-p","--picture",action="store_true",dest='picture_switch',default=False,help="Only pictures")
    ar.add_argument("-g","--gif",action="store_true",dest='gif_switch',default=False,help="Only gifs")
    ar.add_argument("-a",'--all',action="store_true", dest='all_switch',default=True,help="Download all files (Default)")
    ar.add_argument('-b','--board',action='store_true',dest='board_switch',default=False,help='Download all threads from board \n Example abuscript -b e')
    ar.add_argument('-t','--thread',action='store_true',dest='thread_switch',default=False,help='Download by number, only with -b (--board)')
    result = ar.parse_args()
    options = vars(result)
    link = options['link'] #parse link
    dir_name = re.split(r'[https://ch.hk/b/res/.html]+',link)
    dir_name =dir_name[1]
   #dir_name = link.strip('https://2ch.hk/b/res/.html')
    grub(link,ar,dir_name)