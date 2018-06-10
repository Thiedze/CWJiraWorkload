# CWJiraWorkload
A little python script to create a monthly workload of a given user from jira 

## ~/.netrc
Create a .netrc file like to following:
```
machine jira
	account <YOUR_JIRA_URL>
	login <YOUR_JIRA_USERNAME>
	password <YOUR_PASSWORD>
```
# Python packages
You need *pip install py-dateutils* and *pip install jira*

## Selected year and month
Change "date = datetime.date(2018, 6, 1)" to your wish year and month to get all jira issues with the total workload on it.  

## Output
The output is a confluence markup formatted console output. You can esaly copy & paste it into the markup editor of conflluence to report your workload.   

## Outpu example
```
| Issue | Workload |
|[AA-7|<YOUR_ACCOUNT>/AA-7] Summary AA| 2.0h|
|[AB-6|<YOUR_ACCOUNT>/AB-6] Summary AB| 2.0h|
|[AA-5|<YOUR_ACCOUNT>/AA-5] Summary AA| 3.0h|
| Total |*7.0h*|
```
