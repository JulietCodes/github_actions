import pytest

def tet_calc_addition():
  # Function test the output of 2+4
  output = 2+ 4
  assert output ==6

def test_calc_subtraction():
  # Function to test the output 2-4
  output = 2-4
  assert output == -2

def test_calc_multiply():
  # Function test the output 2*4
  output = 2 * 4
  assert output == 8

def test_calc_coucou():
  # Function test if the output returns 'hello'
  output = 'hello'
  assert output == 'hello'
