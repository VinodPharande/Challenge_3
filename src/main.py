import objectpath


class main:

	def get_value(data, key):
		try:
			print("Executing function get_value...")
			print("Info - data: ", data)
			print("Info - data: ", data)
			procesed_json = objectpath.Tree(data)
			print("Info - procesed_json: ", procesed_json)
			res_tuple = tuple(processed_json.execute(f'$..{key}'))
			print("Info - res_tuple: ", res_tuple)
			return res_tuple
		except Exception as ex:
			print("Error - Something went wrong in function get_value: ", ex)
			

if __name__ == '__main__':
	obj = {
		"a": {
			"b": {
				"c": "d"
			}
		}
	}
	
	result = main.get_value(obj, "c")
	#result = main.get_value(obj, "b")
	#result = main.get_value(obj, "a")
	print("Info - result: ", result)