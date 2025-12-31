{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9347163b-a972-4cfa-ad6c-380dcb45a6aa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n"
     ]
    }
   ],
   "source": [
    "x=10\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "13af9909-43bf-464e-b0bf-1e3001a5f861",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-5\n"
     ]
    }
   ],
   "source": [
    "a=5\n",
    "print(-a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "68f70ee9-4d73-406c-ad7d-f147e295ea03",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "p=10\n",
    "q=5\n",
    "print(p>q)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "1fea5552-8058-486f-b257-56ea13a757af",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "false\n",
      "true\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "x=\"true\"\n",
    "y=\"false\"\n",
    "print (x and y)\n",
    "print(x or y)\n",
    "print(not x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "08a5afcb-dede-44e9-8328-8c3939022bb9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "true\n"
     ]
    }
   ],
   "source": [
    "is_pass =\"true\"\n",
    "print(is_pass)  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "fbd1d9cf-f9c5-42b1-935d-b3348403451b",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "unsupported operand type(s) for &: 'str' and 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[17], line 3\u001b[0m\n\u001b[0;32m      1\u001b[0m a\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m5\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m      2\u001b[0m b\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m3\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m----> 3\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[43ma\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m&\u001b[39;49m\u001b[43m \u001b[49m\u001b[43mb\u001b[49m)\n\u001b[0;32m      4\u001b[0m \u001b[38;5;28mprint\u001b[39m(a \u001b[38;5;241m|\u001b[39m b)\n",
      "\u001b[1;31mTypeError\u001b[0m: unsupported operand type(s) for &: 'str' and 'str'"
     ]
    }
   ],
   "source": [
    "a=\"5\"\n",
    "b=\"3\"\n",
    "print(a & b)\n",
    "print(a | b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "d36cfea8-2b2c-412e-b894-693672d5357d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "numbers =[1,2,3,4,6]\n",
    "print(2 in numbers)\n",
    "print(5 not in numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "92a312ff-b32c-4cb6-8f77-435ac49e9a24",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "x=10\n",
    "y=10\n",
    "print(x is y)\n",
    "print(x is not y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f275795b-08a2-4a1b-be2d-f89bda843eaf",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
