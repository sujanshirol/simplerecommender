# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 19:59:10 2021

@author: sshir
"""

def rec(df, item_col, user_col, user, user_rating_col, avg_rating_col, sep=None):
    '''
    Recommending items for a specific existing user based on user rating 
    and average rating per item. Returns only the items which are not consumed
    by the user. If there is only one such item present then returns empty DataFrame.
    
    Parameters
    ----------
    df : Pandas DataFrame
        Entire or part of DataFrame that containe the remaining below mentioned parameters.
    item_col : str
        Column name that contains the item.
    user_col : str
        Column name that contains user ID. Values in the column must be of dtype int
    user : int
        ID of the user for whom we need to recommend items.
    user_rating_col : str
        Column name that contains user ratings.
    avg_rating_col : str
        Column name that contains average rating of each item.
    sep : str [',', '/', '|'], optional
        Delimiter to use for genre column. For example: if genre column comtains multiple
        genres lile Drama, Action, Comedy or Drama / Action / Comedy. Default value is None

    Returns
    -------
    Pandas DataFrame
        Comma-seperated values containig recommended items for user with user_id
        and item details

    '''
    df_copy = df.copy()
    if sep != None:
        df_copy[item_col] = df_copy[item_col].apply(lambda x: x.split(sep)[0].strip())
    user_details = df_copy[df_copy[user_col] == user]
    user_details = user_details[user_details[item_col]==user_details[item_col].value_counts().index[0]]
    
    #find the maximum of rating
    user_max_rating = max(user_details[user_rating_col])

    #fetching the max rated genre by the user
    for i in user_details.index:
        user_ratings = user_details[user_details.index == i][user_rating_col].values[0]
        if user_ratings == user_max_rating:
            index = (user_details[user_details.index == i][user_rating_col] == user_max_rating).index[0]

    liked_item = user_details[user_details.index==index][item_col].values[0]

    #recommendation based on highly rated items by the genre that is max rated by the user
    rec = df_copy[df_copy[item_col] == liked_item].sort_values(avg_rating_col, ascending=False)

    #removing the items already watched by the user
    rec.drop_duplicates(avg_rating_col, inplace=True, keep='last')
    for i in user_details.index:
        if i in rec.index:
            rec.drop(i, inplace=True)
    return rec.head(5)