This files in this directory amis to add the loss function our own defined.

You should put these file into your the directory of the `sklearn` package. For example, when you install `sklearn` as root and the version of python is 3.10, the directory is `/usr/lib/python3.10/site-packages/sklearn/tree`.

**IMPORTANT: you should BACKUP original files!!!** 

After putting these files, run the command `python install.py`.

## Statement
After more tests, we realized that sometimes it doesn't improve the accuracy. :-( 

Considering the time consumption(Although we have used n-vector to accelerate), we recommend that use MSE as the loss function in practice :disappointed_relieved:
