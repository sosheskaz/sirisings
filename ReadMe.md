# Siri Sings

This app makes siri sing songs using the built-in `sirising` command. It's not quite the same as sire,
but meh, close enough.

## Installing

Clone or download this repo. Run `install.sh`. Piping to bash won't work.

## Uninstalling

Run `rm /usr/local/bin/sirisings`. Clean up the dependencies yourself if you really care.

## Running

See `sirisings -h` for the help message at any time. Here it is now.

```
usage: sirisings [-h] [-v VOICE] song [song ...]

this app is kinda crappy, just a heads up

positional arguments:
  song                  search terms for to find the song

optional arguments:
  -h, --help            show this help message and exit
  -v VOICE, --voice VOICE
                        voice for siri to sing with, default is samantha
```

You don't need to quote your search terms. Including the artist might help sometimes.

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
