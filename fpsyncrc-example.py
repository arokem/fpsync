"""Configuration file for fpsynrc.

This file must either be named ~/.fpsyncrc.py or
~/usr/etc/fpsyncrc.py, or specified using the -config option.
"""

# We default to an ssh channel.  The trailing dot is there to
# give properly assembled paths starting at $HOME if / is added
server_home = 'myservername:.'

# Some file/directory which must exist on the server for the script to
# run at all.  Useful to prevent it from running if some NFS mount is
# missing, for example.

MUST_EXIST  = '~/.ssh'

"""
List of things to update.  It is made of dicts:

dict(dir1 = '~',
     dir2 = '~/lw',
     to_update = ('code','research'),
     exclude_from = None,
     )

- dir1/2 are the directories to update.

- to_update is a tuple of files and
 directories which must exist in both dir1 and dir2.  They are updated from
 one to the other based on the selected mode: 'up': 1->2, 'down': 2->1.

 Note that the entries in to_update CAN NOT have subdirectories in them. If
 you put A/B in your list, B/ will end up at the top level 'dir2' target.  For
 updating a directory which lives in dir1/A/B to dir2/A/B, make another entry
 in the TO_UPDATE list with only one level.

- exclude_from: if not None, it must be the name of a file with exclusions
 to be passed to rsync.

 WARNING: because of the semantics of rsync, the files and directories listed
 must NEVER end in '/'.  """

home = dict(dir1 = '~',
            dir2 = server_home,

            to_update = """.emacs .lyx .bashrc .vimrc
            code research talks teach www""".split(),

            exclude_from = '~/path/to/fpsyncrc-ucb.excludes',
            )

local_data = dict(dir1 = '~/.local/share',
                  dir2 = server_home + '/.local/share',

                  to_update = ['data',
                               ],
                  exclude_from = None,
                  )

# Create the list of configs to use in the update process
TO_UPDATE = []
TO_UPDATE.append(home)
TO_UPDATE.append(local_data)
