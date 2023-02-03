import matplotlib.pyplot as plt
import numpy as np

dagger_data = "/home/roger/Desktop/ift6163_homeworks_2023/outputs/2023-01-22/09-09-47/data/q2_bob_Walker2d-v2_22-01-2023_09-09-47/log_file.log"
behaviour_cloning_data = "/home/roger/Desktop/ift6163_homeworks_2023/outputs/2023-01-22/08-50-23/data/q1_bob_Walker2d-v2_22-01-2023_08-50-23/log_file.log"

# We are only going to keep this info
keep_phrases_returns = ["Eval_AverageReturn"]
keep_phrases_expert = ["Initial_DataCollection_AverageReturn"]
keep_phrases_errors = ["Eval_StdReturn"]

# read behaviour cloning performance from log file
with open(behaviour_cloning_data) as f:
    f = f.readlines()
for line in f:
    for phrase in keep_phrases_returns:
        if phrase in line:
            bh_performance = float(line.split(":")[2][1:-2])
            break
    for phrase in keep_phrases_expert:
        if phrase in line:
            expert_performance = float(line.split(":")[2][1:-2])
            break

# read Dagger retruns and std error across iterations
returns = []
errors = []
with open(dagger_data) as f:
    f = f.readlines()
for line in f:
    for phrase in keep_phrases_returns:
        if phrase in line:
            returns.append(float(line.split(":")[2][1:-2]))
            break
    for phrase in keep_phrases_errors:
        if phrase in line:
            errors.append(float(line.split(":")[2][1:-2]))
            break

returns = np.concatenate([np.array([0]), np.array(returns)])
errors = np.concatenate([np.array([0]), np.array(errors)])

# generate the plot
x_data = np.arange(len(returns))
plt.figure()
plt.plot(x_data, returns, label="Dagger")
plt.fill_between(x_data, returns - errors, returns + errors, alpha = 0.2)
plt.axhline(y = bh_performance, color = 'r', linestyle = '-', label="Behaviour Cloning")
plt.axhline(y = expert_performance, color = 'g', linestyle = '-', label="Expert Policy")
plt.xlabel('Number of iterations')
plt.ylabel('Avg. Eval return')
plt.legend(loc="center right")
plt.savefig("dagger_curves.jpg")