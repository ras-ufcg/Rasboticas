import sim  #importar funcoes do coppeliasim
import time #importar o uso do tempo/relogio
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
err_codel,l_motor_handle = sim.simxGetObjectHandle(clientID,"Pioneer_p3dx_leftMotor", sim.simx_opmode_blocking) #motor esquerda
err_coder,r_motor_handle = sim.simxGetObjectHandle(clientID,"Pioneer_p3dx_rightMotor", sim.simx_opmode_blocking) #motor direita

if(clientID!=-1): # Se estiver conectado fazer:
    #definindo o valor da velocidade para os objetos
    err_code = sim.simxSetJointTargetVelocity(clientID,l_motor_handle,1.0,sim.simx_opmode_streaming)
    err_code = sim.simxSetJointTargetVelocity(clientID,r_motor_handle,1.0,sim.simx_opmode_streaming)
    time.sleep(6) # pausa de 4s
    err_code = sim.simxSetJointTargetVelocity(clientID,l_motor_handle,0,sim.simx_opmode_streaming)
    err_code = sim.simxSetJointTargetVelocity(clientID,r_motor_handle,0,sim.simx_opmode_streaming)
    time.sleep(3) #pausa de 3s