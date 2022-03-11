'''
ref --> ['teamname] : [[points,Net runrate],[run rates for each match]]
'''
ref = {'MI':[[0,0],[]],
       'DC':[[0,0],[]],
       'RR':[[0,0],[]],
       'SRH':[[0,0],[]],
       'CSK':[[0,0],[]],
       'KKR':[[0,0],[]],
       'RCB':[[0,0],[]],
       'PBKS':[[0,0],[]]}

# detail = "MI 191/10 110 CSK 190/4 120"

def print_records(ref):
    for key in ref:
        print(key, end = ': ')
        print(ref[key])
    print("\n")

for match_number in range(10):
    match_details = list(map(str, input().split()))
    # match_details = list(map(str, detail.split()))
    first_team_name = match_details[0]
    first_team_runs,first_team_wickets = map(int, match_details[1].split('/'))
    first_team_balls = int(match_details[2])
    second_team_name = match_details[3]
    second_team_runs,second_team_wickets = map(int, match_details[4].split('/'))
    second_team_balls = int(match_details[5])

    # print(first_team_name, first_team_runs, first_team_wickets, first_team_balls)
    # print(second_team_name, second_team_runs, second_team_wickets, second_team_balls)
    
    if first_team_runs > second_team_runs:
        # ADD POINTS TO FIRST TEAM/WIN TEAM
        ref[first_team_name][0][0] += 2
        # CALCULATE RUN RATE
        run_rate = (first_team_runs - second_team_runs)*0.05
        # APPEND THE RUN RATE TO RESPECTIVE TEAM DICTIONARY
        ref[first_team_name][1].append(run_rate)
        ref[second_team_name][1].append(-1*run_rate)
    
    elif second_team_runs > first_team_runs:
        # ADD POINTS TO SECOND TEAM/WIN TEAM
        ref[second_team_name][0][0] += 2
        # CALCULATE PROJECTED RUNS
        projected_runs = 120*(second_team_runs)//(second_team_balls)
        # CALCULATE RUN RATE
        run_rate = (projected_runs - first_team_runs)*0.5
        # APPEND THE RUN RATE TO RESPECTIVE TEAM DICTIONARY
        ref[second_team_name][1].append(run_rate)
        ref[first_team_name][1].append(-1*run_rate)
    else:
        if second_team_runs != first_team_runs:
            break
        # ADD 1 POINT TO BOTH TEAMS AS ITS A DRAW
        ref[second_team_name][0][0] += 1
        ref[first_team_name][0][0] += 1
        # RUN RATE IS ZERO SINCE ITS DRAW
        run_rate = 0
        # APPEND THE RUN RATE TO RESPECTIVE DICTIONARY
        ref[second_team_name][1].append(run_rate)
        ref[first_team_name][1].append(-1*run_rate)
    # break

# print_records(ref)
for team in ref:
    net_run_rate = sum(ref[team][1]) // len(ref[team][1])
    # print(sum)
    ref[team][0][1] = net_run_rate
# print_records(ref)

def print_sorted_teamnames(ref):
    a,b,c = [],[],[]
    for team_name in ref:
        a.append(team_name)
        b.append(ref[team_name][0][0])
        c.append(ref[team_name][0][1])
    # print(a,b,c)

    for i in range(8):
        for j in range(i+1,8,1):
            if b[i] < b[j]:
                a[i],a[j] = a[j],a[i]
                b[i],b[j] = b[j],b[i]
                c[i],c[j] = c[j],c[i]
            elif b[i] == b[j]:
                if c[i] < c[j]:
                    a[i],a[j] = a[j],a[i]
                    b[i],b[j] = b[j],b[i]
                    c[i],c[j] = c[j],c[i]
    return a,b,c

team_name_list,b,c = print_sorted_teamnames(ref)

for team_names in team_name_list:
    print(team_names)
