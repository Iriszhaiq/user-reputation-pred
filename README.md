# Stack Exchange - User Reputation Prediction

> predict the reputation levels of users.

1. `Reputation_prediction_data_train.txt` - This contains the data that you need to use to make your prediction on how reputed a specific user is. Each line corresponds to an individual content that has been created on this stack exchange, consisting of `4` columns - `[Textual Description, User ID, Content Type, Time Stamp]`. 

    - **Textual Description** contains the text that was posted as a part of this content. Note that we have pre-processed the text for you. By pre-processing, we mean that we have passed the text through well-known NLP pre-processing techniques including stop-word removal, stemming, lemmatization etc. The processed text will help you extract more meaningful features if you decide to use the text content in your classification task.
    - **User ID** is a unique identifier for each user. 
    - **Content Type** is the nature of the current content i.e. whether it is a question(`Q`) , answer (`A`), comment (`C`), favorite (`F`) or edit (`E`). 
    - **Time Stamp** is the relative time at which the content was created within the timeline of the stack exchange. This is not the actual time stamp, but rather a relative fraction that was computed taking into account the earliest and last time stamp over all content on this stack exchange.

2. `Reputation_prediction_labels_train.txt` - This contains the labels for the set of users in the training data. Each line consists of 2 columns - `[User ID, User Reputation]`. User Reputation is a number assigned to a user based on his/her reputation and quality of contribution to the stack exchange. It assumes a value in the set `[1,2,3]`. Value `1` indicates users with *high* reputation scores, conversely value `3` indicates a *low* score.

