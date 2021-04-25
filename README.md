# simplerecommender
Recommending items for a specific existing user based on user rating and average rating per item.

[Link to PyPI ](https://pypi.org/project/simplerecommender) 

## Installation

Run the following to install:

```python
pip install simplerecommender
```

## Usage

```python
import simplerecommender

# get recommendations
simplerecommender.rec(df,
                      genre_col,
                      user_col,
                      user,
                      user_rating_col,
                      avg_rating_col,
                      sep=None)
```

## Future works
1. Get rid of parameter avg_rating_col
2. Optimization
3. Add more functionality

## Drawbacks
1. Need of both average rating per item and user ratings to all the items
2. Limited to existing users only
3. Not an optimal algorithm
