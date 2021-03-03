import os

toinstall=["react", "react-dom", "webpack", "webpack-cli", "@babel/core", "babel-loader", "@babel/preset-react", "@babel/preset-env"];

for i in toinstall:
	os.system("npm install {} --save-dev".format(i))
