"""
Promote

This script "promotes" a file by copying it from one directory to another,
using a hash to verify that the copied file is the same as the original.
It keeps a log of these movements, and will check to see if there are any
git commits pending before going through with the move.
"""