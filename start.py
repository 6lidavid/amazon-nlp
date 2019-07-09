{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "showing info https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import tensorflow as tf\n",
    "from tensorflow import keras\n",
    "import nltk\n",
    "nltk.download()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: scikit-learn in /anaconda3/envs/amazon-nlp-env/lib/python3.7/site-packages (0.21.2)\n",
      "Requirement already satisfied: scipy>=0.17.0 in /anaconda3/envs/amazon-nlp-env/lib/python3.7/site-packages (from scikit-learn) (1.3.0)\n",
      "Requirement already satisfied: numpy>=1.11.0 in /anaconda3/envs/amazon-nlp-env/lib/python3.7/site-packages (from scikit-learn) (1.16.4)\n",
      "Requirement already satisfied: joblib>=0.11 in /anaconda3/envs/amazon-nlp-env/lib/python3.7/site-packages (from scikit-learn) (0.13.2)\n"
     ]
    }
   ],
   "source": [
    "%%bash\n",
    "pip install scikit-learn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "trainData = pd.read_csv('./data/amazon_review_full_csv/train.csv', header=None, names=['rating', 'title', 'review'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "testData = pd.read_csv('./data/amazon_review_full_csv/test.csv', header=None, names= ['rating', 'title', 'review'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>rating</th>\n",
       "      <th>title</th>\n",
       "      <th>review</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3</td>\n",
       "      <td>more like funchuck</td>\n",
       "      <td>Gave this to my dad for a gag gift after direc...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>5</td>\n",
       "      <td>Inspiring</td>\n",
       "      <td>I hope a lot of people hear this cd. We need m...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>5</td>\n",
       "      <td>The best soundtrack ever to anything.</td>\n",
       "      <td>I'm reading a lot of reviews saying that this ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Chrono Cross OST</td>\n",
       "      <td>The music of Yasunori Misuda is without questi...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Too good to be true</td>\n",
       "      <td>Probably the greatest soundtrack in history! U...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>5</td>\n",
       "      <td>There's a reason for the price</td>\n",
       "      <td>There's a reason this CD is so expensive, even...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>1</td>\n",
       "      <td>Buyer beware</td>\n",
       "      <td>This is a self-published book, and if you want...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>4</td>\n",
       "      <td>Errors, but great story</td>\n",
       "      <td>I was a dissapointed to see errors on the back...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>1</td>\n",
       "      <td>The Worst!</td>\n",
       "      <td>A complete waste of time. Typographical errors...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>1</td>\n",
       "      <td>Oh please</td>\n",
       "      <td>I guess you have to be a romance novel lover f...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   rating                                  title  \\\n",
       "0       3                     more like funchuck   \n",
       "1       5                              Inspiring   \n",
       "2       5  The best soundtrack ever to anything.   \n",
       "3       4                       Chrono Cross OST   \n",
       "4       5                    Too good to be true   \n",
       "5       5         There's a reason for the price   \n",
       "6       1                           Buyer beware   \n",
       "7       4                Errors, but great story   \n",
       "8       1                             The Worst!   \n",
       "9       1                              Oh please   \n",
       "\n",
       "                                              review  \n",
       "0  Gave this to my dad for a gag gift after direc...  \n",
       "1  I hope a lot of people hear this cd. We need m...  \n",
       "2  I'm reading a lot of reviews saying that this ...  \n",
       "3  The music of Yasunori Misuda is without questi...  \n",
       "4  Probably the greatest soundtrack in history! U...  \n",
       "5  There's a reason this CD is so expensive, even...  \n",
       "6  This is a self-published book, and if you want...  \n",
       "7  I was a dissapointed to see errors on the back...  \n",
       "8  A complete waste of time. Typographical errors...  \n",
       "9  I guess you have to be a romance novel lover f...  "
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "trainData.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
