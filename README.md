# Hidetext

A python library to hide fragments of text.

## Installation

## Examples


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
    

