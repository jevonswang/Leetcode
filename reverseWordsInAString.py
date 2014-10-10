class Solution:
	# @param s, a string
	# @return a string
	def reverseWords(self, s):
		if(s==""):
			return ""
		ret = ""
		word = s.split(" ")
		word.reverse()
		for w in word:
			if(w!=""):
				ret += w+" "
		return ret[0:-1]