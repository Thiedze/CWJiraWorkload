# jira-workload
A little python script to create a monthly workload of a given user from jira 

## ~/.netrc
Create a .netrc file like to following:

machine jira
	account <YOUR_JIRA_URL>
	login <YOUR_JIRA_USERNAME>
	password <YOUR_PASSWORD>

# Python packages
You need *pip install py-utils* and *pip install jira*

## Selected year and month
Change "date = datetime.date(2018, 6, 1)" to your wish year and month to get all jira issues with the total workload on it.  

## Output
The output is a confluence markup formatted console output. You can esaly copy & paste it into the markup editor of conflluence to report your workload.   
