# CS-7641 Machine Learning Project 4 - Markov Decision Processes


**Contents**

    * Test Environment
    * Dependencies
    * Automated Setup
    * Manual Setup
    * Execution
    * Test Times
    * Citations


**Test Environment**

    * Host:

        * Operating System:         Windows 10 Professional
        * Motherboard:              ASUS ROG Maximus XI Hero (Intel Z390 Chipset)
        * CPU:                      Intel Core-i7 9700k @3.6GHz (8 physical cores, 8 threads)
        * RAM:                      32GB (4 x 8GB) DDR4 4133 (PC4 33000)
        * Storage:                  2x Samsung 850 EVO 500GB (1TB total) SSDs in hardware RAID-0

    * Virtualization:

        * Virtual Machine Manager:  Virtualbox 5.2.22r126460
        * Operating System:         Linux Mint 19.1 'Tessa' 64-bit
        * CPU Architecture:         x64/amd64
        * CPU Cores:                2
        * RAM:                      4GB
        * Storage:                  20GB


**Dependencies**

    * Linux Mint 19.1+ 'Tessa' or equivalent (Ubuntu 18.04 LTS 'Bionic Beaver' should work with no issues)
    * Python 3.6.7+ (other recent versions will likely work, but only 3.6.7 has been tested)
    * python3-pip=9.0.1-2.3~ubuntu1 (not required for manual setup, but suggested)
    * python3-tk=3.6.7-1~18.04
    * virtualenv (not required, but suggested)
    * The Python packages/versions listed in ./requirements.txt


**Automated Setup**

    * The 'easy' way is to run ./setup.sh from the top-level directory of the repository.

        * This will install all necessary Linux/Python packages, provided the 1st 2 dependencies above are met.
        * This will also set up a virtual environment and provide instructions on how to execute the experiments.


**Manual Setup**

    1. Install the following:

        * python3-pip=9.0.1-2.3~ubuntu1 (not required for manual setup, but suggested)
        * python3-tk=3.6.7-1~18.04
        * virtualenv (not required, but suggested)

    2. Install all Python packages listed in the requirements.txt file (version numbers are provided)


**Execution**

    1. If using virtualenv, run:

        source bin/activate

    2. Use the run_experiment.py script, which dumps all results in the output directory defined for each dataset:

        python run_experiment.py --all --plot --verbose

    3. When completed, if using virtualenv, run:

        deactivate

    NOTE: run_experiments.py arguments:

        --threads     Number of threads (defaults to -1 for auto)
        --seed        A random seed to set, if desired
        --policy      Run the Policy Iteration (PI) experiment
        --value       Run the Value Iteration (VI) experiment
        --ql          Run the Q-Learner (QL) experiment
        --all         Run all experiments (policy, value, ql)
        --plot        Plot data results
        --verbose     If true, provide verbose output (defaults to false)
        --help        Display the help message and exit


# TODO: UPDATE QL run times and total run time
**Test Times**

    * The following are the test times using the test environment described above for each dataset/experiment
      combination executed individually, along with cummulative total times for each dataset:

        * Policy Iteration:

            * Frozen Lake:          00h 28m 05s
            * Large Frozen Lake:    01h 02m 31s
            * Cliff Walking:        00h 09m 41s
            * Total:                01h 40m 17s

        * Value Iteration:

            * Frozen Lake:          00m 11s
            * Large Frozen Lake:    00m 28s
            * Cliff Walking:        00m 11s
            * Total:                00m 50s

        * Q-Learning:

            * Frozen Lake:          14m 21s
            * Large Frozen Lake:    26m 28s
            * Cliff Walking:        25m 30s
            * Total:                56m 19s

    * The total run time if all experiments are executed using the test environment described above:

        * Total Run Time:   58m 37s


**Citations**

    * All code, except as listed below, was adopted from Chad Maron's publicly available CS-7641 repository:

        * https://github.com/cmaron/CS-7641-assignments/tree/master/assignment4

    * The following code was developed solely by me:

        * ./setup.sh

