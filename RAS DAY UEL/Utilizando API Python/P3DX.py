import sim
import time
sim.simxFinish(-1) 

clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) 
# start a connnection

if clientID!=-1:
    print ("Connected to remote API server")
else:
    print("Not connected to remote API serv")

#Starting the code

#Pegando os objetos da cena

err_codel,l_motor_handle = sim.simxGetObjectHandle(clientID,"Pioneer_p3dx_leftMotor", sim.simx_opmode_blocking)
err_coder,r_motor_handle = sim.simxGetObjectHandle(clientID,"Pioneer_p3dx_rightMotor", sim.simx_opmode_blocking)

if(clientID!=-1):
    err_code = sim.simxSetJointTargetVelocity(clientID,l_motor_handle,1.0,sim.simx_opmode_streaming)
    err_code = sim.simxSetJointTargetVelocity(clientID,r_motor_handle,1.0,sim.simx_opmode_streaming)
    time.sleep(3)
    err_code = sim.simxSetJointTargetVelocity(clientID,l_motor_handle,1.0,sim.simx_opmode_streaming)
    err_code = sim.simxSetJointTargetVelocity(clientID,r_motor_handle,0,sim.simx_opmode_streaming)
    time.sleep(2)
    err_code = sim.simxSetJointTargetVelocity(clientID,l_motor_handle,1.0,sim.simx_opmode_streaming)
    err_code = sim.simxSetJointTargetVelocity(clientID,r_motor_handle,1.0,sim.simx_opmode_streaming)
    time.sleep(3)
    err_code = sim.simxSetJointTargetVelocity(clientID,l_motor_handle,0,sim.simx_opmode_streaming)
    err_code = sim.simxSetJointTargetVelocity(clientID,r_motor_handle,1.0,sim.simx_opmode_streaming)
    time.sleep(2)
    err_code = sim.simxSetJointTargetVelocity(clientID,l_motor_handle,1.0,sim.simx_opmode_streaming)
    err_code = sim.simxSetJointTargetVelocity(clientID,r_motor_handle,1.0,sim.simx_opmode_streaming)
    time.sleep(5)
    err_code = sim.simxSetJointTargetVelocity(clientID,l_motor_handle,0,sim.simx_opmode_streaming)
    err_code = sim.simxSetJointTargetVelocity(clientID,r_motor_handle,1.0,sim.simx_opmode_streaming)
    time.sleep(2)
    err_code = sim.simxSetJointTargetVelocity(clientID,l_motor_handle,1.0,sim.simx_opmode_streaming)
    err_code = sim.simxSetJointTargetVelocity(clientID,r_motor_handle,1.0,sim.simx_opmode_streaming)
    time.sleep(2)
    err_code = sim.simxSetJointTargetVelocity(clientID,l_motor_handle,0,sim.simx_opmode_streaming)
    err_code = sim.simxSetJointTargetVelocity(clientID,r_motor_handle,0,sim.simx_opmode_streaming)
    time.sleep(5)