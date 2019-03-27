import argparse
import cmd
import shlex
from os import system
from subprocess import check_output
from core.utils import color
from core.utils import youtube

class Console(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = color.setcolor(':: ', color='Blue')

    def do_download(self, args):
        """ download video from youtube and convert to mp3 """
        arg_parser = argparse.ArgumentParser(prog="download", description='download audio from youtube')
        arg_parser.add_argument('-l', dest='url', metavar='<url>', help='youtube url (video or playlist)')
        arg_parser.add_argument('-i', dest='id', metavar='<id>', help='video id')
        try:
            args = arg_parser.parse_args(shlex.split(args))
        except: return

        if args.url:
            video = youtube.select_video_streaming(args.url)
            download_video(video, base_url)
        elif args.id:
            print("no")
        else:
            arg_parser.print_help()
        
    def do_upload(self, args):
        """ moves all downloaded audio files to dir """

    def do_help(self,args):
        """ show this help """
        names = self.get_names()
        cmds_doc = []
        names.sort()
        pname = ''
        color.display_messages('Available Commands:', info=True, sublime=True)
        for name in names:
            if name[:3] == 'do_':
                pname = name
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

    def do_clear(self,args):
        """ clean up the line """
        system('clear')

    def do_update(self,args):
        """ find newer versions """
        color.display_messages('checking updates...', info=True)
        color.display_messages(check_output(['git', 'pull']), info=True)

    def default(self, args):pass
    def emptyline(self):pass

    def do_exit(self, args):
        """ exit the program."""
        print('Quitting.')
        raise SystemExit