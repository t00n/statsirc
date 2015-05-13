import argparse
from collections import defaultdict
count_user = defaultdict(lambda: 0)

parser = argparse.ArgumentParser(description="Get stats from a irc log")
parser.add_argument('logfile', type=str)
args = parser.parse_args()

log = open(args.logfile, "r")
for line in log.readlines():
	# avoid netsplit, day changed, freenode moderation
	if line.strip() != "" and "::" not in line and "-!-" not in line and line[:3] != "---" and line[6] != "!":
		# /me
		if line[7] == "*":
			user = line.split(" ")[3]
		# message
		else:
			user = line.split(">")[0].split("<")[-1].strip()
		user = user.rstrip("_")
		count_user[user] += 1

total = float(sum(count_user.values()))
print "Total : ", total

array_users = sorted([(key, val) for key,val in count_user.iteritems()], key=lambda x: x[1], reverse=True)
for user in array_users:
	print user[0], ":", user[1], ":", round(float(user[1])*100.0/total, 2), "%"
