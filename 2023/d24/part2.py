
# This code was not written at 6am anymore, but I don't feel like the disclaimer should be any different, with the AoC days stacking up, the holiday festivities ramping up and the exhaustion and mind fog increasing, the levels of "sorry about my code, maybe" are about the same.

# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.



"""
https://www.wolframalpha.com/input?i=system+equation+calculator&assumption=%7B%22F%22%2C+%22SolveSystemOf4EquationsCalculator
"""



import random
def aoc(filename):
  lines = []
  with open(filename, "r") as f:
    for line in f:
      pos, vel = line.strip("\n").split(" @ ")
      px, py, pz = map(int, pos.split(", "))
      vx, vy, vz = map(int, vel.split(", "))
      lines.append((px, py, pz, vx, vy, vz))

    for _ in range(100):
      p1, p2 = random.sample(lines, 2)
      get_equation(p1, p2)


def get_equation(p1, p2):
  x, y, z, dx, dy, dz = p1
  x2, y2, z2, dx2, dy2, dz2 = p2
  
  """
  unknown: 
  X,Y,Z coordinates of your rock
  DX,DY,DZ its velocity

  known
  x,y,z,dx,dy,dz of hailstone line
  
  t - time when rock collides with hailstone 
  placeholder

  X + t DX = x + t dx
  t = (X - x) / (dx - DX)
  X - x = t(dx - DX)
  (X - x)/(dx - DX) = t
  
  same for y
  (Y - y)/(dy - DY) = t
  
  
  put those two together and move things around
  (X - x)/(dx - DX) = (Y - y)/(dy - DY)
  (X - x)*(dy - DY) = (Y - y)*(dx - DX)
  Xdy - XDY - xdy + xDY = Ydx - YDX - ydx + yDX
  
  do the same for line two
  YDX - XDY = Ydx - Xdy - ydx + yDX + xdy - xDY 
  YDX - XDY = Ydx2 - Xdy2 - ydx2 + yDX2 + xdy2 - xDY2 
  
  YDX & XDY are the same so we can then equate the second parts of the equation

  Ydx - Xdy - ydx + yDX + xdy - xDY  = Ydx2 - Xdy2 - ydx2 + yDX2 + xdy2 - xDY2 
  Ydx - Ydx2 - Xdy + Xdy2 + yDX - yDX2  - xDY + xDY2    = - ydx2  + xdy2 + ydx -  xdy
  Y(dx-dx2) + X (dy2-dy) + DX(y-y2) + DY(x2- x) = - y * dx2  + x * dy2 + y * dx -  x * dy

  Do this for 4 hailstones
  Y(dx-dx2) + X (dy2-dy) + DX(y-y2) + DY(x2- x) = - ydx2  + xdy2 + ydx -  xdy



  Y*1 + X*2 + DX*6 + DY*1 = 55
  Y*3 + X*3 + DX*-6 + DY*0 = 117
  Y*2 + X*3 + DX*-12 + DY*-8 = 98
  Y*0 + X*1 + DX*12 + DY*6 = 12

  for example
  Y * -1 + X* -3 + DX* -18 + DY* -7 = -70
  Y * 3 + X* 3 + DX* -6 + DY* 0 = 117
  Y * -1 + X* -3 + DX* -18 + DY* -7 = -70
  Y * -3 + X* -6 + DX* -6 + DY* 1 = -153
  
  put these in the equation solver.
  
  do the same to extract Z

  cake is bake
  """
  # print values out so that I get the equations to insert into the wolfram equation solver
  print(f"Y *{dx-dx2} + X*{dy2-dy} + A*{y-y2} + B * {x2- x} = {- y2 * dx2  + x2 * dy2 + y * dx -  x * dy}")
  # (dy'-dy) X + (dx-dx') Y + (y-y') DX + (x'-x) DY =  x' dy' - y' dx' - x dy + y dx
  print(f"Z *{dx-dx2} + X*{dz2-dz} + A*{z-z2} + B * {x2- x} = {- z2 * dx2  + x2 * dz2 + z * dx -  x * dz}")
  # Y * dx-dx2 + X* dy2-dy + V* y-y2 + W * x2- x = - y * dx2  + x * dy2 + y * dx -  x * dy
  print(f"Y * {dx-dx2} + X* {dy2-dy} + V* {y-y2} + W * {x2- x} -  { y * dx2  - x * dy2 - y * dx +  x * dy}")
  e = Y * dx-dx2 + X* dy2-dy + V* y-y2 + W * x2- x + y * dx2 - x * dy2 - y * dx +  x * dy

  

# I also tried to use sympy to solve the equation.

from sympy.solvers import solve
from sympy.abc import Z, X, A,B

e = [Z *["redacted"] + X*["redacted"] + A*["redacted"] + B * ["redacted"] - ["redacted"],
     Z *["redacted"] + X*["redacted"] + A*["redacted"] + B * ["redacted"] + ["redacted"],
     Z *["redacted"] + X*["redacted"] + A*["redacted"] + B * ["redacted"] - ["redacted"],
     Z *["redacted"] + X*["redacted"] + A*["redacted"] + B * ["redacted"]- ["redacted"]]

print(solve(e, [Z, X, A,B]))

A = ["redacted"] 
B = ["redacted"] 
B = ["redacted"]
X = ["redacted"] 
Y = ["redacted"]
Z = ["redacted"]

print(X+Y+Z)


textaoc2 = aoc("text.txt")



  

