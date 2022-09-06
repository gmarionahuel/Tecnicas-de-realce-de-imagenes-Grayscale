
#Negativo de una imágen

def negativo(img):                #Negativo de una imágen ingresada como parámetro
  (F,C) = img.shape
  negative = np.zeros((F,C),np.uint8)
  for i in range(F):
    for j in range (C):
      negative[i,j] = 255 - img[i,j]
  plt.show()           
  plt.imshow(negative,cmap='gray')
  
  
  #Estiramiento de contraste
  
  def contrastStretching(img,r1,r2,s1,s2):
  (F,C) = img.shape
  contrasted = np.zeros((F,C),np.uint8)
  max = np.max(img)
  min = np.min(img)
  for i in range(F):      
    for j in range (C):
      if img[i,j]<r1:
        contrasted[i,j]= ((s1/r1)*img[i,j])
      elif  img[i,j] < r2:
          contrasted[i,j]=(((s2-s1)/(r2-r1))*img[i,j])
      else:
          contrasted[i,j]= (((255-s2)/(255-r2))*img[i,j])  
  plt.show()         
  plt.imshow(contrasted,cmap='gray')
  return contrasted
  
  
  #Rango dinámico
  
  def rangoDinamico(img):
  (F,C) = img.shape
  rango = np.zeros((F,C),np.uint8)
  c = 255/math.log10(1+np.max(img))
  max = np.max(img)
  min = np.min(img)
  for i in range(F):
    for j in range (C):
      rango[i,j] = (255*((img[i,j]-min)/(max-min)))
  return rango      #Muestro la salida como matriz
  
  
  
  #Bit plane slicing
    
  def bitPlane(img,x1,x2):
  (F,C) = img.shape
  bitPlane = np.zeros((F,C),np.uint8)
  c = 255/math.log10(1+np.max(img))
  max = np.max(img)
  min = np.min(img)
  for i in range(F):
    for j in range (C):
      if img[i,j]>x1 and img[i,j]<x2:
       bitPlane[i,j] = 0
      else:
        bitPlane[i,j] = 255 
  return bitPlane      #Muestro la salida como matriz
  
  
  
  # Para visualizar la imagen de salida se puede usar matplotlib.pyplot importandolo con la siguiente linea: 'import matplotlib.pyplot as plt', y luego con la función plt.imshow()
