import argparse
import cmd
import shlex
import os
from os import system
from subprocess import check_output
from src.core.utils import color, youtube, settings, android

class Console(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.use_rawinput = False
        cmd.Cmd.__init__(self)
        self.config = settings.Config()
        self.prompt = color.setcolor(':: ', color='Blue')


    def do_download(self, args):
        """ download video from youtube and convert to mp3 """
        arg_parser = argparse.ArgumentParser(prog="download", description='download audio from youtube')
        arg_parser.add_argument('url', type=str, metavar='[url]', help='youtube url (video or playlist)')
        arg_parser.add_argument('-pl', '--playlist', type=bool, dest='playlist', metavar='<playlist>', help='download the whole playlist or not')
        try:
            args = arg_parser.parse_args(shlex.split(args))
        except: return

        if not self.config.require_one('path'):
            return

        if not args.url:
            arg_parser.print_help()
        elif args.playlist:
            try:
                videos = youtube.get_playlist_videos(args.url)
            except IndexError:
                color.display_messages('url is not a playlist', error=True)
                return
                
            for video_url in videos:
                youtube.download_audio(video_url, self.config['path'])
        else:
            youtube.download_audio(args.url, self.config['path'])
            

    def do_upload(self, args):
        """ moves all downloaded audio files to dir """
        if not self.config.require(['path', 'dest']):
            return

        files = os.listdir(self.config['path'])
        for filename in files:
            android.upload_audio(filename, self.config['path'], self.config['dest'])
            os.remove(os.path.join(self.config['path'], filename))


    def do_config(self, args):
        """ edit application's user preferences """
        arg_parser = argparse.ArgumentParser(prog="config", description='config application settings (only one parameter per config call)')
        arg_parser.add_argument('-p', dest='path', metavar='<path>', help='sets download path (folder to download in)')
        arg_parser.add_argument('-d', dest='dest', metavar='<dest>', help='sets destination folder (android filesystem)')
        try:
            args = arg_parser.parse_args(shlex.split(args))
        except: return

        # add main section in case it hasn't been created yet
        if 'main' not in self.config.sections():
            self.config.add_section('main')

        if args.path: 
            self.config.set('main', 'path', args.path)
            self.config.dump()
        elif args.dest:
            self.config.set('main', 'dest', args.dest)
            self.config.dump()
        else:
            arg_parser.print_help()


    def do_help(self, args):
        """ show this help """
        names = self.get_names()
        cmds_doc = []
        names.sort()
        color.display_messages('Available Commands:', info=True, sublime=True)
        for name in names:
            if name[:3] == 'do_':
                cmd   = name[3:]
                if getattr(self, name).__doc__:
                    cmds_doc.append((cmd, getattr(self, name).__doc__))
                else:
                    cmds_doc.append((cmd, ""))

        #self.stdout.write('%s\n'%str(self.doc_header))
        self.stdout.write('    {}	 {}\n'.format('Commands', 'Description'))
        self.stdout.write('    {}	 {}\n'.format('--------', '-----------'))
        for command,doc in cmds_doc:
            self.stdout.write('    {:<10}	{}\n'.format(command, doc))
        color.linefeed()


    def do_clear(self, args):
        """ clean up the line """
        system('clear')


    def do_update(self, args):
        """ find newer versions """
        color.display_messages('checking updates...', info=True)
        color.display_messages(check_output(['git', 'pull']), info=True)


    def default(self, args):pass
    def emptyline(self):pass


    def do_exit(self, args):
        """ exit the program."""
        print('Quitting.')
        raise SystemExit
