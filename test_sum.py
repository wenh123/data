import pytest

def sum2(a,b):
  return a+b

def test_sum1():
  assert sum2(3,6) == 9

def test_sum2():
  assert sum2(0,0) == 0
