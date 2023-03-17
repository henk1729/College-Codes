import sys
import math

curr_state = [0, 0, 0, 0]
prev_state = tuple(curr_state)
path = set()
step_count = 0


def input_jugs():
    global path
    
    jug1_max_cap = int(input("Enter jug 1 capacity: "))
    jug2_max_cap = int(input("Enter jug 2 capacity: "))
    target_jug   = int(input("Enter target jug: "))
    target_vol   = int(input("Enter target volume: "))
    target_jug -= 1
    
    curr_state[2] = step_count
    path.add(tuple(i for i in curr_state))
    
    if target_jug != 0 and target_jug != 1:
        print("Invalid target jug input.")
    elif target_vol % math.gcd(jug1_max_cap, jug2_max_cap) == 0:
        if (target_jug == 0 and target_vol <= jug1_max_cap) or (target_jug == 1 and target_vol <= jug2_max_cap):
            print("\nHere are the states:")
            decide_operation(jug1_max_cap, jug2_max_cap, target_jug, target_vol)
        else:
            print("\nTarget volume over target jug capacity.")
    else:
        print("\nThere's no solution.")
    
    
def print_success():
    for cnt in range(len(path)):
        for state in path:
            if state[2] == cnt:
                print("[", state[0], state[1], "]")
    print("\nSUCCESS")
    sys.exit()
    
    
# def print_status(pid):
#     print("Status: curr_state->", curr_state, "| path->", path)
#     match pid:
#         case 1:
#             print("PID[", pid, "] Process: Fill Jug 1")
#         case 2:
#             print("PID[", pid, "] Process: Fill Jug 2")
#         case 3:
#             print("PID[", pid, "] Process: Fill Jug 1")
#         case 4:
#             print("PID[", pid, "] Process: Pour Jug 2 Into Jug 1")
#         case 5:
#             print("PID[", pid, "] Process: Fill Jug 2")
#         case 6:
#             print("PID[", pid, "] Process: Pour Jug 1 Into Jug 2")
#         case 7:
#             print("PID[", pid, "] Process: Fill Jug 1")
#         case 8:
#             print("PID[", pid, "] Process: Fill Jug 2")
#         case 9:
#             print("PID[", pid, "] Process: Empty Jug 1")
#         case 10:
#             print("PID[", pid, "] Process: Empty Jug 2")
#         case 11:
#             print("PID[", pid, "] Process: Pour Jug 1 Into Jug 2")
#         case 12:
#             print("PID[", pid, "] Process: Pour Jug 2 Into Jug 1")
            
               
def fill_jug1(jug1_max_cap, jug2_max_cap, target_jug, target_vol):
    global curr_state
    global prev_state
    
    prev_state = tuple(curr_state)
    curr_state[0] = jug1_max_cap
    
    check_state(jug1_max_cap, jug2_max_cap, target_jug, target_vol)

                       
def fill_jug2(jug1_max_cap, jug2_max_cap, target_jug, target_vol):
    global curr_state
    global prev_state
    
    prev_state = tuple(curr_state)
    curr_state[1] = jug2_max_cap
    
    check_state(jug1_max_cap, jug2_max_cap, target_jug, target_vol)
                       
def empty_jug1(jug1_max_cap, jug2_max_cap, target_jug, target_vol):
    global curr_state
    global prev_state
    
    prev_state = tuple(curr_state)
    curr_state[0] = 0
    
    check_state(jug1_max_cap, jug2_max_cap, target_jug, target_vol)
                      
    
def empty_jug2(jug1_max_cap, jug2_max_cap, target_jug, target_vol):
    global curr_state
    global prev_state
    
    prev_state = tuple(curr_state)
    curr_state[1] = 0
    
    check_state(jug1_max_cap, jug2_max_cap, target_jug, target_vol)
                
    
def pour_jug1_into_jug2(jug1_max_cap, jug2_max_cap, target_jug, target_vol):
    global curr_state
    global prev_state
    
    jug1_curr_cap = curr_state[0]
    jug2_curr_cap = curr_state[1]
    
    prev_state = tuple(curr_state)
    curr_state[0] = jug1_curr_cap - min(jug2_max_cap-jug2_curr_cap, jug1_curr_cap)
    curr_state[1] = jug2_curr_cap + min(jug2_max_cap-jug2_curr_cap, jug1_curr_cap)
    
    check_state(jug1_max_cap, jug2_max_cap, target_jug, target_vol)
    
    
def pour_jug2_into_jug1(jug1_max_cap, jug2_max_cap, target_jug, target_vol):
    global curr_state
    global prev_state
    
    jug1_curr_cap = curr_state[0]
    jug2_curr_cap = curr_state[1]
    
    prev_state = tuple(curr_state)
    curr_state[0] = jug1_curr_cap + min(jug1_max_cap-jug1_curr_cap, jug2_curr_cap)
    curr_state[1] = jug2_curr_cap - min(jug1_max_cap-jug1_curr_cap, jug2_curr_cap)
    
    check_state(jug1_max_cap, jug2_max_cap, target_jug, target_vol)


def check_state(jug1_max_cap, jug2_max_cap, target_jug, target_vol):
    global curr_state
    global path
    global step_count
    
    if curr_state[target_jug] == target_vol:
        step_count += 1
        curr_state[2] = step_count
        path.add(tuple(curr_state))
        print_success()
    else:
        for i in path:
            if i[0] == curr_state[0] and i[1] == curr_state[1]:
                curr_state = list(i for i in prev_state)
                return
        step_count += 1
        curr_state[2] = step_count
        path.add(tuple(curr_state))
        decide_operation(jug1_max_cap, jug2_max_cap, target_jug, target_vol)
        

def decide_operation(jug1_max_cap, jug2_max_cap, target_jug, target_vol):
    global curr_state
    global prev_state
    global path
    
    if curr_state[0] == 0 and curr_state[1] == 0:
        # print_status(1)
        fill_jug1(jug1_max_cap, jug2_max_cap, target_jug, target_vol)
        # print_status(2)
        fill_jug2(jug1_max_cap, jug2_max_cap, target_jug, target_vol)
    elif curr_state[0] == 0:
        # print_status(3)
        # if curr_state[1] != jug2_max_cap:
        fill_jug1(jug1_max_cap, jug2_max_cap, target_jug, target_vol)
        # print_status(4)
        pour_jug2_into_jug1(jug1_max_cap, jug2_max_cap, target_jug, target_vol)
    elif curr_state[1] == 0:
        # print_status(5)
        # if curr_state[0] != jug1_max_cap:
        fill_jug2(jug1_max_cap, jug2_max_cap, target_jug, target_vol)
        # print_status(6)
        pour_jug1_into_jug2(jug1_max_cap, jug2_max_cap, target_jug, target_vol)
    else:
        # print_status(7)
        # if curr_state[1] != jug2_max_cap:
        fill_jug1(jug1_max_cap, jug2_max_cap, target_jug, target_vol)
        # print_status(8)
        # if curr_state[0] != jug1_max_cap:
        fill_jug2(jug1_max_cap, jug2_max_cap, target_jug, target_vol)
        # print_status(9)
        # if curr_state[1] != jug2_max_cap:
        empty_jug1(jug1_max_cap, jug2_max_cap, target_jug, target_vol)
        # print_status(10)
        # if curr_state[0] != jug1_max_cap:
        empty_jug2(jug1_max_cap, jug2_max_cap, target_jug, target_vol)
        # print_status(11)
        pour_jug1_into_jug2(jug1_max_cap, jug2_max_cap, target_jug, target_vol)
        # print_status(12)
        pour_jug2_into_jug1(jug1_max_cap, jug2_max_cap, target_jug, target_vol)
    
        
def main():
    input_jugs()
    
main()
