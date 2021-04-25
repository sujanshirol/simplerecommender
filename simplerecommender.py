# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 19:59:10 2021

@author: sshir
"""

def rec(df, genre_col, user_col, user, user_rating_col, avg_rating_col, sep=None):
    '''
    Recommending items for a specific existing user based on user rating 
    and average rating per item.
    
    Parameters
    ----------
    df : Pandas DataFrame
        Entire or part of DataFrame that containe the remaining below mentioned parameters.
    genre_col : str
        Column name that contains the genre.
    user_col : str
        Column name that contains user ID.
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
        df_copy[genre_col] = df_copy[genre_col].apply(lambda x: x.split(sep)[0].strip())
    user_details = df_copy[df_copy[user_col] == user]
    user_details = user_details[user_details[genre_col]==user_details[genre_col].value_counts().index[0]]
    
    #find the maximum of rating
    user_max_rating = max(user_details.user_rating)

    #fetching the max rated genre by the user
    for i in user_details.index:
        user_ratings = user_details[user_details.index == i][user_rating_col].values[0]
        if user_ratings == user_max_rating:
            index = (user_details[user_details.index == i][user_rating_col] == user_max_rating).index[0]

    liked_genre = user_details[user_details.index==index][genre_col].values[0]

    #recommendation based on highly rated animes by the genre that is max rated by the user
    rec = df_copy[df_copy[genre_col] == liked_genre].sort_values(avg_rating_col, ascending=False)

    #removing the anime's already watched by the user
    rec.drop_duplicates(avg_rating_col, inplace=True)
    for i in user_details.index:
        if i in rec.index:
            rec.drop(i, inplace=True)
    return rec.head(5)