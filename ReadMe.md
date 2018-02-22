# Siri Sings

This app makes siri sing songs using the built-in `sirising` command. It's not quite the same as siri,
but meh, close enough.

## Installing

Clone or download this repo. Run `install.sh`. Piping to bash won't work.

## Uninstalling

Run `rm /usr/local/bin/sirisings`. Cleaning up the dependencies is left as an exercise for the reader.

## Running

See `sirisings -h` for the help message at any time. Here it is now.

```
$ sirisings -h
usage: sirisings [-h] [-v VOICE] [-s SAVE] [-l] song [song ...]

this app is kinda crappy, just a heads up

positional arguments:
  song                  search terms for to find the song

optional arguments:
  -h, --help            show this help message and exit
  -v VOICE, --voice VOICE
                        voice for siri to sing with, default is samantha
  -s SAVE, --save SAVE  instead of singing it, save it to the specified file
                        so you can enjoy it later
  -l, --showlyrics      show the lyrics
```

You don't need to quote your search terms. Including the artist might help sometimes.

## Quality

This code is top-quality. Pylint said so.

```
$ pylint sirisings/sirisings.py
No config file found, using default configuration

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

## Examples

```bash
$ sirisings but why tho
singing 16 Bars by HIM
```

```
$ sirisings ain\'t no reason
singing Ain't No Reason by Brett Dennen
```

Siri rhythmically sings the song when it does that.
