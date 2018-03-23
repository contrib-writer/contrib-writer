# setup script, run once!: 
#   calculate number of dirs to make (7*52(?)) and make them in "cells"
#   initialize each with 10+4 commit files so that they have some background noise


# daily script:
#   get message from text file
#       convert to a binary grid of size of cells
#   in each cells folder
#       determine if part of text or not
#       if text
#           make appropriate number of commits on the date of cell
#       else
#           make background number of commits on date of cell
#   push changes to master