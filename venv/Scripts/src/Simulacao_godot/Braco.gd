extends Node2D

var http_request = HTTPRequest.new()

func _ready():
	# Create an HTTP request node and connect its completion signal.
	add_child(http_request)
	http_request.request_completed.connect(self._http_request_completed)
	
	# Send a GET request to get the current robot position.
	http_request.request("http://127.0.0.1:3000/robot/position",[], HTTPClient.METHOD_GET)
	
func _http_request_completed(result, response_code, headers, body):
	if result == HTTPRequest.RESULT_SUCCESS:
		# Parse the JSON response.
		var json_data = JSON.new()
		json_data.parse(body.get_string_from_utf8())
		var response = json_data.get_data()
		print(response)
		#var positionX = response['positionX']
		#var positionY = response['positionY']
		#var positionZ = response['positionZ']
		#var rot = response['rotation']
		#print(response.headers["User-Agent"])
		#print("PositionX atual: ({positionX})".format(response))
		#print("PositionY atual: ({positionY})".format(response))
		#print("PositionZ atual: ({positionZ})".format(response))
		#print("rotation atual: ({rotation})".format(response))
		for position in response:
				await get_tree().create_timer(1).timeout
				print(position)
				$Pngwingcom.position.x = position[1]
				$Pngwingcom.position.y = position[2]
			
				$Pngwingcom.modulate.r = position[3]
				$Pngwingcom.modulate.g = position[1]
			
				$Pngwingcom.rotation = position[4]
			
		$Timer.start()
	else:
		print("HTTP request failed with error code: {}".format(response_code))

func _on_timer_timeout():
	$Timer.wait_time = 1
	http_request.request("http://127.0.0.1:3000/robot/position")
