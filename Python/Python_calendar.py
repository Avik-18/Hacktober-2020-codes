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
      "CALENDER\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "input year: 2020\n",
      "input month: 11\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   November 2020\n",
      "Mo Tu We Th Fr Sa Su\n",
      "                   1\n",
      " 2  3  4  5  6  7  8\n",
      " 9 10 11 12 13 14 15\n",
      "16 17 18 19 20 21 22\n",
      "23 24 25 26 27 28 29\n",
      "30\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(\"CALENDER\")\n",
    "import calendar\n",
    "\n",
    "y=int(input(\"input year:\"))\n",
    "m=int(input(\"input month:\"))\n",
    "print(calendar.month(y,m))"
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
 "nbformat_minor": 4
}