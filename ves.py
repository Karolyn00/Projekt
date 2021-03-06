from PIL import Image

class VESread:
  def __init__(self, width, content):
    self.in_width = int(width)
    self.render(content)

  def render(self, content):
    data = content.split("\n")
    header = data[0].split(" ")

    if header[0]=='VES': 
      self.width = round(float(header[2]))
      self.height = round(float(header[3]))
      if self.in_width == "":
        self.output_width = self.width
        self.output_height = self.height 
                                           
      else:
        self.output_width = round(float(self.in_width))
        self.output_height = int(self.height/self.width * self.output_width)
    self.img = Image.new("RGB", (self.output_width, self.output_height), (255,255,255))

    for t in data[1:]:
      line = t.split(" ")
      self.prikaz(line)

  def prikaz(self, line):
    if line == "\n":
      pass
    else:
      prikaz = line[0]
      if prikaz == "CLEAR":
        self.clear_im(self.hexColor(line[1]))
      elif prikaz == "LINE":
        Ax = float(line[1])
        Ay = float(line[2])
        Bx = float(line[3])
        By = float(line[4])
        thickness = self.convert_x(float(line[5]))
        color = self.hexColor(line[6])
        self.thick_line(self.convert_point((Ax, Ay)), self.convert_point((Bx, By)), thickness, color)
      elif prikaz == "RECT":
        Ax = float(line[1])
        Ay = float(line[2])
        width = float(line[3])
        height = float(line[4])
        thickness = self.convert_x(float(line[5]))
        color = self.hexColor(line[6])
        self.RECT(self.convert_point((Ax, Ay)), self.convert_x(width), self.convert_x(height), thickness, color)
      elif prikaz == "TRIANGLE":
        Ax = float(line[1])
        Ay = float(line[2])
        Bx = float(line[3])
        By = float(line[4])
        Cx = float(line[5])
        Cy = float(line[6])
        thickness = self.convert_x(float(line[7]))
        color = self.hexColor(line[8])
        self.TRIANGLE(self.convert_point((Ax, Ay)), self.convert_point((Bx, By)), self.convert_point((Cx, Cy)), thickness, color)
      elif prikaz == "CIRCLE":
        Sx = float(line[1])
        Sy = float(line[2])
        r = self.convert_x(float(line[3]))
        thickness = self.convert_x(float(line[4]))
        color = self.hexColor(line[5])
        self.CIRCLE(self.convert_point((Sx, Sy)), r, thickness, color)
      elif  prikaz == "FILL_CIRCLE":
        Sx = float(line[1])
        Sy = float(line[2])
        r = self.convert_x(float(line[3]))
        color = self.hexColor(line[4])
        self.FILL_CIRCLE(self.convert_point((Sx, Sy)), r, color)
      elif prikaz == "FILL_TRIANGLE":
        Ax = float(line[1])
        Ay = float(line[2])
        Bx = float(line[3])
        By = float(line[4])
        Cx = float(line[5])
        Cy = float(line[6])
        color = self.hexColor(line[7])
        self.FILL_TRIANGLE(self.convert_point((Ax, Ay)), self.convert_point((Bx, By)), self.convert_point((Cx, Cy)), color)
      elif prikaz == "FILL_RECT":
        Ax = float(line[1])
        Ay = float(line[2])
        width = float(line[3])
        height = float(line[4])
        color = self.hexColor(line[5])
        self.FILL_RECT(self.convert_point((Ax, Ay)), self.convert_x(width), self.convert_x(height), color)
  
  
  def hex2dec(self, hex_num):
    hex_num = hex_num.replace("\r", "")
    decimal = 0
    for index in range(len(hex_num)):
      num = hex_num[(index+1)*(-1)].upper()
      if ord("A") <= ord(num) <= ord("F"):
        num = ord(num) - 65 + 10
      else:
        num = int(num)
      decimal += num * 16 ** index
    return decimal


  def hexColor(self, color):
    self.color = color.replace("\n", "")
    r = self.hex2dec(self.color[1:3])
    g = self.hex2dec(self.color[3:5])
    b = self.hex2dec(self.color[5:])

    return (r, g, b)


  def overenie(self, body, color):
    for bod in body:
      if bod[0] < 0 or bod[1] < 0 or bod[0] >= self.output_width or bod[1] >= self.output_height:
        pass
      else:
        self.img.putpixel(bod, color)

  def clear_im(self, color):
    for i in range(self.output_width):
      for j in range(self.output_height):
        self.img.putpixel((i, j), color)

  def linePixels(self, A, B):
    pixels = []
    if A[0] == B[0]:
      if A[1] > B[1]:
        A,B = B,A
      for y in range(A[1], B[1] + 1):
        pixels.append((A[0], y))
    elif A[1] == B[1]:
      if A[0] > B[0]:
        A,B=B,A
      for x in range(A[0], B[0] + 1):
        pixels.append((x, A[1]))
    else:
      if A[0] > B[0]:
        A,B=B,A 
      dx = B[0] - A[0] 
      dy = B[1] - A[1]
      if abs(dy/dx) > 1:
        for y in range(min(A[1], B[1]), max(A[1],B[1]) + 1):
          x = int((y - A[1] + (dy/dx) * A[0]) * (dx/dy))
          pixels.append((x, y))
      else:
        for x in range(min(A[0], B[0]), max(A[0], B[0])+ 1):
          y = int((B[1] - A[1])/(B[0] - A[0]) * (x - A[0]) + A[1])
          pixels.append((x,y))
    return pixels

  def line(self, A, B, color):
    body = []
    if A[0] == B[0]:
      if A[1] > B[1]:
        A,B = B,A
      for y in range(A[1], B[1] + 1):      
        body.append((A[0],y))
    elif A[1] == B[1]:
      if A[0] > B[0]:
        A,B=B,A
      for x in range(A[0], B[0] + 1):
        body.append((x,A[1]))
    else:
      if A[0] > B[0]:
        A,B=B,A 
      dx = B[0] - A[0] 
      dy = B[1] - A[1]
      if abs(dy/dx) > 1:
        for y in range(min(A[1], B[1]), max(A[1],B[1]) + 1):
          x = int((y - A[1] + (dy/dx) * A[0]) * (dx/dy))
          body.append((x,y))
      else:
        for x in range(min(A[0], B[0]), max(A[0], B[0])+ 1):
          y = int((B[1] - A[1])/(B[0] - A[0]) * (x - A[0]) + A[1])
          body.append((x,y))
    self.overenie(body,color)

  def getY(self, point):
      return point[1]
    
  def FILL_TRIANGLE(self, A, B, C, color):
    V = sorted([A, B, C], key=self.getY)
    left = self.linePixels(V[0], V[1]) + self.linePixels(V[1], V[2])
    right = self.linePixels(V[0], V[2])

    Xmax = max(A[0], B[0], C[0])
    Xmin = min(A[0], B[0], C[0])

    if V[1][0] == Xmax:
      left, right = right, left

    for y in range(self.getY(V[0]), self.getY(V[2]) + 1):
      x1 = Xmax
      for X in left:
        if X[1] == y and X[0] < x1:
          x1 = X[0]
      
      x2 = Xmin
      for X in right:
        if X[1] == y and X[0] > x2:
          x2 = X[0]

      if x2 < 0:
        continue
      if x2 > self.img.width:
        x2 = self.img.width - 1
      if x1 < 0:
        x1 = 0

      self.line((x1, y), (x2, y), color)

  def FILL_CIRCLE(self,S, r, color):
    for x in range(0, int(r/2**(1/2)) + 1):
      y = int((r**2 - x**2)**(1/2))

      self.line((x + S[0], y + S[1]), (x + S[0], -y + S[1]), color)
      self.line((y + S[0], x + S[1]), (y + S[0], -x + S[1]), color)
      self.line((-x + S[0], -y + S[1]), (-x + S[0], y + S[1]), color)
      self.line((-y + S[0], -x + S[1]), (-y + S[0], x + S[1]), color)

  def CIRCLE(self, S, r, thickness, color):
    for x in range(0, int(r/2**(1/2)) + 1):
      y = int((r**2 - x**2)**(1/2))
      
      self.FILL_CIRCLE((x + S[0], y + S[1]), thickness/2, color)
      self.FILL_CIRCLE((y + S[0], x + S[1]), thickness/2, color)
      self.FILL_CIRCLE((y + S[0], -x + S[1]), thickness/2, color)
      self.FILL_CIRCLE((x + S[0], -y + S[1]), thickness/2, color)
      self.FILL_CIRCLE((-x + S[0], -y + S[1]), thickness/2, color)
      self.FILL_CIRCLE((-y + S[0], -x + S[1]), thickness/2, color)
      self.FILL_CIRCLE((-y + S[0], x + S[1]), thickness/2, color)
      self.FILL_CIRCLE((-x + S[0], y + S[1]), thickness/2, color)
      
  def TRIANGLE(self, A, B, C, thickness, color):

    self.thick_line(A, B, thickness, color)
    self.thick_line(B, C, thickness, color)
    self.thick_line(A, C, thickness, color)

  def thick_line(self, A, B, thickness, color):
    pixels = self.linePixels(A, B)
    for X in pixels:
      self.FILL_CIRCLE(X, thickness/2, color)

  def RECT(self,A,width,height,thickness,color):
    B = (A[0]+width,A[1])
    C = (A[0],A[1]+height)
    D = (A[0]+width,A[1]+height)
    self.thick_line(A, B,  thickness, color)
    self.thick_line(A, C, thickness, color)
    self.thick_line(B, D, thickness, color)
    self.thick_line(D,C, thickness, color)
    
  def FILL_RECT(self,A,width,height,color):
    body = []
    for x in range(A[0],A[0]+width):
      for y in range(A[1],A[1]+height):
        body.append((x,y))
    self.overenie(body,color)


  def convert_x(self, x):
    return int(x/self.width * self.output_width)

  def convert_y(self, y):
    return int(y/self.height * self.output_height)

  def convert_point(self, X):
    return (self.convert_x(X[0]), self.convert_y(X[1])) 
