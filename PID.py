#PID control simulation
setpoint = 22.0
temp = 18.0
Kp, Ki, Kd = 0.6, 0.0009, 0.05

integral = 0.0
prev_error = setpoint - temp

for step in range(15):
    error = setpoint - temp
    integral += error
    derivative = error - prev_error

    heater = Kp * error + Ki * integral + Kd * derivative
    temp += heater * 0.5          # crude model of the room responding
    prev_error = error

    print(f"Step {step+1}: temp = {temp:.2f}")