# osint-alumnforce

Looking for people across websites that are using Alumnforce SaaS solution (a people directory solution for organizations).

## parameters

Parameters to fill hardcoded before the launch of that script:

**firstname**: string   
*in case of compound first name, use the following character: -*

**lastname**: string   
*in case of compound last name, use the following character: -*

## launch

To execute: 
```bash
$ python3 alumnforce.py >> output.txt
```

## output

Please use the bash command **grep** with the following parameters in your result output:   
- ``"Graduated from"``   
- ``"Pending validation of"`` 
- ``"Diplômé(e) de"`` 
- ``"En attente de validation"``  

© CERT-HM Le CERT des hypermarchés Mammouth
```
 __  __      _           _____    _           ____            _
|  \/  | ___| |_ _ __ __|_   ____| | ___ ___ |  _ \  ___   __| | ___
| |\/| |/ _ | __| '__/ _ \| |/ _ | |/ __/ _ \| | | |/ _ \ / _` |/ _ \
| |  | |  __| |_| | | (_) | |  __| | (_| (_) | |_| | (_) | (_| | (_) |
|_|  |_|\___|\__|_|  \___/|_|\___|_|\___\___/|____/ \___/ \__,_|\___/
```
