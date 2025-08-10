# Colon ion and fluid transport FTU
This project contains the CellML bond graph modules and circulatory autogen input files for generating a functional tissue unit (FTU) of ion and fluid transport in the distal colon. 

# Overview

## Full model
*Insert an image of full bond graph model*

## Modules
### Compartments
####

### Membranes

### Proteins
#### Epithelial Sodium Channel (ENaC)
#### Na/K-ATPase
#### Aquaporin
#### K-leak channel

### Processes
#### Diffusion
#### Solvent drag (advection)

# How to use

## Circulatory autogen installation
This project uses the model generation capabilities of [Circulatory autogen](https://github.com/FinbarArgus/circulatory_autogen/tree/master) to couple modules into the distal colon FTU. Follow the [getting started](https://github.com/FinbarArgus/circulatory_autogen/blob/master/tutorial/docs/getting-started.md) documentation to install circulatory autogen. As part of this process, you will install OpenCOR, which will be used to run the generated FTU.

## Update paths
Before running circulatory autogen, open the file: 

circulatory_autogen > user_run_files > user_inputs.yaml 

and update:

user_inputs_path_override: [colon_FTU_dir]/CA_colon_FTU/colon_FTU_user_inputs.yaml


# Directory structure


# Citation
*Insert journal citations when this model is published.*

# Acknowledgement
This work was funded by the Auckland Bioengineering Insitute 12 Labours project grant from the Ministry of Business Innovation and Employment’s Catalyst: Strategic fund. 

# License


# Contact
If you're interested in collaborating or have any questions about the model, please contact j.dowrick@auckland.ac.nz