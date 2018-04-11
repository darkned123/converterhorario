import datetime
from datetime import date



def converterHorario(horario):
  try:  
    hora_manha = datetime.datetime.strptime('07:30', '%H:%M').time()
    hora_tarde = datetime.datetime.strptime('14:00', '%H:%M').time()
    hora_tarde_noite = datetime.datetime.strptime('14:00', '%H:%M').time()
    hora_noite = datetime.datetime.strptime('18:30', '%H:%M').time()
    ano = int(datetime.date.today().strftime("%Y"))
    mes = int(datetime.date.today().month)
    dia = int(datetime.date.today().strftime("%d"))
    #0-monday 1-tuesday 2-wednesday 3-thursday
    dia_semana = datetime.date.today().weekday()
    dia_semana +=2
    print(dia_semana)
    
    semana = list()
    turno = list ()
    hora =list ()
    horario_turno = " ".join(horario)
    horario_turno = horario_turno.split(" ")
    alpha = True

    for i in horario_turno:
      if str(i).isnumeric() and alpha:
        semana.append(i)
        continue
      elif str(i).isalpha:
        alpha = False
        turno.append(i)
    
    if dia_semana in semana:
      print(dia_semana)
    
    print(semana)
    print(turno)
   
    hora_mtn = ""
   
    if 'M' in horario:
     print("Manhã")
     hora_mtn = hora_manha
  
  
    elif ('T' in horario) and ('N' in horario):
     print("Tarde e Noite")
     hora_mtn=hora_tarde_noite
 
  
    elif 'T' in horario:
     print("Tarde")
     hora_mtn=hora_tarde
  
    elif 'N' in horario:
     print("Noite")
     hora_mtn=hora_noite
     
    turno.pop(0)
    cont = 0
    first = 0
    inicio = 0
    for i in turno:
      if str(i).isnumeric():
        if first == 0 :
          first = 1
          for j in range(1,int(i)+1):
            cont = cont + 50
            if j == 3 or j == 5:
              cont = cont + 10
          inicio = cont
        else:
          cont = cont + 50
          if int(i) == 3 or int(i) == 5:
              cont = cont + 10

    delta =  datetime.timedelta(minutes = inicio-50)
    hora_inicio =  (datetime.datetime.combine(datetime.date(ano,mes,dia),hora_mtn)+delta) 
    delta =  datetime.timedelta(minutes = cont)
    hora_termino = (datetime.datetime.combine(datetime.date(ano,mes,dia),hora_mtn)+delta) 
    return (hora_inicio,hora_termino)
  except:
    raise


"""
dia da semana/(manhã,tarde,noite)/horário
3456			M,T,N				123456

ex.:
horario = "35T5N1"
35T5N1
horario = "35T345N12"
35T12
"""

horario = "35T5N123"

hora_inicio,hora_termino=converterHorario(horario)
print(hora_inicio)
print(hora_termino)
print(hora_termino - hora_inicio)