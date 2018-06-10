import datetime
from workload import Workload

date = datetime.date(2018, 6, 1)

workload = Workload()
issues = workload.getWorkloadPerIssue(date)

totalWorkload = 0
print "| Issue | Workload |"
for issue in issues:
    totalWorkload += issues[issue]
    print "|[" + issue.key + "|"+ workload.account + issue.key + "] " + issue.fields.summary + "| " + str(
        float(issues[issue]) / 3600) + "h|"

print "| Total |*" + str(float(totalWorkload) / 3600) + "h*|"
