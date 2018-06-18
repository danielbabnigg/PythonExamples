#variables in strings
welcome = "Hello everyone!"
print (welcome)

pi = 3.14
print (str(pi))

#escaping characters
print ("There\'s a snake!")

#variable string shortcuts
name = "Daniel"
age = "15"
color = "orange"
print ("Hello, my name is %s and I am %s years old, my favorite color is %s." % (name,age,color))

#slicing strings
message1 = "HXeylAlsoS ahsoSwa DasraeY tyAoauo?"
message = message1[::2]
print (message)

encodedmessage = "XTXXhXXXXiXXs XiXXXsXX XaXXX XXXvXXerXXXXy XXsXXeXXXXXXXcXXXXXXrXeXXXtXXXXX XXmXXXeXsXXsXXaXgXXXeX.XXX"
newmessage = filter(lambda x: x != "X", encodedmessage)
print (newmessage)