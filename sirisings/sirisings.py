#!/usr/bin/env python2 -W ignore
'''a waste of time'''
import argparse
import os
import subprocess
import urllib2
from PyLyrics import PyLyrics
from google import google


def main():
    '''runs the code'''
    parser = argparse.ArgumentParser(description='this app is kinda crappy, \
just a heads up')
    parser.add_argument('song', help='search terms for to find the song',
                        nargs='+')
    parser.add_argument('-v', '--voice', help='voice for siri to sing with, \
default is samantha', default='samantha')
    parser.add_argument('-s', '--save', help='instead of singing it, save it \
to the specified file so you can enjoy it later')
    parser.add_argument('-l', '--showlyrics', help='show the lyrics',
                        action='store_true')
    args = parser.parse_args()
    candidates = search_for_song(' '.join(args.song))
    for singer, song in candidates:
        try:
            sing_song(singer, song, args.voice, args.save, args.showlyrics)
            return
        except ValueError:
            continue
    print 'no songs found, try better search terms.'


def search_for_song(search_terms):
    '''finds a list of songs from the search terms'''
    search_terms = 'site:lyrics.wikia.com {}'.format(search_terms)
    search_results = google.search(search_terms, 2)
    pairs = (item.link.split('lyrics.wikia.com/wiki/')[1] for item in search_results)
    pairs = (tuple(pair.split(':')) for pair in pairs if ':' in pair)
    pairs = (pair for pair in pairs if 'category' not in pair[0].lower())
    return list(pairs)


def sing_song(singer, song, voice, savefile=None, showlyrics=False):
    '''sings the song'''
    lyrics = PyLyrics.getLyrics(singer, song)
    print urllib2.unquote('singing {} by {}'.format(song, singer).replace('_',
                                                                          ' '))
    if showlyrics:
        print lyrics
    saveargs = []
    if savefile is not None:
        _, ext = os.path.splitext(savefile)
        if ext.lower() != '.aiff':
            savefile += '.aiff'
        saveargs = ['-o', savefile]
        print 'Saving to {}'.format(savefile)
    subprocess.call(['say', '-v', voice] + saveargs + [lyrics])


if __name__ == '__main__':
    main()
