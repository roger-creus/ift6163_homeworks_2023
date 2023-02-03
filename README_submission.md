# Docker install

I created a new Dockerfile called "Dockerfile2" to install torch with GPU + Mujoco in my environment. If you have your own docker image and works well, just keep it.

(Optional) Create docker image

sudo docker build -f Dockerfile2 -t <DOCKER_IMAGE_NAME> . 

# Reproduce code

1. Start the docker image

sudo docker run --gpus 0 -v <PATH_TO_YOUR_FOLDER>:/workspace -it <DOCKER_IMAGE_NAME>

2. Run an experiment

Change the config file at conf/config_hw1.yaml and run:

cd workspace/
python3 run_hw1_bc.py

3. Generate plots

Exit the docker image. 

Define the correct paths inside the plot_curves.py to match the *.log files of the experiment you want to plot.
You will need the log file of a BC experiment and the log file of a Dagger experiment.
Once the variables are correctly defined run:

plot_curves.py 

This will output the jpg image of the curves