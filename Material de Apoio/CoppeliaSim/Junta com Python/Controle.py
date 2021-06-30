import sim #importar funcoes do coppeliasim
import time #importar o uso do tempo/relogio
import math
sim.simxFinish(-1) #encerra se receber -1

#Conexao api
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) 

#Iniciando conexao
if clientID!=-1:
    print ("Connected to remote API server") #conectado com o coppelia
else:
    print("Not connected to remote API serv") #nao conectado, ou seja, nao iniciou a simulacao

#Starting the code

#Definindo os objetos
# ele envia um erro e um identificador para cada objeto
retorno,junta = sim.simxGetObjectHandle(clientID,"junta", sim.simx_opmode_blocking)

if(clientID!=-1): # Se estiver conectado fazer:
    #definindo o valor da velocidade para os objetos
    retorno = sim.simxSetJointTargetPosition(clientID,junta,90*math.pi/180,sim.simx_opmode_streaming)
    time.sleep(6) # pausa de 4s
    retorno = sim.simxSetJointTargetPosition(clientID,junta,180*math.pi/180,sim.simx_opmode_streaming)
    time.sleep(6) # pausa de 4s
