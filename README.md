# Hidetext

Extensible Python library to hide fragments of text.

## Installation

## Basic usage


```python
from hidetext import Hidetext

hide = Hidetext()

print(hide.character("""
Dear Mr Robinson,

I'm contacting you regarding 
My DNI is 43244328J.

Email: fdsfsd@gmail.com
"""))
```

    
    Dear Mr Robinson,
    
    I'm contacting you regarding 
    My DNI is *********.
    
    Email: ****************
    



```python
print(hide.kind("""
Dear Mr Robinson,

I'm contacting you regarding 
My DNI is 43244328J.

Email: fdsfsd@gmail.com
"""))
```

    
    Dear Mr Robinson,
    
    I'm contacting you regarding 
    My DNI is <ID_CARD>.
    
    Email: <EMAIL>
    


## Creating custom filters

It's easy to create custom filters to remove undesired text using `PatternFilter`:


```python
from typing import Dict

from hidetext import Hidetext
from hidetext.filters import PatternFilter

class HourFilter(PatternFilter):
    name: str = "HOUR"

    patterns: Dict[str, str] = {
        "digital_hour": r"\d{2}(:\d{2}){1,2}",
        "hour": "\d{1,2}\s?(am|pm)"
    }

hide = Hidetext(filters=[HourFilter()])

hide.kind("The train departs at 15:45 and arrives at 19:35, therefore I'll be at the party at 8pm.")
```




    "The train departs at <HOUR> and arrives at <HOUR>, therefore I'll be at the party at <HOUR>."


