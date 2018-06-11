from jira import JIRA
import netrc

import calendar
import datetime
from dateutil import parser


class Workload():

    def __init__(self):
        secrets = netrc.netrc()
        self.username, self.account, password = secrets.authenticators('jira')
        self.jira = JIRA(options={'server': self.account}, basic_auth=(self.username, password))

    def getFirstDate(self, date):
        newDate = datetime.date(date.year, date.month, 1)
        return newDate

    def getLastDate(self, date):
        newDate = datetime.date(date.year, date.month, calendar.monthrange(date.year, date.month)[1])
        return newDate

    def getWorkloadPerIssue(self, date):
        workload = {}

        jql = "timeSpent is not EMPTY AND worklogDate >= " + self.getFirstDate(date).strftime(
            "%Y-%m-%d") + " AND worklogDate <= " + self.getLastDate(date).strftime(
            "%Y-%m-%d") + " AND assignee was " + self.username

        issues = self.jira.search_issues(jql, startAt=0, maxResults=10000, validate_query=True, fields=None,
                                         expand='changelog', json_result=None)

        for issue in issues:
            for history in issue.changelog.histories:
                created = parser.parse(history.created).date()
                if created >= self.getFirstDate(date) and created <= self.getLastDate(
                        date) and history.author.key == self.username:
                    for item in history.items:
                        if 'timespent' == item.field:
                            if item.fromString == None:
                                fromValue = 0
                            else:
                                fromValue = int(item.fromString)

                            if item.toString == None:
                                toValue = 0
                            else:
                                toValue = int(item.toString)

                            if issue not in workload:
                                workload[issue] = 0

                            workload[issue] += toValue - fromValue

        return workload
