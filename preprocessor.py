# import re
# import pandas as pd

# def preprocess(data):
#     pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'

#     messages = re.split(pattern, data)[1:]
#     dates = re.findall(pattern, data)

#     df = pd.DataFrame({'user_message': messages, 'message_date': dates})
#     # convert message_date type
#     df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%Y, %H:%M - ')

#     df.rename(columns={'message_date': 'date'}, inplace=True)

#     users = []
#     messages = []
#     for message in df['user_message']:
#         entry = re.split('([\w\W]+?):\s', message)
#         if entry[1:]:  # user name
#             users.append(entry[1])
#             messages.append(" ".join(entry[2:]))
#         else:
#             users.append('group_notification')
#             messages.append(entry[0])

#     df['user'] = users
#     df['message'] = messages
#     df.drop(columns=['user_message'], inplace=True)

#     df['only_date'] = df['date'].dt.date
#     df['year'] = df['date'].dt.year
#     df['month_num'] = df['date'].dt.month
#     df['month'] = df['date'].dt.month_name()
#     df['day'] = df['date'].dt.day
#     df['day_name'] = df['date'].dt.day_name()
#     df['hour'] = df['date'].dt.hour
#     df['minute'] = df['date'].dt.minute

#     period = []
#     for hour in df[['day_name', 'hour']]['hour']:
#         if hour == 23:
#             period.append(str(hour) + "-" + str('00'))
#         elif hour == 0:
#             period.append(str('00') + "-" + str(hour + 1))
#         else:
#             period.append(str(hour) + "-" + str(hour + 1))

#     df['period'] = period

#     return df

import re
import pandas as pd

def preprocess(data):
    # Pattern to extract date and time in the WhatsApp format
    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'

    # Extract messages and dates using regex
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    # Create a DataFrame with messages and corresponding dates
    df = pd.DataFrame({'user_message': messages, 'message_date': dates})

    # Convert message_date to datetime with error handling
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%Y, %H:%M - ', errors='coerce')

    # Rename the message_date column to 'date' for consistency
    df.rename(columns={'message_date': 'date'}, inplace=True)

    # Handle user and message separation from the 'user_message' column
    users = []
    messages = []
    for message in df['user_message']:
        # Extract the username and the actual message content
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:  # Check if there's a valid user and message
            users.append(entry[1])  # Add the user
            messages.append(" ".join(entry[2:]))  # Add the message
        else:
            # For system messages or group notifications
            users.append('group_notification')
            messages.append(entry[0])

    # Add user and message columns to the DataFrame
    df['user'] = users
    df['message'] = messages

    # Drop the original 'user_message' column
    df.drop(columns=['user_message'], inplace=True)

    # Drop rows where the date couldn't be parsed (NaT values)
    df.dropna(subset=['date'], inplace=True)

    # Add additional date and time-related columns
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    # Generate time period ranges
    period = []
    for hour in df['hour']:
        if hour == 23:
            period.append(f"{hour}-00")
        elif hour == 0:
            period.append("00-01")
        else:
            period.append(f"{hour}-{hour+1}")
    
    # Add the period column to the DataFrame
    df['period'] = period

    return df