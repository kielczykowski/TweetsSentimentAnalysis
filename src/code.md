# Aspect Based Sentiment Analysis - code


## Requirements and usage

All scripts requirements should be placed in `requirements.txt` file. All dependencies can be installed using the following command:

``` python
pip3 install -r requirements.txt
```

### Database

Handling database connection is done using Cosmos DB with MongoDB API. Using this piece of code requires `pymongo` module installed.
Additionally to make database connection valid You need to provide the following local variables in system:

```
AZURE_DATABASE_URL
AZURE_DATABASE_USER
AZURE_DATABASE_PASSWORD
```

For development purposes (under Linux) the following `setup.bash` file was created:

``` bash
#! /bin/bash

export AZURE_DATABASE_URL=<database url>
export AZURE_DATABASE_USER=<username>
export AZURE_DATABASE_PASSWORD=<password>
```

Sourcing the file (`source ./setup.bash`) will inject presented variables into system scope. For database access contact one of the code maintainers. Written script can be used generally with other MongoDB instances by providing adequate credentials.