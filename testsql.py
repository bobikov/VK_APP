#!/usr/local/bin/python3


import pymysql.cursors
import cgi
import cgitb

print("Content-type: text/html")
print()

# cgitb.enable()
# # Using PyMySql for accessing to MySql 
# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              passwd='immortal',
#                              db='chats',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)
# try:
# 	# with connection.cursor() as cursor:
# 		# sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
# 		# cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

# 		# sql = "INSERT INTO `users` (`email`, `username`) VALUES (%s, %s)"
# 		# cursor.execute(sql, ('admin@chatbox.com', 'admin'))


# 	# connection.commit()

# 	with connection.cursor() as cursor:
# 		sql = "SELECT * FROM `users`"
# 		cursor.execute(sql)
# 		result = cursor.fetchall()
# 		print("<table>")
# 		for value in result:
# 			print("<tr><td>" + str(value['id']) + "</td><td>" + str(value['username']) + "</td><td>" + str(value['password']), str(value['confirm']) + "</td></tr>")
# 		print("</table>")	
# finally:
# 	connection.close()


#Testing Python Cycles
def list1(n):
	""" Making increase value of every element in list using WHILE cycle """
	i=-1;
	arr = [1, 1, 1, 1, 1]
	while i < len(arr)-1:
		i+=1
		arr[i]+=n
	return print(arr)

def list2(n):
	""" Making increase value of every element in list using FOR cycle """
	arr=[1, 1, 1, 1, 1]
	arr = [x+n for x in arr]
	return print(arr)

print(list1.__doc__)