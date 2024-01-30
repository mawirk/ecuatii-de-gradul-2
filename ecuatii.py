import math,time


a1 = ""
a2 = ""
a3 = ""
a4 = ""
message = ""



while a1 == "" and a2 == "" and a3 == "" and a4 == "" and message == "":
  a1 = str(input("Coeficientul a: "))
  try:
    if a1.isnumeric() == False:
      h1 = int(a1)
  except Exception:
      while a1.isalpha() == True:
        print("\nEroare. Pune un numar")
        a1 = str(input("Coeficientul a: "))
        h1 = int(a1)

  a2 = str(input("Coeficientul b: "))
  try:
    if a2.isnumeric() == False:
      h2 = int(a2)
  except Exception:
    while a2.isalpha() == True:
      print("\nEroare. Pune un numar")
      a1 = str(input("Coeficientul b: "))
      h1 = int(a2)

  a3 = input("Coeficientul c: ")
  try:
    if a3.isnumeric() == False:
      h3 = int(a3)
  except Exception:
      while a3.isalpha() == True:
        print("\nEroare. Pune un numar")
        a3 = str(input("Coeficientul c: "))
        h3 = int(a3)

  a4 = input("Ce litera din alfabet este variabila (x,z,t,etc): ")
  while a4.isnumeric() == True:
    print("\nEroare. Pune o litera din alfabet")

# if a2 == "+" + a2:
#    message = input("\nEcuatia ta arata asa?: "+""+str(a1)+""+a4+"**2"+"+"+str(a2)+""+a4+""+str(a3)+" = "+"0"+"\n"+"da/nu: ").lower()

message = input("\nEcuatia ta arata asa?: "+""+str(a1)+""+a4+"**2"+""+str(a2)+""+a4+""+str(a3)+" = "+"0"+"\n"+"da/nu: ").lower()
if message == "da":
  global delta
  delta = int(a2)**2 - 4 * int(a1) * int(a3)
  print("-------------------------------\nDiscriminantul tau este: " + str(delta)+"\n-------------------------------")
  time.sleep(1)
  delta = str(delta)
  if delta.isnumeric() == False:
    delta = int(delta)
    delta = delta + delta * -2
    sqrt = int(math.sqrt(delta))
    b = -int(a2)
    x1 = str(str(b)+"+"+str(sqrt)+"i"+ "/"+ str(2* int(a1)))
    print("x1 este egal cu: {}".format(x1))
    x2 = str(str(b)+ "-"+str(sqrt)+"i"+ "/"+ str(2* int(a1)))
    print("x2 este egal cu: {}".format(x2))
    print("S="+"{"+str(x1)+";"+str(x2)+"}"+"\n(S-ar putea sa simplifici partea reala de la numarator cu numitorul cand este cazul)")
  else:
    delta = int(delta)
    sqrt = int(math.sqrt(delta))
    b = -int(a2)
    x1 = int((b + sqrt) / 2* int(a1))
    print("x1 este egal cu: {}".format(x1))
    x2 = int((b - sqrt) / 2* int(a1))
    print("x2 este egal cu: {}".format(x2))
    print("S="+"{"+str(x1)+";"+str(x2)+"}")
elif message == "nu":
  a1 = ""
  a2 = ""
  a3 = ""
  a4 = ""
  message = ""
elif message != "da" or message != "nu":
  print("There is an error with your response")
  a1 = ""
  a2 = ""
  a3 = ""
  a4 = ""
  message = ""

   
# cc = str(input("Provide a number: "))
# if cc.isnumeric() == False:
#   print(int(cc) - int(cc) * 2)

# print(cc.isnumeric())
# print(cc)

