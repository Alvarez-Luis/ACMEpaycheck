from datetime import datetime

class calc_methods:

    def __init__(self) -> None:
        self.week_schedule1_start = datetime.strptime('00:01', '%H:%M').time()
        self.week_schedule1_end = datetime.strptime('09:00', '%H:%M').time()
        self.week_schedule2_start = datetime.strptime('09:01', '%H:%M').time()
        self.week_schedule2_end = datetime.strptime('18:00', '%H:%M').time()
        self.day_time1 = None
        self.day_time2 = None


    def payment_calc(self, day, week):
        paycheck = 0
        self.day_time1 = datetime.strptime(day[2:7], '%H:%M')
        self.day_time2 = datetime.strptime(day[8:13], '%H:%M')

        if self.day_time1.time() >= self.week_schedule1_start and self.day_time2.time() <= self.week_schedule1_end:
            time = (self.day_time2-self.day_time1)
            time = str(time)[:1]
            paycheck += int(time)*(25 if week else 30)
        elif self.day_time1.time() >= self.week_schedule2_start and self.day_time2.time() <= self.week_schedule2_end:
            time = (self.day_time2-self.day_time1)
            time = str(time)[:1]
            paycheck += int(time)*(15 if week else 20)
        else:
            time = (self.day_time2-self.day_time1)
            time = str(time)[:1]
            paycheck += int(time)*(20 if week else 25)
        
        return paycheck


    @staticmethod
    def is_weekend(day) -> bool:
        DAYS_OF_WEEKEND = ['SA','SU']
        return day in DAYS_OF_WEEKEND