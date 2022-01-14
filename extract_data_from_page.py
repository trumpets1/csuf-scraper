import numpy as np, pandas as pd
import bs4



# children = list(filter(lambda child: child.name != 'br',
#                 get_info_from_page(url).contents))

# new_children = np.array(children, dtype='object')

# def is_h1(x): return x.name == 'h1'

# is_h1_vec = np.vectorize(is_h1)
# bool_arr = is_h1_vec(new_children)
# print(new_children[bool_arr])