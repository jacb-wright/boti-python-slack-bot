import logging
import os
from datetime import date, datetime
from pathlib import Path
from typing import Optional
from urllib.request import urlopen

import fire
import pandas as pd
from ics import Calendar

logger = logging.getLogger(__file__)
today = datetime.today().strftime('%Y-%m-%d')

print ("todays date --> ",today)

def main(output: Optional[str] = "my-output.csv", url: Optional[str] = "https://outlook.office365.com/owa/calendar/34c495a664ea44d0a7ceeaf02fa56955@computacenter.com/164d55d19dfc44678780031afbb35cb816007673447775235462/calendar.ics"):
    if not url:
        logger.error("URL argument or CAL_ICS_URL env variable must be set")
        quit()

    logger.info("Reading calendar")
    cal = Calendar(urlopen(url).read().decode("iso-8859-1"))

    # get events
    events = [e.__dict__ for e in cal.events]
    logger.info(f"Fetched {len(events)} events")

    # create dataframe
    df = pd.DataFrame(events)
    df['new_date'] = [d.date() for d in df['_begin']] #parsing date from datetime column
    df['new_date'] = pd.to_datetime(df.new_date) #fixing date time format from object to datetime
    df = df.loc[df['new_date'] == today] #rewrite df to only meetings from today
    my_list_events = df["name"].tolist()
    print("Today's events are -->")
    for i in my_list_events:
        print(i)
    #return my_list_events
    #print(my_list_events)
    #df.to_csv(output, index=False)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fire.Fire(main)
