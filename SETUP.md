## Initial Setup

### __Version__
The main version for this is `Python 3.7.3`

<hr/>

### __Step 1: Downloading the dataset__
Please download the dataset into `data` directory. If no `data` directory exists create one and download the files into it.

Open the link https://drive.google.com/drive/folders/0Bz8a_Dbh9Qhbfll6bVpmNUtUcFdjYmF2SEpmZUZUcVNiMUw1TWN6RDV3a0JHT3kxLVhVR2M

Click on the file: **amazon_review_full_csv_tar**

This should take some time to download. Once downloaded unzip the file by clicking on them.


### __Step 2: Create a virtual environment__
This first part is to create a virtual Python environement that installs packages necessary for the project.

If running the following command in the Mac Terminal to create the virtual environment. This only done once in this directory:
`conda create -n <name_of_environment> --file mac-spec-file.txt`

**Once created substitue the `<name_of_environment>` with the new name in this document.**

<hr/>

### __Step 3: Activating the Virtual Environment__

<div>
If running version `4.6` or greater of `Anaconda` run the command: <code>conda activate <name_of_environemt></code>
</div>


If using an earlier version of <code>Anaconda</code>, to activate the environement on a Mac run the command: `source activate <name_of_environment>`


When activated the terminal should read:

`(name_of_environment) $`
<hr/>

### __Step 4: Install the Anaconda Notebook Extensions__

Once the environment is running/activated add the following extensions (this is only done once):

`conda install nb_conda`

`conda install nb_conda_kernels`

<hr/>

### __Step 5: Install Tensorflow 2__
 With the environment activated run the command":

 `pip install tensorflow==2.0.0-beta1`


<hr/>

### __Step 6: Opening the Jupyter Notebook__
To open the `Jupyter` notebook run the command in the project's directory:
`jupyter notebook`

Your browser should open up with the files and directories listed
<hr/>

### __Step 7: Creating a Python3 NoteBook Starter File__

In the browser create a Python 3 file. Open the file and in first block add:
```
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
```

Hit Shift and Enter/Return to run the cell.

In the next two cell read in the two datasets and hit the Shift and Enter to run each cell. In the first cell write

`trainData = pd.read_csv('./data/amazon_review_full_csv/train.csv', header=None, names=['rating', 'title', 'review'])`




In the next cell write:

`testData = pd.read_csv('./data/amazon_review_full_csv/test.csv', header=None, names= ['rating', 'title', 'review'])`


To test you have some data in a new cell write and check to see the output.
`trainData.head(10)`

<hr/>


### __Step 8: Deactivating the Environment__


<div>
If running version `4.6` or greater of `Anaconda` run the command: <code>conda deactivate</code>
</div>


If using an earlier version of <code>Anaconda</code>, to activate the environement on a Mac run the command: `source deactivate`


The terminal should now read:

`$`

### __Step 9: Repeating Steps working with file__
After going through the intial setup you will only be running steps 3, 6, and 8.

Be sure to make branches with your progress and submit PR.