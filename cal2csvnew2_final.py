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
#d = datetime.now()
#today = d.strftime('X%m/X%d/%Y').replace('X0','X').replace('X','')
print ("todays date --> ",today)
###start_date = today
###print ("start date --> ",start_date)
###end_date = today
###print ("end date --> ",end_date)

def main(output: Optional[str] = "my-output.csv", url: Optional[str] = "https://outlook.office365.com/owa/calendar/34c495a664ea44d0a7ceeaf02fa56955@computacenter.com/164d55d19dfc44678780031afbb35cb816007673447775235462/calendar.ics"):
#def main(output: Optional[str] = "my-output.csv", url: Optional[str] = "https://outlook.office365.com/owa/calendar/34c495a664ea44d0a7ceeaf02fa56955@computacenter.com/164d55d19dfc44678780031afbb35cb816007673447775235462/calendar.html"):

    # get calendar
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
    ###print (df.columns)
    #print (df[['_begin', 'name']])

#    for index, row in df.iterrows():
#        print(index, row['_begin', 'name'])
#
    #print (df.sort_values('_begin', ascending=False))
    df['new_date'] = [d.date() for d in df['_begin']] #parsing date from datetime column
    df['new_date'] = pd.to_datetime(df.new_date) #fixing date time format from object to datetime
    ###print (df)
    ###print (df.columns)
    ##print (today)
    ##print (df.sort_values('new_date', ascending=False))
    ##print (df.dtypes)
    #print (df.loc[df['_begin'].str.contains('2021-02-24')])

    ###print (df.loc[df['new_date'] == today]) #listing meeing from todays date
    # dump output

    if not output:
        now = datetime.now().strftime("%Y-%m-%d")
        output = Path(__file__).parent / f"{now}_calendar.csv".resolve()
        output = output.resolve()
    else:
        output = Path(output)
    logger.info(f"Saving to {output.resolve()}")
    df = df.loc[df['new_date'] == today] #rewrite df to only meetings from today
    df.to_csv(output, index=False)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fire.Fire(main)
